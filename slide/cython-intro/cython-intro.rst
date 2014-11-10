===============
Python 代码优化
===============

:author: yihuang
:email: yi.codeplayer@gmail.com
:company: 深圳云悦科技

Redis API
=========

.. code-block:: python

    conn.execute('get', 'key')

    # VS

    conn.get('key')

Redis API Pipeline
==================

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

Redis API Pipeline
==================

.. code-block:: python

    conn.execute_pipeline(
        *[('get', 'key%d'%i) for i in range(10)]
    )

    # VS

    pipe = conn.pipeline()
    for i in range(10):
        pipe.get('key%d'%i)
    pipe.execute()

Protocol Buffer
===============

.. code-block:: protobuf

    message Test {
        required int32 a = 1;
        optional int32 b = 2;
    }

    Test(10, 10)
    # image to explain encoding of Test message

Protocol Buffer
===============

* A simple design with a huge implementation.

Pythonic Protocol Buffer
========================

.. code-block:: python

    class Person(ProtoEntity):
        a = Field('int32', 1)
        b = Field('int32', 2, required=False)


