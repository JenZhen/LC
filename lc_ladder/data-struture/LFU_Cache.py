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
class ListNode(object):
    def __init__(self, key=None, value=None, pre=None, next=None):
        self.key = key
        self.val = value
        self.pre = pre
        self.next = next

class DoubleLinkedList(object):
    # head->node1->node2->...->noden->tail
    # head side is MORE recently accessed
    # tail side is LESS recently accessed
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def removeNode(self, node):
        # not check node validity in this function
        preNode = node.pre
        nextNode = node.next
        preNode.next = nextNode
        nextNode.pre = preNode

    def addAtHead(self, node):
        nextNode = self.head.next
        self.head.next = node
        node.next = nextNode
        node.pre = self.head
        nextNode.pre = node

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.cache = DoubleLinkedList()
        self.freqMap = dict()
        self.heap = []
        heapq.heapify(self.heap)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        """
        if not in freqMap:
            return -1
        else:
            increase freqMap
        """


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """



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
