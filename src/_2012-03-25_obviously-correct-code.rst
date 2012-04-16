==================
编写显然正确的代码
==================

:author: 黄毅 众禄基金程序员
:email: yi.codeplayer@gmail.com
:blog: http://yi-programmer.com/
:github: http://github.com/yihuang

今天分享啥
==========

.. class:: big

* 码农的代码分享会

* 函数式编程风格 和 静态类型系统

* Haskell介绍

Haskell速成 - 函数定义
============================

.. class:: big
.. raw:: html

  <div class="highlight haskell-quick"><pre><span class="nf function-name">filter</span> <span class="ow">::</span> <span class="p">(</span><span class="n">a</span><span class="ow">-&gt;</span><span class="kt">Bool</span><span class="p">)</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="n">a</span><span class="p">]</span> <span class="ow">-&gt;</span> <span class="p">[</span><span class="n">a</span><span class="p">]</span>
  <span class="nf">filter</span> <span class="n">p</span> <span class="kt">[]</span> <span class="ow">=</span> <span class="kt">[]</span>
  <span class="nf">filter</span> <span class="n">p</span> <span class="p">(</span><span class="n">x</span><span class="kt">:</span><span class="n">xs</span><span class="p">)</span>
       <span class="o">|</span> <span class="n">p</span> <span class="n">x</span>       <span class="ow">=</span> <span class="n">x</span> <span class="kt">:</span> <span class="n">filter</span> <span class="n">p</span> <span class="n">xs</span>
       <span class="o">|</span> <span class="n">otherwise</span> <span class="ow">=</span> <span class="n">filter</span> <span class="n">p</span> <span class="n">xs</span>
  </pre></div>
  <script>
  desc('.haskell-quick .function-name', '函数名')
  </script>

.. class:: handout

    这是一个函数定义，第一行是类型签名，冒号前面是函数名，后面是函数的类型，参数和返回值的类型统一由箭头组合在一起，最后一个是返回值，前面都是参数。这种语法使得curry化非常方便，这一点我们后面会讲到。

    后面几行呢就是函数的定义了，这里比较有意思的地方就是模式匹配了，模式匹配这个东西从执行的角度来讲它就是一种分支的方法，但它是一种更受限的分支方法，它只能针对一个类型的不同构造器进行分支，这个约束使得它具备一个很好的特性，那就是编译器可以自动检查代码是否把所有分支都覆盖全面了，如果遗漏了哪个分支，它会出一个警告，这一点对于编写正确的代码来说太有用了。

Haskell速成 - Curry化
======================

.. class:: big
.. code-block:: haskell

    add :: Int -> Int -> Int
    (add 1)    :: Int -> Int

    >>> let inc = add 1
    >>> inc 2
    3

.. class:: handout

    Curry化又叫部分函数调用，也就是一个函数本来接受两个参数，返回一个值的，你现在只给它传一个参数，你就得到了一个只接受一个参数的函数了。通过后面的代码我们会看到，这个特性对于函数式编程风格来说非常重要，它可以大大提高代码重用性，一个函数可以当几个函数用。

Haskell速成 - 前缀/中缀表示法
==============================

.. class:: big
.. code-block:: haskell

    >>> 1 + 2
    3
    >>> (+) 1 2
    3
    >>> add 1 2
    3
    >>> 1 `add` 2
    3

.. class:: handout

    Haskell里操作符和普通函数没太大区别，唯一的区别就是操作符由特殊符号组成，而普通函数名由标示符组成。

    而不管操作符还是普通函数，都可以写成前缀形式，也可以写成中缀形式，这几句代码都是等价的。

Haskell速成 - 前缀/中缀表示法
==============================

.. class:: big

  .. code-block:: haskell
 
      1 `add` 2 `add` 3 `add` 4
 
  VS

  .. code-block:: haskell

      add (add (add 1 2) 3) 4

.. class:: handout

    中缀形式在嵌套的时候特别给力，比如这个例子。其实haskell代码也可以写成lisp风格的。

Haskell速成 - lambda
=====================

.. class:: big
.. code-block:: haskell

    \a b -> a + b

.. class:: handout

    这个lambda语法有够简单了，一条斜杠定义lambda函数的开始，后面空格分隔的是形参，箭头后面就是函数定义。

Haskell速成 - 结束
===================

.. class:: center huge

恭喜你，你已经学会了Haskell 50% 常用语法

显然正确的代码
==============

.. class:: center huge

一、贴近自然语言描述

.. class:: center

如何让代码更直接地表达你的想法

.. class:: handout

    现在正式切入本次分享的题目

    显然正确的代码，这是个很虚词语，其实我想说的就是代码质量，
    代码质量也还是很虚，世界上有这么多编程风格，每一种都有它独到的地方，
    到底什么样的代码是好的代码，很难有一个统一的标准。
    那今天既然是我给大家分享，那就只好先用我的标准啦，贴近自然语言，大家要是对这个有意见，我们再交流。

    OK，我们就不纠结这个问题了，直接看代码，大家就会明白我要表达的是啥意思啦。

问题1
=====

.. class:: center huge

从列表取大于10且小于100的数

.. class:: incremental center huge
.. code-block:: haskell

  filter ( (>10) `and` (<100) )

.. class:: handout

    这个例子够简单了，不过我想也没有太多语言能想这个代码这样和问题描述如此贴近吧。
    下面我们就把它拆开来，它是由哪些部分拼起来的。

分解： 从列表取 ? 的数
===========================

.. class:: incremental big
.. code-block:: haskell

    \x -> filter ? x

.. class:: incremental

  不如直接点：

  .. class:: big
  .. code-block:: haskell

      filter ?

.. class:: handout

    首先，我们先考虑这个大的框架，就是从列表取符合某个条件的数，一个lambda函数就可以搞定，
    这个很普通，但是按照我们上面介绍的curry特性，我们可以更进一步，写成这种形式，这两个表达式是等价的。
    Curry特性省了我们很多代码。

分解： 大于10
===========================

.. class:: incremental big
.. code-block:: haskell

    \x -> x > 10

.. class:: incremental

  不如直接点：

  .. class:: big
  .. code-block:: haskell

      (>10)

.. class:: handout

    然后我们来考虑具体过滤条件，大于10，也很简单，一个lambda函数搞定，但我们可以再一次应用我们的curry特性，
    把它写成等价形式，是不是更直接？
    你可以看作是从 (x>10) 里面把x拿掉，就产生了一个这样函数，当你给它传一个参数，它就把那个x的空给补上。

分解： 小于100
===============

.. class:: incremental

  同样：

  .. class:: big
  .. code-block:: haskell

      (<100)

.. class:: handout

    这个就没什么悬念了

分解： 且
===========================

.. class:: incremental big
.. code-block:: haskell

    &&

.. class:: incremental big
.. code-block:: haskell

    :: Bool -> Bool -> Bool

.. class:: incremental
.. class:: red

    类型不对

.. class:: handout

    最后，我们还剩下一个 且 ，我们知道and操作符，接受两个bool值返回他们的且，但很遗憾在这里类型不匹配

分解： 且
===========================

.. class:: current big
.. code-block:: haskell

    ?

    :: (a -> Bool)
    -> (a -> Bool)
    -> (a -> Bool)

.. class:: handout

    因为我们需要组合的是两个判断函数，而不是简单的布尔值。

分解： 且
============================

.. class:: current big
.. code-block:: haskell

    and f g = \x -> f x && g x

    :: (a -> Bool)
    -> (a -> Bool)
    -> (a -> Bool)

.. class:: handout

    我们当然可以再一次专门定义一个函数来解决这个问题
    这样我们的问题貌似就全部解决了。

分解： 且
============================

.. class:: current big
.. code-block:: haskell

    $ lambdabot
    >>> :pl \f g x -> f x && g x
    liftA2 (&&)

.. class:: handout

    但实际上， and 函数甚至也有一个更直接的实现，
    haskell有意思的地方之一就是它有很多有意思的工具，比如说这个lambdabot，
    里面这个 pl 命令可以把lambda表达式转换成函数组合的风格，
    比如刚才这个and函数的定义就被转换成了一个 liftA2 的调用，
    也就是说，and函数实际上是 liftA2 把 && 函数提升一下的结果！
    至于liftA2函数就不在今天的范畴了，大家有兴趣可以去了解一下 Applicative。

分解： 且
============================

.. class:: current big
.. code-block:: haskell

    and = liftA2 (&&)

    :: (a -> Bool)
    -> (a -> Bool)
    -> (a -> Bool)

合并
====

.. class:: center huge
.. code-block:: haskell

  filter ( (>10) `and` (<100) )

函数管道 (.)
=================

.. class:: big
.. code-block:: haskell

    (.) :: (b -> c)
        -> (a -> b)
        -> (a -> c)
    (f . g) x = f (g x)
 
::

       +--------------------+       
       |   +---+    +---+   |       
    <<-c---c---b----b---a---a-<<-
       |   +---+    +---+   |       
       +--------------------+       

.. class:: handout

    在看下一个例子之前，我先介绍一下这个函数，这个组合函数类似unix管道，
    它把两个函数组合在一起，当你向它传参数的时候，它先把参数传给右边的函数，
    再把右边函数的返回值传给左边函数。
    加上前面介绍过的中缀语法形式，它可以把一对函数连在一起，非常节省代码。

问题2
===================

在二维数组里找长度大于5的子数组

在符合要求的子数组里找所有偶数

如果数据小于10则乘以2,大于10除以2

最后统计符合要求的数据的和

.. class:: handout

    我们来看这个例子，这是微博上一个朋友发的题目。其实传统命令式风格的程序，
    写几个循环，弄几个中间数组中间变量，也可以搞定这个问题。
    我们看看haskell函数式程序如何解决这个问题

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

.. class:: handout

    这个程序的含义我们要从下往上看，基本上和描述语言是一一对应的。
    最下面是取长度大于5的子数组，然后concat是把二维数组拼成一维，
    然后过滤出偶数，然后用map遍历一次，最后sum求和。

抽象与性能不是死敌
===================

.. class:: big

GHC 编译器优化

.. class:: big

* 内联（跨模块）

* 等价代码转换

.. class:: handout

    看到这么多函数式程序，我想很多同学都跟我一样想，这么多小函数套小函数，
    性能一定很差吧，确实对于很多动态语言来说，函数调用就是很大一部分开销。
    不过haskell通过编译器进行代码优化，可以同时获得代码的抽象能力以及很好的性能。
    最主要的手段就是内联，和等价代码转换，而且内联还可以跨模块，这个还是很牛逼的。

查看中间代码
=============

.. class:: huge

::

  ghc -O
      -ddump-simpl
      foo.hs

GHC编译器中间代码是Haskell的子集

.. class:: handout

    GHC编译器中间代码用的也是Haskell的一个子集，而且还是带类型的，这个很有意思，
    对于GHC的开发者来说，这意味着他们可以比较放心地对代码进行转换，
    因为它可以对中间代码进行类型检查，类型检查可以保证代码转换基本上不会出太大问题。
    还有一个好处就是，我们可以很方便地查看编译器优化后的代码，因为它还是haskell的语法。
    这个命令就是用来导出中间代码的。下面我们用这个命令看几个例子。

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

.. class:: handout

    可以看到这两个小函数的组合经过内联和转换变成一个简单的判断语句了。

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

.. class:: handout

    而这个更复杂一些的例子，也被编译成一个平坦的递归，没有小函数，没有生成中间列表。

    可以说，也正是因为编译器有这个能力做这些优化，也才能使得这种编程风格变得实用。
    否则如果按照python对函数的实现，那真的是不太敢写这样的代码。

边界条件
========

取http get参数"name"，前面加上"hello"返回回去。

.. code-block:: haskell

  webapp :: Application
  webapp req = do
      let name = lookup "name" (queryString req)
      response ("hello "++name)

.. class:: incremental red

但是，如果用户没有传参数的话。。。

.. class:: handout

    我们看这个简单的web应用，它从querystring里面取一个name参数，加上hello后返回回去。
    代码看起来也非常简单，和我们的问题描述很接近，但是，如果用户没有传参数过来的话，
    就要崩溃了。实际上类似这样的问题，至少在我的python代码里面，经常碰到。

显然正确的代码
==============

.. class:: center huge

二、要能主动暴露自然语言不严谨之处

.. class:: incremental huge center

解决方案：静态类型系统

.. class:: handout

    这就引出我想分享的第二点内容，代码光能贴近自然语言是不够的，因为自然语言并不精确，
    要少出bug，我们的代码需要更严谨一些，如何做到严谨，我们需要强大的静态类型系统。
    我们先来看看在haskell里面我们如何处理这个问题。

问题2 - 继续
============

.. class:: huge
.. code-block:: haskell

    lookup :: k -> Map k v
           -> ?

.. class:: big current

``lookup`` 应该返回什么类型？

.. class:: handout

    大家看这个lookup函数，它的作用是从map中根据key查找value的，大家觉得它应该返回什么类型？
    这里k代表key，v代表value

问题2 - 继续
=============

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

.. class:: handout

    是返回 v 吗？实际上很多语言都是这么设计的，但是这正式造成上面我们崩溃的原因。
    因为当我们把lookup的返回值传给其他函数进行处理的时候，从类型上看没有任何问题，但运行时却崩溃了。

问题2 - 继续
=============

答案： ``Maybe v``

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

.. class:: handout

    在 Haskell 里面，它的返回值叫做 Maybe v ，有了它，这个代码就变成了一个静态的类型错误，
    而不是运行时错误。那Maybe类型是个什么东西呢

Maybe - 显式表达异常情况
=========================

.. class:: center huge
.. code-block:: haskell

  data Maybe a = Just a
                | Nothing

.. class:: handout

    从名字上来看，Maybe就是用来表达一个值可能存在也可能不存在的情况，存在的话就是 Just a，
    不存在的话就是 Nothing。

    准确地说，Maybe是一个Haskell里面一个自定义数据类型，里面的小写字母 a 是个类型变量，它可以是任何类型。
    如果要类比的话，可以把Maybe看做是个泛型。
    大家可能还会联想到其他语言的比如python的none对象，
    Maybe其实就是一个显式表达出来的none，显式表达的好处就是，代码而不会一不小心忽略对它的处理，因为你的类型会不匹配。

类型系统的终极目标
==================

.. class:: big

* 排除所有错误的程序

* 允许所有正确的程序

* 一言以蔽之：精确!

.. class:: handout

    对于静态类型系统的设计者来说，终极的目标就是要能排除所有错误的程序，也就是说把所有运行时错误变成类型错误，提前捕获，允许所有正确的程序，就是说类型系统不能挡我们的路，对于我们想要表达的程序，我们知道它是正确的，类型系统不能成为我们的绊脚石，很多时候我们喜欢动态语言的原因也就是这个，虽然他们不能帮我们发现问题，但至少它不挡我的路，我可以比较随心所欲的写我的程序。

Haskell类型系统作用
=====================

.. class:: big

区分纯函数式代码和命令式代码

.. class:: big
.. code-block:: haskell

    upper :: String -> String

    bomb  :: String -> IO String

.. class:: handout

    刚才说的是个比较完美的境界了，按照这个目标的话，我想haskell的类型系统还差很远，
    但是已经可以帮我们作很多事情了，比如区分纯函数式代码和命令式代码，
    比如通过签名我们就能知道upper只能是个字符串转换函数，它不会修改全局变量，不会写文件，
    除了把输入字符串变成输出字符串它不会干别的，而 readFile 的返回值是 IO String，
    意味着它可以作任何事情，比如发射个导弹啥的。

Haskell类型系统作用
=====================

.. class:: big

精确的文档

.. class:: big
.. code-block:: haskell

    readChan :: Chan a -> IO a

这个函数会阻塞吗？

.. class:: handout

    把类型变得更精确的另一个好处就是，类型签名本身可以提供更多的信息，
    比如这个函数，从签名可以看出，它应该是从一个channel读一个数据出来。
    再多想一步，其实我们从类型就可以看出它会不会阻塞。

    我们可以想象一下，假设它不阻塞，那如果这个channel是空的，它得返回什么呢？
    所以阻塞接口会返回 a，而不阻塞的接口应该返回 Maybe a

Haskell类型系统作用
=====================

.. class:: big

精确的文档

.. class:: big
.. code-block:: haskell

    tryReadChan :: Chan a -> IO (Maybe a)

这个呢？

Haskell is lazy
================

在一个400米的环形跑道上

A以每秒一米的速度开跑

B以每秒两米的速度开跑

问他们何时相遇？

.. class:: handout

    最后再给一个例子，让我们看看惰性求值能够如何帮助我们以更直接的方式编写程序。

Haskell is lazy
================

.. class:: big
.. code-block:: haskell

    iterate :: (a -> a) -> a -> [a]
    iterate f a = [a, f a, f f a, f f f a ...]

.. code-block:: haskell

    >>> iterate (+1) 0
    [0,1,2,3,4,...]

.. class:: handout

    在给出程序之前，先介绍一个迭代函数，给它传一个函数和一个初始值，
    它会对这个值不断应用这个函数，并把每一次应用生成一个无限列表。

Haskell is lazy
================

.. code-block:: haskell

  a = iterate ((`mod` 400) . (+1)) 0
  -- [0, 1, 2, 3, 4...]

  b = iterate ((`mod` 400) . (+2)) 0
  -- [0, 2, 4, 8, 10...]

  findIndex (uncurry (==)) (tail (zip a b))
  -- Just 399

.. class:: handout

    我们可以用这个迭代函数来模拟这个跑步的过程，把它每一秒的位置生成一个无穷列表，
    每一秒位置+1再摸上400，因为是个环形跑道，然后把a和b的数据用zip一一对应起来，
    用tail去掉第一个元素，然后找到第一个相等的索引，也就是他们相遇的时间了。

Lazy I/O
=========

.. class:: big
.. code-block:: haskell

    main = do
        s <- Lazy.readFile input
        Lazy.writeFile output s

.. class:: big

消耗常数内存

.. class:: handout

    惰性求值除了能让我们以一种全新的结构编写程序，对于一些I/O问题也有奇效，
    比如这个程序，它把输入文件的内容写到输出文件中去，最有意思的是它只消耗常数内存，
    也就是说它运行时是流式处理的，读一块数据写一块数据，原因就在于 readFile 返回的是个
    惰性求值的字符串，它只在被求值的时候才去读内容。

    不过 Lazy I/O 只适合这种命令行工具的场景，运行完就退出了，不太适合编写持久运行的server，
    因为它很难控制句柄的生命周期，当然对于server的场景有其他库来进行流式数据处理，我们今天就不聊这个了。

Q & A
======

Monad！
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

