==============================================
Keep simple things simple and high performance
==============================================

:author: yihuang
:email: yi.codeplayer@gmail.com
:company: 深圳云悦科技

定义简单
========

Redis client API:

.. code-block:: python

    conn.execute('get', 'key')

    # VS

    conn.get('key')

定义简单
========

Redis client pipeline API:

.. code-block:: python

    conn.execute_pipeline(
        ('get', 'key'),
        ('set', 'foo', 'bar')
    )

    # VS

    pipe = conn.pipeline()
    pipe.get('key')
    pipe.set('foo', 'bar')
    pipe.execute()

定义简单
========

Redis client pipeline API:

.. code-block:: python

    cmds = [('get', 'key%d'%i) for i in range(10)]
    conn.execute_pipeline(*cmds)

    # VS

    pipe = conn.pipeline()
    for i in range(10):
        pipe.get('key%d'%i)
    pipe.execute()

定义简单
========

* 更少的接口
* 更简单的实现
* No magic

credis
======

https://github.com/yihuang/credis

更简单的实现
============

Protocol Buffer

.. code-block:: protobuf

    message Test {
        required int32 a = 1;
        optional int32 b = 2;
    }

    Test(10, 10)
    # image to explain encoding of Test message

更简单的实现
============

Protocol Buffer 简单的编码规则

[(index, type, content), ...]

* 向后兼容，向前兼容。

更简单的实现
============

* Protocol Buffer 复杂的官方实现
  ( 排除编译器，12万行c++代码，2万行python代码 )

* cprotobuf, 804行cython代码加185行python代码。

cprotobuf
=========

.. code-block:: python

    class Person(ProtoEntity):
        a = Field('int32', 1)
        b = Field('int32', 2, required=False)

    req = Person()
    req.ParseFromString(s)
    req.SerializeToString()

* 接口命名兼容官方版本

cprotobuf
=========

https://github.com/yihuang/cprotobuf

普通python程序的性能
====================

* 变量获取
* 对象构建
* 属性访问
* 函数调用

Cython作为一门语言
==================

* 融合python和c的语法
* 完全兼容python2和3的语法
  (升级python3不用改代码)

Cython典型用途
==============

* 包装C库
* 加速python代码
* 直接编写cython代码

调用C代码
=========

.. code-block:: cython

    from libc.stdlib cimport atoi

    cdef extern const char* getenv(const char*)

    def getenv(s):
        return atoi(getenv(<const char*>s))

给C传递Python回调
=================

.. code-block:: cython

    from libc.stdlib cimport qsort

    cdef int c_cmp(const void * a, const void * b):
        return (<int*>a)[0] - (<int*>b)[0]

    cdef int* arr = [1,2,3,4,5]
    qsort(arr, 5, sizeof(int), c_cmp)

给变量加类型签名
================

.. code-block:: cython

    def f(double x):
        return x**2-x

使用C的循环
===========

.. code-block:: cython

    cdef int i
    for i in range(10):
        pass

.. code-block:: c

    for(int i=0; i<10; i++)
    {}

memoryview
==========

cython -a
=========

学习Python c-api的好工具。

demo.html

