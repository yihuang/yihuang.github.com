===============
Python 代码优化
===============

:author: yihuang
:email: yi.codeplayer@gmail.com
:company: 深圳云悦科技

今天不探讨
==========

.. class:: incremental

* IO
  
  请先确定瓶颈在Python代码

* pypy
  
  准备用pypy的话，今天说的完全不适用

大纲
====

#. **性能分析工具(快速)**
#. CPython的性能
#. Cython简明教程

评测工具: timeit
=================

用于：

.. class:: incremental

* 对比不同实现
* 明确优化效果

* .. code-block:: python

    import timeit
    print timeit.timeit('test()',
        'from __main__ import test', number=10000)

profile: cProfile
=================

.. code-block:: python

    import cProfile
    rng = range(10000)
    cProfile.run('for i in rng:test()', sort='time')

一起用
=======

::

   timeit[10000]: 0.519935846329

         290002 function calls in 0.901 seconds
   Ordered by: internal time

   ncalls  tottime  percall filename:lineno(function)
    10000    0.199    0.000 base.pyx:196(load)
    10000    0.158    0.000 rpc.pyx:184(__call__)
    10000    0.088    0.000 base.pyx:90(decode)
    10000    0.083    0.000 rpc.pyx:49(wrapper)
    10000    0.076    0.000 base.pyx:81(_hash)
    ...

Mockup
======

.. class:: incremental

* 排除IO的影响

* patch_socket.py (http://tinyurl.com/pb3joac)

* .. code-block:: python

    from patch_socket import run_with_recording

    ...

    run_with_recording(_sock, test)
    _sock.start_replay()
    cProfile.run('test()', sort='time')

内存泄漏[1]
===========

.. class:: incremental

* 创建heap快照 ``gc.get_objects()``

* .. code-block:: python

    stats = defaultdict(int)
    for o in gc.get_objects():
        stats[str(type(o))] += 1

* 对比heap快照

::

    list: 100
    tuple: -40
    <class '__main__.Test'>: 1

内存泄漏[2]
===========

* CPython存在小对象缓存 和 内存碎片

.. class:: incremental

* live with it.

大纲
====

* 性能分析工具(快速)
* **CPython的性能**
* Cython简明教程

使用正确的数据结构[1/2]
=======================

.. class:: incremental

* ``list``. 连续，不要在中间增删数据！
* ``tuple``. immutable, 比 ``list`` 稍快且省内存
* ``dict/defaultdict``. 哈希表
* ``set``. 去重
* ``bytearray``. 可变的字符串缓冲区
* ``deque``. 双端链表，可两头操作。
* ``heap``. 最小堆，实现timer。

使用正确的数据结构[2/2]
=======================

.. class:: incremental

* ``namedtuple``. 不可变对象，比对象省点内存。
* ``OrderedDict`` (dict+linked list). 费内存，需要就用。

小对象缓存和freelist
====================

.. class:: incremental

* [-5, 257) 之间的整数对象。
* 空字符串和单字符串。
* 长度20以内的 ``tuple`` ，每个长度最多存2000个对象。
* (所以大部分 ``tuple`` 对象的创建都很便宜)
* 最多80个 ``list`` 对象，但 ``list`` 额外还有动态内存分配。
* 最多80个 ``dict`` 对象，但 ``dict`` 额外还有动态内存分配。

预先计算[1]
===========

.. class:: incremental

* **BAD**

  .. code-block:: python

      for i in range(10):
          if i in ('test1', 'test2', 'test3'):
              pass

* **GOOD**

  .. code-block:: python

      t = ('test1', 'test2', 'test3')
      for i in range(10):
          if i in t:
              pass

预先计算[2]
===========

其他预先计算时机：

* 模块导入时
* class创建时 (metaclass)

name resolution[1]
==================

.. class:: incremental

* 局部变量

  .. code-block:: python

      def test(a):
          a
  
  .. code-block:: python

      LOAD_FAST 0

name resolution[2]
==================

``LOAD_FAST i``

  .. code-block:: c

    PyObject *PyEval_EvalCodeEx(...) {
        register PyObject **fastlocals;
        ...
        fastlocals = f->f_localsplus;
        ...
        fastlocals[i]
        ..*

name resolution[3]
==================

* 模块变量

  .. code-block:: python

      a = 1
      def test():
          a

  .. code-block:: python

      LOAD_GLOBAL 0

name resolution[4]
==================

``LOAD_GLOBAL 0``

  .. class:: small
  .. code-block:: c

    PyObject *PyEval_EvalCodeEx(...) {
        PyObject *names;
        ...
        names = co->co_names;
        ...
        w = PyTuple_GetItem(names, i);
        x = PyDict_GetItem(f->f_globals, w);
        if (x == NULL) {
            x = PyDict_GetItem(f->f_builtins, w);
            if (x == NULL) {
              load_global_error:
        ..*

name resolution[5] 优化示例
===========================

* .. code-block:: python

    def encode(s):
        b = 0
        for c in s:
            b |= ord(c)

.. class:: incremental

* .. code-block:: python

    def encode(s):
        b = 0
        _ord = ord
        for c in s:
            b |= _ord(c)

function call[1]
================

.. code-block:: python

    test(1, 2, 3, a=1, b=2)

.. class:: incremental

.. code-block:: c

    PyObject *func = LOAD_NAME 'test';
    PyObject *args = PyTuple_New(3);
    PyTuple_SET_ITEM(args, 0, 1);
    PyTuple_SET_ITEM(args, 1, 2);
    PyTuple_SET_ITEM(args, 2, 3);
    PyObject *kwargs = PyDict_New();
    PyDict_SetItem(kwargs, "a", 1);
    PyDict_SetItem(kwargs, "b", 2);
    PyObject_Call(func, args, kwargs);
    ..*

function call[2]
================

优化方法：

.. class:: incremental

* 尽量使用内置函数 ``map``,``filter`` 等替代循环函数调用。

* 还是无法忍受，没办法，只能改成c了。

object model
============

对象的消耗：

.. class:: incremental

.. code-block:: python

    object PyObject_GenericGetAttr(object obj, object name):
        # 从class中查找descriptor
        descr = PyType_Lookup(Py_TYPE(obj), name)
        if PyDescr_IsData(descr):
            # 如果是data descriptor，直接使用
            return descr.__get__(descr, obj, obj->obj_type)
        else:
            # 否则使用对象字典
            r = obj.__dict__[name]
            if r is not None:
                return r
            elif descr is not None:
                # 最后使用 Non-data descriptor
                return descr.__get__(...)

延迟计算 - Non-data descriptors
===============================

.. class::incremental

.. code-block:: python

    class LazyUser(object):
        def __get__(self, obj, objtype=None):
            value = self.loader(obj, objtype)
            # 使用对象字典作为缓存
            obj.user = value
            return value

.. code-block:: python

    >>> req.user
    计算...
    >>> req.user
    从字典中取值

简化设计
========

.. class:: incremental

* KISS, KISS, KISS

* 没什么好说的

* 就像

大纲
====

* 性能分析工具(快速)
* CPython的性能
* **Cython简明教程**

啥是Cython
==========

.. class:: incremental

* Python到c的编译器
* 完全兼容python2/3的语法
* 提供扩展语法用于对接c

编译纯Python的好处
==================

.. class:: incremental

* 没有解释执行的开销

* .. code-block:: python

    def test(a, b):
        return a + b

* .. code-block:: c

    PyObject *test(PyObject *args) {
        PyObject *a = PyTuple_GET_ITEM(args, 0);
        PyObject *b = PyTuple_GET_ITEM(args, 1);
        return PyNumber_Add(a, b);
    }

给Python加入类型签名
====================

.. class:: incremental

* .. code-block:: python

    def test(int a, int b):
        return a + b

* .. code-block:: c

    PyObject *test(PyObject *args) {
        PyObject *pya = PyTuple_GET_ITEM(args, 0);
        PyObject *pyb = PyTuple_GET_ITEM(args, 1);
        int a = __Pyx_PyInt_AsInt(pya);
        int b = __Pyx_PyInt_AsInt(pyb);
        return PyInt_FromLong(a + b);
    }

cdef Early binding
==================

cdef 

cdef Method
===========
