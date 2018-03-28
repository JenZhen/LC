#!/usr/bin/python

# https://leetcode.com/problems/lru-cache/description/
# Example

"""
Algo:
D.S.:

Solution:
Python, unlike c++ has container list served as double linked list. (Another option is deque)
Here with the help of self-implemented DoubleLinkedList, to complete the work
- head denotes the first element in the list, first means the most recently accessed element
- tail denotes the last element in the list, last means the least recently accessed element

Corner cases:
- list is empty: self.head = self.tail = None
- list has only 2: consider which one to remove
"""

class ListNode(object):
    def __init__(self, key=None, val=None, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class DoubleLinkedList(object):
    def __init__(self):
        self.head, self.tail = None, None

    def removeNode(self, node):
        # case1: if only 1 node
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        # case2: if 2 nodes, remove near head one
        if self.head == node:
            nextNode = node.next
            self.head = nextNode
            nextNode.pre = None
            return
        # case3: if 2 nodes, remove near tail one
        if self.tail == node:
            preNode = node.pre
            self.tail = preNode
            preNode.next = None
            return

        # case4: 3 or more nodes
        preNode = node.pre
        nextNode = node.next
        preNode.next = nextNode
        nextNode.pre = preNode
        return

    def removeTail(self):
        # tail meaninng least used node
        self.removeNode(self.tail)

    def addAtHead(self, node):
        # head meaning most recent node
        if self.head is None:
            self.head = node
            self.tail = node
            node.pre = None
            node.next = None
        else:
            nextNode = self.head
            self.head = node
            node.next = nextNode
            node.pre = None
            nextNode.pre = node


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.map = dict()
        self.cache = DoubleLinkedList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            targetNode = self.map[key]
            self.cache.removeNode(targetNode)
            self.cache.addAtHead(targetNode)
            return targetNode.val
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        """
        if key is duplicate:
            1. update node value
            2. move the new node position
        else:
            1. create a new node
            2. add new node to map
            3. after increasing the size of cache check if exceed limit
                if over limit:
                    remove the tail element
                    remove node in map
                else:
                    do nothing
        """
        if key in self.map:
            targetNode = self.map[key]
            targetNode.val = value
            self.cache.removeNode(targetNode)
            self.cache.addAtHead(targetNode)
            self.map[key].val = value
        else:
            newNode = ListNode(key, value)
            self.cache.addAtHead(newNode)
            self.map[key] = newNode
            self.size += 1
            if self.size > self.capacity:
                del self.map[self.cache.tail.key]
                self.cache.removeTail()
                self.size -= 1


# Test Cases
if __name__ == "__main__":
    c = LRUCache(2)
    # ["LRUCache","put","put","get","put","put","get"]
    # [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

    c.put(2, 1)
    c.put(2, 2)
    # c.checkMap()
    # c.checkList()
    print c.get(2)
    c.put(1, 1)
    # c.checkMap()
    # c.checkList()
    c.put(4, 1)
    # c.checkMap()
    # c.checkList()
    print c.get(2)
