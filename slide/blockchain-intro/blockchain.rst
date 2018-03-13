==========
区块链介绍
==========

行业特点
========

* 开源
* p2p理念
* 安全性(理论安全，和实现安全)

数据结构
========

* hash list
* hash chain
* hash tree(Merkle tree)
* blockchain

BlockChain
==========

figure TODO.

SPV Proof
==========

figure TODO.

bloom filter
============

TODO

p2p网络
========

* gossip network
* kademlida DHT

eclipse attack
==============

figure TODO

* 路由表优先旧节点
* 提高伪造地址难度（hash+nouce)
* 限制相同地址下节点数量

共识算法
========

* 目的：需要一个节点来处理写请求（共识+随机）
* PoW：算力竞赛+最长链
* PoS：随机选择+最长链
* PBFT: TODO

PoW
====

* 利用哈希值证明工作量(防DoS)
* 简洁，安全性论证简单
* 不环保
* 矿工利益和币价不必然挂钩

PoS(Ouroboros)
===============

* 多方共同产生一个随机数
* 执行 follow-the-satoshi 算法

如何产生随机数
==============

Commit和Open
=============

Coin-Tossing
=============

Verifiable Secret Sharing
==========================

完整随机数协议
===============

Ouroboros安全性证明
===================
