===============
Haskell for web
===============

:author: yi.codeplayer@gmail.com

Greeting
=========

* 专业Python程序员
* 业余Haskell程序员

Why haskell
============

* Pure functional
* Static type system
* GHC

GHC
====

* Interactive environment
* Industrial-strength optimizing
* Great concurrency support
* Plenty of features

Concurrency support
====================

微线程 + IO复用 + 多核调度

graph

微线程
======

.. code-block:: haskell

    server <- listen 8080
    forever $ do
        (handle, addr) <- accept server
        forkIO $ handleClient handle addr

微线程
======

.. code-block:: haskell

    timeout :: Int -> IO () -> IO ()
    timeout n f = do
        pid <- myThreadId
        bracket (forkIO $ threadDelay n >> throwTo pid ThreadTerminate)
                killThread
                (\_ -> f)

微线程
======

.. code-block:: haskell

    server <- listen 8080
    forever $ do
        (handle, addr) <- accept server
        forkIO . timeout 1000000 $ handleClient handle addr

Web framework
==============


