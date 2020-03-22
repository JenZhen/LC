#!/usr/bin/python

# https://leetcode.com/problems/lru-cache/description/
# Example: passed OJ

"""
Algo:
D.S.:

Solution:
# head->node1->node2->...>noden->tail
Corner cases:
"""

class ListNode(object):
    def __init__(self, key=None, val=None, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class DoubleLinkedList(object):
    def __init__(self):
        # head->node1->node2->...>noden->tail
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def addAtHead(self, node):
        # add the most recently accessed node to head side
        nextNode = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = nextNode
        nextNode.pre = node

    def removeNode(self, node):
        preNode = node.pre
        nextNode = node.next
        preNode.next = nextNode
        nextNode.pre = preNode

    def removeTailNode(self):
        LRNode = self.tail.pre
        self.removeNode(LRNode)

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
         # key: keyOfElement
        # val: ListNode ref
        self.map = dict()
        self.cache = DoubleLinkedList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        """
        if in map:
            1. get the targetNode
            2. removeNode
            3. addAtHead
            return value
        else:
            return -1
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
            1. create a new node and add at head
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
            self.map[key].val = value
            self.cache.removeNode(targetNode)
            self.cache.addAtHead(targetNode)
        else:
            newNode = ListNode(key, value)
            self.cache.addAtHead(newNode)
            self.map[key] = newNode
            self.size += 1
            if self.size > self.capacity:
                del self.map[self.cache.tail.pre.key]
                self.cache.removeTailNode()
                self.size -= 1


    def checkMap(self):
        print("Debuggin map ==============")
        for key, value in self.map.items():
            print("[key: %s, val: %s]" %(key, value.val))

    def checkList(self):
        print("Debugging list ============")
        elements = []
        cur = self.cache.head.next
        while cur is not self.cache.tail:
            elements.append(str(cur.val))
            cur = cur.next
        print elements
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Test Cases
if __name__ == "__main__":
    c = LRUCache(2)
    # ["LRUCache","put","put","get","put","put","get"]
    # [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

    c.put(2, 1)
    c.put(2, 2)
    c.checkMap()
    c.checkList()
    print c.get(2)
    c.put(1, 1)
    c.checkMap()
    c.checkList()
    c.put(4, 1)
    c.checkMap()
    c.checkList()
    print c.get(2)
