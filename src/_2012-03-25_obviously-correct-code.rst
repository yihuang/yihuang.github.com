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

Can Programming Be Liberated from the von Neumann Style?

	by John Backus 1978


Von Neumann models
==================

* **Foundations:** complex, bulky, not useful.

* **History sensitivity:** have storage, history sensitive

* **Semantics:** state transition with complex states.

* **Program clarity:** can be moderately clear, and not very useful conceptually.

The rise of Haskell
=====================

* **September 1987.** Initial meeting at FPCA.

* **1 April 1990.** Version 1.0 Report was published.

* **May 1996.** Version 1.3 Report with Monadic I/O.

* **February 1999** Haskell 98 Report was published.

* **July 2010** Haskell 2010 Report was published.

Haskell is lazy
================

* non-strict semantics and lazy evaluation.

* good for modularization (参考《why fp》).

* incompatiable with side-effects.

* pros: has runtime overhead.

* pros: hard to predict the space behaviour.

Haskell is lazy
================

模拟追及问题

::

    let a = iterate ((`mod` 360) . (+1)) 0
        -- [0, 1, 2, 3, 4...]
        b = iterate ((`mod` 360) . (+2)) 1
        -- [1, 3, 5, 7, 9...]
        collides = zipWith (==) a b
        -- [False, False, ..., True, ...]
    in  elemIndex True collides
        -- Just 359

Haskell is pure
================

* good for correctness.

* good for compiler optimization.

* good for parallelization.

Haskell has type classes
=========================

TODO

代码质量
========

* 抽象
* 健壮

抽象 - 函数组合
===============

* `(.)` 函数管道

  ::
  
    (.) :: (b -> c) -> (a -> b) -> a -> c
    (f . g) x = f (g x)
  
  ::
  
       /--------------------\       
       |   /---\    /---\   |       
    <<-c---c---b----b---a---a-<<-
       |   \---/    \---/   |       
       \--------------------/       

感受组合的能力
==============

::

  > ( (==0) . (`mod` 2) ) 4
  True
  > filter ((==0) . (`mod` 2)) [1..10]
  [2,4,6,8,10]

Case study
==========

来自微博的问题：

 找出一个锯齿数组里长度大于5的子数组
 在符合要求的子数组里的数据里找出所有偶数
 如果数据小于10的话乘以2,大于10的除以2
 最后统计符合要求的数据的和

Case study
===========

TODO 需要更直观地展示每一步数据转换的过程，以及与自然语言描述的对应。

::

  sum' = sum
         . map (\x -> if x<10 then x*2 else x `div` 2)
         . filter ((==0) . (`mod` 2))
         . concat
         . filter ((>5) . length)

担心性能？
==========

::

    ghc -O -ddump-simpl foo.hs

担心性能？
==========

::

    (==0) . (`mod` 2)

优化后 ::

    \x -> case modInt#  x 2 of
            0 -> True
            _ -> False

担心性能？
==========

::

      map (\x -> x*x)
    . filter ((==0) . (`mod` 2))

::

    go xs = case xs of
        []   -> []
        x:xs ->
          case modInt# x 2 of
            0 -> (x*x) : go xs
            _ -> go xs

函数组合 - 继续
===============

::

  > :t (||)
  Bool -> Bool -> Bool
  > let (||^) = liftA2 (||)
  > :t (||^)
  (a -> Bool) -> (a -> Bool) -> (a -> Bool)
  > filter ((<3) ||^ (>8)) [1..10]
  [1,2,9,10]

静态类型系统
============

* 能排除错误的程序，同时允许正确的程序的表达，精确性。

TODO 图表 (正确的程序 与 类型正确的程序 之间的交集)

Case study - lookup
===================

::

    lookup :: k -> Map k v -> ?

假想
====

::

    lookup :: k -> Map k v -> v

    process :: v -> something

    > process (lookup k m)
    **crash**

Case study - lookup
===================

::

    lookup :: k -> Map k v -> Maybe v

Maybe - 总有些事情是我们没有把握的
==================================

::

  data Maybe a = Just a | Nothing

Maybe - 总有些事情是我们没有把握的
==================================

::

    process :: a -> something

    > process (lookup k m)
    **type error**

Maybe - 总有些事情是我们没有把握的
==================================

::

    fromMaybe :: a -> Maybe a -> a
    fromMaybe _ (Just a) = a
    fromMaybe a Nothing  = a

    > process (fromMaybe 0 (lookup k m))
    **typing ok**

抽象之Monad
============

* 什么是Monad

* 隐喻：Monad是重载

* 重载：相同形式，不同含义

* ``a+b`` 的含义？ ``1+2`` 还是 ``"foo"+"bar"``

重载命令式语句
==============

语句 vs 表达式

Monad重载的命令式语句的含义
===========================

List Monad (list comprehension的另一种形式)

::

    do a <- [1..10]
       b <- [1..10]
       guard $ a+b>10
       return (a, b)

Monad重载的命令式语句的含义
===========================

State Monad

::

    do 
        TODO

Monad重载的命令式语句的含义
===========================

Coroutine Monad

::

    do TODO

Monad重载的命令式语句的含义
===========================

IO Monad

::

    do name <- readInput
       printf "hello %s" name

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

Q & A
======
