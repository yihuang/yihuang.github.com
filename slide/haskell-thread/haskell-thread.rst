=================
Haskell微线程实现
=================

:Author: 云悦科技 黄毅
:Email: yi.codeplayer@gmail.com

论文列表
========

[http://www.haskell.org/haskellwiki/Research_papers/Parallelism_and_concurrency]

用户线程与内核线程
==================

* 一对一 (传统线程实现)
* 多对一 (gevent)
* 一对多 (并行计算)
* 多对多 (GHC, GO)

抢占式调度
==========

* 优点: 避免饥饿
* 缺点: 关键区域

调度时机
========

* 在分配内存时

线程同步 MVar a
===============

::

    data MVar a = Empty | Full a

    takeMVar :: MVar a -> IO a
    takeMVar Empty = 阻塞
    takeMVar (Full a) = return a

    putMVar :: MVar a -> a -> IO ()
    putMVar (Full a) = 阻塞
    putMVar Empty    = 写操作

主要数据结构
============

* Thread State Object (TSO)

  * 堆栈和少量其他状态
  * Chunked Stack (默认1K)

    * 自动增长 (生成指令检查堆栈空间)
    * 自动收缩 (GC)

* Haskell Execution Context (HEC) <-> 系统线程

  * 可以运行时增加数量
  * 通常对应一条系统线程
  * 有阻塞外部调用时可能对应多个系统线程

挑战1 - 阻塞的外部调用
======================

挑战1 - 阻塞的外部调用
======================

HEC:

* Ownership field, protected by lock.
* 消息队列
* 处理外部调用的 thread pool

挑战1 - 阻塞的外部调用
======================

* 调用前释放HEC Ownership
* 通知线程池中另一个系统线程，或者创建新系统线程继续调度其他 Haskell 线程。
* 返回时通过消息队列通知当前系统线程，把自己放到等待线程池
* 当前系统线程收到消息，再让位给返回线程

FFI语法 (safe/unsafe)
======================

::

    foreign import ccall safe
        "sys/epoll.h epoll_wait"

    foreign import ccall unsafe
        "sys/eventfd.h eventfd"

实现多播IO 
===========

实现多播IO 调用者
=================

::

    recv :: Handler -> Int -> IO String
    recv fd size = do
        threadWait EventRead fd
        c_recv fd ...
        ...

实现多播IO 调用者
=================

::

    threadWait :: Event -> IO ()
    threadWait evt = do
        m <- newEmptyMVar
        registerFd fd evt $ do
            putMVar m evt
        takeMVar m

实现多播IO 另一种调用者
=======================

::

    recv :: Handler -> Int -> IO String
    recv fd size = do
        ret <- c_recv fd ...
        if ret==WOULDBLOCK then do
            threadWait EventRead fd
            c_recv fd ...
        ...

实现多播IO IO管理器
===================

::

    forever $ do
        events <- poll [socket 和 控制命令的管道]
        处理timer
        调用events对应的回调

挑战2 异步异常
==============

::

    throwTo threadId Exception

* 用处： timeout 100 long_task

挑战2 异步异常
==============

::

    bracket open close process = do
        a <- open   -- 打开资源
        _ <- try (process a) -- 处理，并忽略所有异常
        close a     -- 关闭资源

* 问题：异常可能在 open 和 try 之间抛出

挑战2 异步异常
==============

::

    bracket open close process =
      mask $ \restore -> do
        a <- open
        r <- restore (process a) `onException` close a
        _ <- close a
        return r

挑战2 异步异常
==============

::

    timeout :: Int -> IO a -> IO (Maybe a)
    timeout n io = do
        pid <- myThreadId
        timer <- forkIO $ do
            threadDelay n
            throwTo pid KillThread
        a <- io
        throwTo KillThread timerThread
        return (Just a)

性能
====

[https://gist.github.com/4045809]

* 0.3s 创建10万条线程

  10X faster than gevent

* 10万条线程占用184M内存

  3.2X less memory usage than gevent

论文列表
========

[http://www.haskell.org/haskellwiki/Research_papers/Parallelism_and_concurrency]

Thanks
======
