============================
进程、线程、微线程和事件驱动
============================

内核级 VS 用户级
================

* 普通程序运行于用户级
* 通过system call调用内核程序 (TRAP指令)

进程 - 一段程序的顺序执行
=========================

* 抢占式调度
* 独立的地址空间

线程
====

* 共享地址空间的进程
* 对调度器来说和进程没有区别

内核调度时机 - 事件驱动
=======================

* 时钟中断触发抢占式调度
* IO中断触发内核线程的阻塞和唤醒

用户级线程 - 微线程/绿线程/协程
===============================

* 在用户级调度不同的代码执行序列
* 好处：开销小
* 坏处：需要避开阻塞的系统调用

用户级调度器的调度时机
======================

* 由解释器进行调度

* 代码主动切换 (协作式调度)

抢占式调度 VS 协作式调度
========================

* 抢占式调度容易出现: 关键区域(Critical Section)的同步

* 协作式调度容易出现：饥饿

线程模型
========

线程数量:内核调度单元

* 1:1 系统线程

* M:1 greenlet的线程

* M:N golang/haskell的线程

事件驱动编程
============

* 内核的事件驱动：中断

* 多播IO：select/poll/epoll/kqueue/IOCP

事件驱动主循环
==============

.. code-block:: python

    while True:
        events = epoll_wait()
        for fd, event in events:
            for callback in callbacks[(fd, event)]:
                callback()

注册事件接口
============

.. code-block:: python

    def register_fd(fd, event, callback):
        epoll_ctl(fd, ADD, event)
        callbacks[(fd, event)].append(callback)

    def unregister_fd(fd, event):
        epoll_ctl(fd, DEL, event)
        del callbacks[(fd, event)]

使用
====

.. code-block:: python

    def sendall(fd, msg):
        offset = 0
        def callback():
            count = send(fd, msg[:offset])
            offset += count
            if offset >= len(msg):
                unregister_fd(fd, EV_WRITE)
        register_fd(fd, EV_WRITE, callback)

对比系统线程+阻塞接口
=====================

.. code-block:: python

    def sendall(fd, msg):
        offset = 0
        while offset<len(msg):
            count = send(fd, msg[offset:])
            offset += count

微线程+事件驱动+非阻塞接口
==========================

.. code-block:: python

    def sendall(fd, msg):
        offset = 0
        while offset<len(msg):
            count = send(fd, msg[offset:])
            offset += count

区别在send的实现
================

.. code-block:: python

    def wait_fd(fd, event):
        thread = getcurrent()
        register_fd(fd, event, thread.switch)
        # 主动挂起当前微线程
        # 协作式调度
        hub.switch()    

    def send(fd, msg):
        wait_fd(fd, WRITE)
        return c_send(fd, msg)

线程安全 - 识别何时会切换
=========================

* 抢占式调度：随时可能切换

* 协作式调度：通常是阻塞操作的接口会切换或主动切换

* 事件驱动：不同回调函数之间

线程安全 - 识别何时会切换 - 例子
================================

* executeSQL 切换, async_executeSQL 不切换
* socket.send 切换，socket.async_send 不切换

线程安全 - 示例
===============

.. code-block:: python

    player = players[new_id] = Player()
    value = executeSQL(...)
    player.init(value)

线程安全 - 示例 - 事件驱动
==========================

.. code-block:: python

    def on_success(value):
        player.init(value)
    player = players[new_id] = Player()
    async_executeSQL(..., on_success)
