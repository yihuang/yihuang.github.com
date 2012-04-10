==================
编写显然正确的代码
==================

:author: yihuang

显然正确的代码
==============

.. class:: center huge

应该贴近自然语言描述

示例1
=====

.. class:: center huge

从列表取大于10且小于100的数

表达： 从列表取 ? 的数
===========================

.. class:: incremental big
.. code-block:: haskell

    λ x -> filter ? x

.. class:: incremental

  不如直接点：

  .. class:: big
  .. code-block:: haskell
  
      filter ?

表达： 大于10
===========================

.. class:: incremental big
.. code-block:: haskell

    λ x -> x > 10

.. class:: incremental

  不如直接点：

  .. class:: big
  .. code-block:: haskell

      (>10)

表达： 小于100
===============


.. class:: incremental

  同样：
  
  .. class:: big
  .. code-block:: haskell
  
      (<100)

表达： 且
===========================

.. class:: incremental big
.. code-block:: haskell

    &&

.. class:: incremental big
.. code-block:: haskell

    :: Bool -> Bool

.. class:: incremental
.. class:: red

    类型不匹配

表达： 且
===========================

.. class:: current big
.. code-block:: haskell

    ?

    (a -> Bool) -> (a -> Bool) -> (a -> Bool)

表达： 且
============================

.. class:: current big
.. code-block:: haskell

    liftA2 (&&)

    (a -> Bool) -> (a -> Bool) -> (a -> Bool)

表达： 且
===========================

.. class:: current big
.. code-block:: haskell

    (&&&) = liftA2 (&&)

拼在一块：
============================

.. class:: incremental big
.. code-block:: haskell

    filter ( (>10) &&& (<100) )

.. class:: incremental
.. code-block:: haskell

    >>> let foo = filter ( (>10) &&& (<100) )
    >>> foo [1..20]
    [11, 12, 13 ... ]
