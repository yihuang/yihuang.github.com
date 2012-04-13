==================
编写显然正确的代码
==================

:author: yihuang
:email: yi.codeplayer@gmail.com
:blog: http://yi-programmer.com/
:github: http://github.com/yihuang

今天不讲啥
==========

.. class:: incremental big

* 编写0-bug软件

* 用自然语言编程

今天讲啥
========

.. class:: incremental big

* 码农代码分享会

* 函数式风格的程序

* Haskell介绍

显然正确的代码
==============

.. class:: center huge

应该贴近自然语言描述

问题1
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

    类型不对

表达： 且
===========================

.. class:: current big
.. code-block:: haskell

    ?

       (a -> Bool)
    -> (a -> Bool)
    -> (a -> Bool)

表达： 且
============================

.. class:: current big
.. code-block:: haskell

    liftA2 (&&)

       (a -> Bool)
    -> (a -> Bool)
    -> (a -> Bool)

表达： 且
===========================

.. class:: current big
.. code-block:: haskell

    (&&&) = liftA2 (&&)

       (a -> Bool)
    -> (a -> Bool)
    -> (a -> Bool)

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

问题2
=====

.. class:: incremental

取http get参数"name"，前面加上"hello"返回回去。

.. class:: incremental
.. code-block:: haskell

  webapp :: Application
  webapp = do
      name <- look "name"
      response ("hello "++name)

.. class:: incremental red

但是，如果用户没有传参数的话。。。

显然正确的代码
==============

.. class:: center huge

要能主动暴露自然语言不严谨之处

.. class:: incremental center big

静态类型系统

函数式编程源起
==============

.. class:: center huge

Can Programming Be Liberated from the von Neumann Style?

.. class:: right

by John Backus 1978

冯诺依曼模型的问题
===================

.. class:: incremental huge center

依赖执行顺序的复杂的状态机模型

.. class:: incremental

* 不容易理解

* 不容易组合

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

* **Pros:** 更强大的组合能力

* **Pros:** 与副作用本质上不兼容

* **Cons:** 存在运行时开销

* **Cons:** 不容易预测内存占用（解决方法：静态分析和heap profile）

举一个简单的例子
=================

在一个400米的环形跑道上

A以每秒一米的速度开跑

.. code-block:: haskell

    a = iterate ((`mod` 400) . (+1)) 0
    -- [0, 1, 2, 3, 4...]

B以每秒两米的速度开跑

.. code-block:: haskell

    b = iterate ((`mod` 400) . (+2)) 1
    -- [1, 3, 5, 7, 9...]

问他们何时相遇？

.. code-block:: haskell

    findIndex (uncurry (==)) (zip a b)
    -- Just 399

Haskell is pure
===============

.. class:: big
.. class:: incremental

* 没有副作用

* 不容易出错

* 编译器可以做大量优化

* 很容易并行化

纯函数是个好抽象
=================

``(.)`` 函数管道

.. class:: incremental

.. code-block:: haskell

    (.) :: (b -> c) -> (a -> b) -> a -> c
    (f . g) x = f (g x)
 
.. class:: incremental

::

       +--------------------+       
       |   +---+    +---+   |       
    <<-c---c---b----b---a---a-<<-
       |   +---+    +---+   |       
       +--------------------+       

感受组合的魅力
==============

.. class:: incremental
.. class:: code-list

*  .. code-block:: haskell
 
    >>> ( (==0) . (`mod` 2) ) 4
 
*  .. code-block:: haskell
 
    True

*  .. code-block:: haskell

    >>> filter ((==0) . (`mod` 2)) [1..10]
  
*  .. code-block:: haskell

    [2, 4, 6, 8, 10]

来自微博的问题
================

在二维数组里找长度大于5的子数组

在符合要求的子数组里找所有偶数

如果数据小于10则乘以2,大于10除以2

最后统计符合要求的数据的和

来自微博的问题
================

.. code-block:: haskell

  sum' = sum
         . map (\x -> if x<10
                        then x*2
                        else x `div` 2)
         . filter ((==0) . (`mod` 2))
         . concat
         . filter ((>5) . length)

抽象能力与性能不一定成反比
==========================

* 内联（跨模块）

* 代码转换

查看中间代码
=============

GHC编译器中间代码是Haskell的子集

.. class:: huge

::

  ghc -O
      -ddump-simpl
      foo.hs

查看中间代码
=============

.. class:: incremental
.. class:: code-list big nomargin

* .. code-block:: haskell

    (==0) . (`mod` 2)

* 优化后：

  .. code-block:: haskell

    \x -> case modInt# x 2 of
            0 -> True
            _ -> False

查看中间代码
=============

.. class:: incremental
.. class:: code-list middle nomargin

* .. code-block:: haskell

      map (*2)
    . filter ((==1) . (`mod` 2))

* .. code-block:: haskell

    go xs = case xs of
        []   -> []
        x:xs ->
          case modInt# x 2 of
            1 -> (x*2) : go xs
            _ -> go xs

静态类型系统
============

.. class:: incremental big

* 排除错误的程序

* 允许正确的程序
  
* 一言以蔽之：精确!

Case study
==========

``lookup`` 应该返回什么类型？

.. class:: huge
.. code-block:: haskell

    lookup :: k -> Map k v
           -> ?

Case study
===========

.. class:: big

``v`` ?

.. class:: huge code-list nomargin
.. class:: incremental

* .. code-block:: haskell

    lookup :: k -> Map k v
           -> v

.. class:: code-list
.. class:: incremental

* .. code-block:: haskell

    process :: v -> something

* .. code-block:: haskell

    >>> process (lookup k empty)

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

Maybe - 显式表达异常分支
========================

.. class:: code-list big
.. class:: incremental

* .. code-block:: haskell

    fromMaybe :: a -> Maybe a -> a
    fromMaybe _ (Just a) = a
    fromMaybe a Nothing  = a

* .. code-block:: haskell

    >>> fromMaybe 0
          (lookup k empty)
    0

Monad 也是个好抽象 
==================

.. class:: huge center

    什么是Monad

什么是Monad
==================

.. class:: huge center

    Monad是对语句的重载

定义重载
===============

.. class:: huge center

    重载：相同形式，不同含义

.. class:: incremental

``a + b`` 的含义？

.. class:: incremental

``1 + 2`` ? 

.. class:: incremental

``"foo" + "bar"`` ?

定义语句
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

List Monad (list comprehension的马甲)

::

    do a <- [1..10]
       b <- [1..10]
       guard $ a+b>10
       return (a, b)

    -- [(1,10), (2,9), (2,10)...]

Monad - 重载语句
================

Parser Monad - 提供解析器的输入并维护中间状态

.. code-block:: haskell

    do t  <- getTagName
       a <- forM ["title", "href"]
                 getAttribute
       return (t, a)

Monad - 重载语句
================

IO Monad - 提供命令式编程风格

::

    do input <- getLine
       forM_ [1..3] $ \i ->
           printf "echo%d:%s" i input

::

    > haskell
    echo1:haskell
    echo2:haskell
    echo3:haskell

Monad - 重载语句
================

Resource Monad - 在 ``IO`` 的基础上提供释放资源的能力。

.. code-block:: haskell

    do f <- openFile "data"
       register (closeFile f)
       process f
       ...

重复一次
========

.. class:: center huge

Monad提供重载命令式语句的语义的能力

GHC - 工业级Haskell实现
=======================

.. class:: incremental

* 支持Haskell 2010以及大量扩展功能

* 强大的优化能力，能够跨模块优化

* 能生成高效的代码，并发程序尤其表现突出
  [http://shootout.alioth.debian.org/]

* 完美的并发和并行实现，包括M-N微线程和STM实现

* 跨平台支持 (Windows, Linux, Mac, 有非官方的iOS的支持)

* Profiling支持，包括time/allocation以及多种heap profiling。

其他实现
========

.. class:: incremental

* UHC 有字节码解释器和Javascript后端。

* 其他 [http://www.haskell.org/haskellwiki/Implementations]

Q & A
======

Learn Haskell Fast and Hard
===========================

* 核心语法 (case let where ADT)

* 语法糖 (pattern match, type class)

* 类型推导
  
* 高阶类型系统扩展

