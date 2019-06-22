#!/usr/bin/python

# https://leetcode.com/problems/lfu-cache/description/
# Example
# Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

# Follow up:
# Could you do both operations in O(1) time complexity?

"""
Algo: linked list, heap
D.S.:

Solution:

Corner cases:
"""
import heapq
# class ListNode(object):
#     def __init__(self, key=None, value=None, pre=None, next=None):
#         self.key = key
#         self.val = value
#         self.pre = pre
#         self.next = next
#
# class DoubleLinkedList(object):
#     # head->node1->node2->...->noden->tail
#     # head side is MORE recently accessed
#     # tail side is LESS recently accessed
#     def __init__(self):
#         self.head = ListNode()
#         self.tail = ListNode()
#         self.head.next = self.tail
#         self.tail.pre = self.head
#
#     def removeNode(self, node):
#         # not check node validity in this function
#         preNode = node.pre
#         nextNode = node.next
#         preNode.next = nextNode
#         nextNode.pre = preNode
#
#     def addAtHead(self, node):
#         nextNode = self.head.next
#         self.head.next = node
#         node.next = nextNode
#         node.pre = self.head
#         nextNode.pre = node

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



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Test Cases
if __name__ == "__main__":
    solution = Solution()


    LFUCache cache = new LFUCache( 2 /* capacity */ );

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.get(3);       // returns 3.
    cache.put(4, 4);    // evicts key 1.
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4
