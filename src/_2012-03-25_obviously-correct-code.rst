==================
编写显然正确的代码
==================

:author: yihuang
:email: yi.codeplayer@gmail.com
:blog: http://yi-programmer.com/
:github: http://github.com/yihuang

History
========

TODO 头像

.. class:: center huge

Can Programming Be Liberated from the von Neumann Style?

.. class:: right

by John Backus 1978

Von Neumann models
==================

.. class:: middle
.. class:: incremental

* **Foundations:** complex, bulky, not useful.

* **History sensitivity:** have storage, history sensitive

* **Semantics:** state transition with complex states.

* **Program clarity:** can be moderately clear, and not very useful conceptually.

The rise of Haskell
=====================

.. class:: middle
.. class:: incremental

* **September 1987.** Initial meeting at FPCA.

* **1 April 1990.**   Version 1.0 Report was published.

* **May 1996.**       Version 1.3 Report with Monadic I/O.

* **February 1999**   Haskell 98 Report was published.

* **July 2010** Haskell 2010 Report was published.

Haskell is lazy
================

.. class:: middle
.. class:: incremental

* **Cons:** good for modularization (参考《why fp》).

* **Cons:** incompatiable with side-effects.

* **Pros:** has runtime overhead.

* **Pros:** hard to predict the space behaviour.

Haskell is lazy
================

模拟追及问题

.. code-block:: haskell

    let a = iterate ((`mod` 360) . (+1)) 0
        -- [0, 1, 2, 3, 4...]
        b = iterate ((`mod` 360) . (+2)) 1
        -- [1, 3, 5, 7, 9...]
        collides = zipWith (==) a b
        -- [False, False, ..., True, ...]
    in  elemIndex True collides
        -- Just 359

Haskell is pure
===============

.. class:: big
.. class:: incremental

* no side-effects.

* **Good** for correctness.

* **Good** for compiler optimization.

* **Good** for parallelization.

Haskell is pure
================

.. class:: center huge
.. code-block:: haskell

    print :: String -> IO ()

.. class:: code-list

* ``IO`` is a type constructor, like generics.

* Type system will prevent ``IO`` appeares in pure code.

* So, ``IO`` allows effects, but not **side-** effects.

Haskell has type classes
=========================

* like interface but better.

* TODO

代码质量
========

.. class:: huge
.. class:: center

  抽象

.. class:: huge
.. class:: center

  健壮

抽象 - 函数组合
===============

``(.)`` 函数管道

.. class:: incremental

.. code-block:: haskell

    (.) :: (b -> c) -> (a -> b) -> a -> c
    (f . g) x = f (g x)
 
.. class:: incremental

::

       /--------------------\       
       |   /---\    /---\   |       
    <<-c---c---b----b---a---a-<<-
       |   \---/    \---/   |       
       \--------------------/       

感受组合的能力
==============

.. class:: incremental
.. class:: code-list

*  .. code-block:: haskell
 
    > ( (==0) . (`mod` 2) ) 4
 
*  .. code-block:: haskell
 
    True

*  .. code-block:: haskell

    > filter ((==0) . (`mod` 2)) [1..10]
  
*  .. code-block:: haskell

    [2, 4, 6, 8, 10]

Case study
==========

来自微博的问题：

 在二维数组里找长度大于5的子数组

 在符合要求的子数组里找所有偶数

 如果数据小于10则乘以2,大于10除以2

 最后统计符合要求的数据的和

Case study
===========

TODO 需要更直观地展示每一步数据转换的过程，以及与自然语言描述的对应。

.. code-block:: haskell

  sum' = sum
         . map (\x -> if x<10 then x*2 else x `div` 2)
         . filter ((==0) . (`mod` 2))
         . concat
         . filter ((>5) . length)

担心性能？
==========

.. class:: hugehuge

::

  ghc -O
      -ddump-simpl
      foo.hs

担心性能？
==========

.. class:: incremental
.. class:: code-list big

* .. code-block:: haskell

    (==0) . (`mod` 2)

* 优化后：

  .. code-block:: haskell

    \x -> case modInt# x 2 of
            0 -> True
            _ -> False

担心性能？
==========

.. class:: incremental
.. class:: code-list big nomargin

* .. code-block:: haskell

      map (\x -> x*x)
    . filter ((==0) . (`mod` 2))

* .. code-block:: haskell

    go xs = case xs of
        []   -> []
        x:xs ->
          case modInt# x 2 of
            0 -> (x*x) : go xs
            _ -> go xs

函数组合 - 继续
===============

.. class:: incremental
.. class:: code-list

* .. code-block:: haskell

    > :t (||)
    Bool -> Bool -> Bool
* .. code-block:: haskell

    > let (||^) = liftA2 (||)
* .. code-block:: haskell

    > :t (||^)
    (a -> Bool) -> (a -> Bool) -> (a -> Bool)
* .. code-block:: haskell

    > filter ( (<3) ||^ (>8) ) [1..10]
* .. code-block:: haskell

    [1,2,9,10]

静态类型系统
============

* 排除错误的程序

* 允许正确的程序
  
* 要精确!

TODO 图表 (正确的程序 与 类型正确的程序 之间的交集)

Case study
==========

``lookup`` 的返回类型应该是什么？

.. class:: huge
.. code-block:: haskell

    lookup :: k -> Map k v
           -> ?

Case study
===========

.. class:: big

``v`` ?

.. class:: huge code-list
.. class:: incremental

* .. code-block:: haskell

    lookup :: k -> Map k v
           -> v

.. class:: code-list
.. class:: incremental

* .. code-block:: haskell

    process :: v -> something

* .. code-block:: haskell

    > process (lookup k empty)

* .. class:: red

  ::

    **crash**

Case study
===========

正确答案： ``Maybe v``

.. class:: huge
.. code-block:: haskell

    lookup :: k -> Map k v
           -> Maybe v

.. class:: code-list
.. class:: incremental

* .. code-block:: haskell

    process (lookup k empty)

* .. class:: red

  ::

    **type error**

What is Maybe
=============

.. class:: center huge
.. code-block:: haskell

  data Maybe a = Just a
                | Nothing

Maybe
=====

现在需要显式处理异常返回，比如提供默认值。

.. class:: code-list big
.. class:: incremental

* .. code-block:: haskell

    fromMaybe :: a -> Maybe a -> a
    fromMaybe _ (Just a) = a
    fromMaybe a Nothing  = a

* .. code-block:: haskell

    > process (fromMaybe 0 
                 (lookup k empty))
    0

抽象 - Monad
============

.. class:: huge center

    什么是Monad

抽象 - 什么是Monad
==================

.. class:: huge center

    Monad是对语句的重载

抽象 - 定义重载
===============

.. class:: huge center

    重载：相同形式，不同含义

.. class:: incremental

``a + b`` 的含义？

.. class:: incremental

``1 + 2`` ? 

.. class:: incremental

``"foo" + "bar"`` ?

抽象 - 定义语句
================

.. class:: huge center

    语句：顺序执行的指令

.. class:: incremental

**顺序：** 必须严格按顺序执行

.. class:: incremental

**执行：** 对执行环境产生副作用

.. class:: incremental

**环境：** 负责执行语句，并维护执行过程中的副作用

Monad - 重载语句
================

IO Monad - 提供普通命令式编程风格

::

    do input <- getLine
       forM_ [1..3] $ \i ->
           printf "echo%d:%s" i input

Monad - 重载语句
================

Parser Monad - 提供解析器的输入并维护中间状态

.. code-block:: haskell

    do t  <- getTagName
       as <- forM ["title", "href"]
               getAttribute
       return (t, as)

Monad - 重载语句
================

Resource Monad - 维护finalizers，并自动在异常发生时调用以释放资源

.. code-block:: haskell

    do f <- openFile "data"
       register (closeFile f)
       process f
       ...

Monad - 重载语句
================

 (list comprehension的另一种形式)

::

    do a <- [1..10]
       b <- [1..10]
       guard $ a+b>10
       return (a, b)

GHC - 工业级Haskell实现
=======================

* 支持Haskell 2010以及大量扩展功能

* 强大的优化能力，能够跨模块优化
  [http://shootout.alioth.debian.org/]

* 完美的并发和并行实现，包括M-N微线程和STM实现

* 跨平台支持 (Windows, Linux, Mac, 有非官方的iOS的支持)

* Profiling支持，包括time/allocation以及多种heap profiling。

其他实现
========

* UHC 有字节码解释器和Javascript后端。

* 其他 [http://www.haskell.org/haskellwiki/Implementations]

Learn Haskell Fast and Hard
===========================

Core Syntax

TODO

Q & A
======
