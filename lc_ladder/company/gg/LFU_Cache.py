#! /usr/local/bin/python3

# https://www.lintcode.com/problem/lfu-cache/description?_from=ladder&&fromId=18
# Example
# LFU是一个著名的缓存算法
# 实现LFU中的set 和 get
#
# 样例
# capacity = 3
#
# set(2,2)
# set(1,1)
# get(2)
# >> 2
# get(1)
# >> 1
# get(2)
# >> 2
# set(3,3)
# set(4,4)
# get(3)
# >> -1
# get(2)
# >> 2
# get(1)
# >> 1
# get(4)
# >> 4

"""
Algo:
D.S.: Dict/hashmap, Doubly-linkedlist

Solution:
为“最不常使用缓存”（LFU cache）设计实现数据结构。应当支持get和set操作。

get(key) - 如果存在key，返回其对应的value，否则返回-1。

set(key, value) - 如果不存在key，新增value；否则替换原始value。当缓存容量满时，应当将最不常使用的项目移除。如果存在使用频度相同的多个项目，则移除最近最少使用（Least Recently Used）的项目。

进一步思考：

能否在O(1)时间完成操作？

解题思路：
双向链表（Doubly Linked List） + 哈希表（Hash Table）

首先定义双向链表节点：KeyNode（Key节点）与FreqNode（频度节点）。

KeyNode中保存key（键），value（值），freq（频度），prev（前驱），next（后继）

FreqNode中保存freq（频度）、prev（前驱）、next（后继）、first（指向最新的KeyNode），last（指向最老的KeyNode）
在数据结构LFUCache中维护如下属性：

capacity：缓存的容量
keyDict：从key到KeyNode的映射
freqDict：从freq到FreqNode的映射
head：指向最小的FreqNode
整体数据结构设计如下图所示：

head --- FreqNode1 ---- FreqNode2 ---- ... ---- FreqNodeN
              |               |                       |
            first           first                   first
              |               |                       |
           KeyNodeA        KeyNodeE                KeyNodeG
              |               |                       |
           KeyNodeB        KeyNodeF                KeyNodeH
              |               |                       |
           KeyNodeC         last                   KeyNodeI
              |                                       |
           KeyNodeD                                 last
              |
            last


Corner cases:
"""

class KeyNode(object):
    def __init__(self, key, value, freq = 1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = self.next = None

class FreqNode(object):
    def __init__(self, freq, prev, next):
        self.freq = freq
        self.prev = prev
        self.next = next
        self.first = self.last = None

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.keyDict = dict()
        self.freqDict = dict()
        self.head = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.keyDict:
            keyNode = self.keyDict[key]
            value = keyNode.value
            self.increase(key, value)
            return value
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        if key in self.keyDict:
            self.increase(key, value)
            return
        if len(self.keyDict) == self.capacity:
            self.removeKeyNode(self.head.last)
        self.insertKeyNode(key, value)

    def increase(self, key, value):
        """
        Increments the freq of an existing KeyNode<key, value> by 1.
        :type key: str
        :rtype: void
        """
        keyNode = self.keyDict[key]
        keyNode.value = value
        freqNode = self.freqDict[keyNode.freq]
        nextFreqNode = freqNode.next
        keyNode.freq += 1
        if nextFreqNode is None or nextFreqNode.freq > keyNode.freq:
            nextFreqNode = self.insertFreqNodeAfter(keyNode.freq, freqNode)
        self.unlinkKey(keyNode, freqNode)
        self.linkKey(keyNode, nextFreqNode)

    def insertKeyNode(self, key, value):
        """
        Inserts a new KeyNode<key, value> with freq 1.
        :type key: str
        :rtype: void
        """
        keyNode = self.keyDict[key] = KeyNode(key, value)
        freqNode = self.freqDict.get(1)
        if freqNode is None:
            freqNode = self.freqDict[1] = FreqNode(1, None, self.head)
            if self.head:
                self.head.prev = freqNode
            self.head = freqNode
        self.linkKey(keyNode, freqNode)

    def delFreqNode(self, freqNode):
        """
        Delete freqNode.
        :rtype: void
        """
        prev, next = freqNode.prev, freqNode.next
        if prev: prev.next = next
        if next: next.prev = prev
        if self.head == freqNode: self.head = next
        del self.freqDict[freqNode.freq]

    def insertFreqNodeAfter(self, freq, node):
        """
        Insert a new FreqNode(freq) after node.
        :rtype: FreqNode
        """
        newNode = FreqNode(freq, node, node.next)
        self.freqDict[freq] = newNode
        if node.next: node.next.prev = newNode
        node.next = newNode
        return newNode

    def removeKeyNode(self, keyNode):
        """
        Remove keyNode
        :rtype: void
        """
        self.unlinkKey(keyNode, self.freqDict[keyNode.freq])
        del self.keyDict[keyNode.key]

    def unlinkKey(self, keyNode, freqNode):
        """
        Unlink keyNode from freqNode
        :rtype: void
        """
        next, prev = keyNode.next, keyNode.prev
        if prev: prev.next = next
        if next: next.prev = prev
        if freqNode.first == keyNode: freqNode.first = next
        if freqNode.last == keyNode: freqNode.last = prev
        if freqNode.first is None: self.delFreqNode(freqNode)

    def linkKey(self, keyNode, freqNode):
        """
        Link keyNode to freqNode
        :rtype: void
        """
        firstKeyNode = freqNode.first
        keyNode.prev = None
        keyNode.next = firstKeyNode
        if firstKeyNode: firstKeyNode.prev = keyNode
        freqNode.first = keyNode
        if freqNode.last is None: freqNode.last = keyNode

# Test Cases
if __name__ == "__main__":
    solution = Solution()
