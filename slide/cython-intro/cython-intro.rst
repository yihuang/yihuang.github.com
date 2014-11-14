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

VS

.. code-block:: python

    conn.get('key')

定义简单
========

.. code-block:: python

    conn.execute_pipeline(
        ('get', 'key'),
        ('set', 'foo', 'bar')
    )

VS

.. code-block:: python

    pipe = conn.pipeline()
    pipe.get('key')
    pipe.set('foo', 'bar')
    pipe.execute()

定义简单
========

.. code-block:: python

    cmds = [('get', 'key%d'%i) for i in range(10)]
    conn.execute_pipeline(*cmds)

VS

.. code-block:: python

    pipe = conn.pipeline()
    for i in range(10):
        pipe.get('key%d'%i)
    pipe.execute()

定义简单
========

* 更少的接口
* 更容易理解
* 更简单的实现
* 更容易维护和优化

.. class:: incremental
    credis (https://github.com/yihuang/credis)

更简单的实现
============

Protocol Buffer

.. code-block:: protobuf

    message Test {
        required int32 a = 1;
        optional int32 b = 2;
    }

    Test(a=10, b=10)

更简单的实现
============

简单的编码规则

.. class:: huge center
.. code-block:: python

    [(index, type, content), ...]

支持向后/向前兼容的协议升级。

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

cprotobuf
=========

https://github.com/yihuang/cprotobuf

下面开始
========

.. class:: huge center

Cython简明教程

Cython典型用途
==============

* 包装C库
* 加速python代码
* 直接编写cython代码

普通python代码的开销
====================

* 变量获取
* 属性访问
* 函数调用
* 对象构建

Cython作为一门语言
==================

* 融合python和c的语法
* 完全兼容python2和3的语法
  (升级python3不用改代码)

三种定义
========

* ``def`` 定义python函数和方法
* ``cdef`` 定义C的函数或其他声明
* ``cpdef`` 同时提供两种接口

调用C代码
=========

.. code-block:: cython

    from libc.stdlib cimport atoi

    cdef extern const char* c_getenv "getenv"(const char*)

    def getenv(s):
        return atoi(c_getenv(<const char*>s))

引入C的枚举
===========

.. code-block:: cython

    cdef extern from "c_maze.h":
        cpdef extern enum eDirection:
            eDirection_Invalid
            eDirection_Up
            eDirection_Right
            eDirection_Down
            eDirection_Left

给C传递Python回调
=================

.. code-block:: cython

    from libc.stdlib cimport qsort

    cdef int c_cmp(const void * a, const void * b):
        return (<int*>a)[0] - (<int*>b)[0]

    cdef int* arr = [1,2,3,4,5]
    qsort(arr, 5, sizeof(int), c_cmp)

封装C结构体
===========

.. code-block:: cython

    cdef class Matrix:
        cdef t_matrix* _matrix
        def __cinit__(self):
            self._matrix = malloc_matrix()

        def __dealloc__(self):
            free_matrix(self._matrix)

        def revert(self):
            revert_matrix(self._matrix)

类型签名加速python代码
======================

.. class:: huge
.. code-block:: cython

    def f(double x):
        return x**2-x

字符串处理
==========

* 支持 ``bytes``, ``unicode``
* ``str`` 编译时确定是 ``bytes`` 还是 ``unicode``

C字符串转换
===========

.. code-block:: cython

    from libc.stdlib cimport malloc

    cdef char* c_str = "hello world"
    cdef bytes s = c_str
    # PyBytes_FromString

    cdef char* c_buf = <char*>malloc(1024)
    cdef bytes buf = c_buf[:1024]
    # PyBytes_FromStringAndSize

C字符串转换
===========

.. code-block:: cython

    cdef bytes s = b"hello world"

    cdef char* c_s = s
    # PyObject_AsString

    cdef Py_ssize_t size = len(s)
    # PyBytes_GET_SIZE

遍历字符串
==========

.. code-block:: cython

    cdef bytes s = b"hello world"
    cdef char c
    for c in s:
        if c == 'A':
            ...

遍历字符串
==========

.. code-block:: c

    char* p = PyBytes_AS_STRING(s)
    int size = PyBytes_GET_SIZE(s)
    char c
    for(char* pp = p; pp<p+size; pp++) {
        c = *pp;
        if (c == 'A')
            ...
    }

编译range
=========

.. code-block:: cython

    cdef int i
    for i in range(10):
        pass

.. class:: incremental
.. code-block:: c

    for(int i=0; i<10; i++)
    {}

释放GIL
=======

.. code-block:: cython

    cdef compute():
        ...
        with nogil:
            纯计算

pxd文件：共享C声明
==================

.. code-block:: cython

    #foo.pxd
    cdef extern from "gl_redirect.h":
        cdef void glActiveTexture(GLenum texture) nogil

    #foo.pyx
    from foo cimport glActiveTexture

pxd文件：共享扩展类
===================

.. code-block:: cython

    #foo.pxd 声明
    cdef class Matrix:
        cdef float data[16]
        cdef revert(self)

    #foo.pyx 实现
    from foo cimport Matrix
    cdef class Matrix:
        cdef revert(self, Matrix b):
            # implementation

pxd文件：共享扩展类
===================

.. code-block:: cython

    #main.pyx 使用
    from foo cimport Matrix
    m = Matrix()

Typed Memoryviews
=================

.. code-block:: cython

    cdef fill_buffer(unsigned char[:] buf):
        c_fill(&buf[0], buf.shape[0])

    fill_buffer( bytes | bytearray | numpy array )

Using Cython Declarations from C
================================

.. code-block:: cython

    #foo.pyx
    cdef public struct Bunny:
        int vorpalness

    cdef public int spam

    cdef public void grail():
        print "Ready the holy hand grenade"

Using Cython Declarations from C
================================

.. code-block:: c

    #foo.h
    struct Bunny {
      int vorpalness;
    };

    __PYX_EXTERN_C DL_IMPORT(void) grail(void);
    __PYX_EXTERN_C DL_IMPORT(int) spam;

其他特性
========

* yield from
* OpenMP并行
* numpy
* c++

Killer App: cython -a
=====================

.. code-block:: bash

    cython -a demo.pyx

* `demo.html <demo.html>`_
* `cprotobuf.internal.html <cprotobuf.internal.html>`_
* `cprotobuf.utils.html <cprotobuf.utils.html>`_
* `credis.base.html <credis.base.html>`_

调试
====

* gdb
* cygdb
