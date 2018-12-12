#!/usr/local/bin/python3

# https://www.lintcode.com/problem/lru-cache/description?_from=ladder&&fromId=8
# Example
# 为最近最少使用（LRU）缓存策略设计一个数据结构，它应该支持以下操作：获取数据（get）和写入数据（set）。
#
# 获取数据get(key)：如果缓存中存在key，则获取其数据值（通常是正数），否则返回-1。
#
# 写入数据set(key, value)：如果key还没有在缓存中，则写入其数据值。当缓存达到上限，它应该在写入新数据之前删除最近最少使用的数据用来腾出空闲位置

"""
Solution:
Time: O(1): Space O(capacity)
这个是用单向链表解决，其他的算法是双向

Corner cases:
moveNextToTail will handle everything

"""
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.next = None

class LRUCache:

    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = ListNode(0, 0) # dummy head ahead of real head
        self.tail = self.head
        self.keyToPreNode = {} # since no prev pointer, use prev node to track

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.keyToPreNode:
            return -1
        self.moveNextToTail(key)
        return self.tail.val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # 1) if key in map, modify existing node
        if key in self.keyToPreNode:
            self.keyToPreNode[key].next.val = value
            self.moveNextToTail(key)
            return

        # 2) if key not in map, add not over capacity, add to tail
        if self.size < self.capacity:
            newNode = ListNode(key, value)
            self.tail.next = newNode
            self.keyToPreNode[key] = self.tail
            self.tail = newNode
            self.size += 1
            return

        # 3) if key not in map add over capacity, update head, then move to tail
        firstNode = self.head.next

        # remove old first info
        del self.keyToPreNode[firstNode.key]

        # modify to new node
        firstNode.key = key
        firstNode.val = value
        self.keyToPreNode[firstNode.key] = self.head

        # move to tail
        self.moveNextToTail(key)

    def moveNextToTail(self, key):
        # input: key (int) of the node to be moved
        preNode = self.keyToPreNode[key]
        curNode = preNode.next

        if curNode is None or curNode == self.tail:
            return

        preNode.next = preNode.next.next
        self.keyToPreNode[preNode.next.key] = preNode
        self.tail.next = curNode
        self.keyToPreNode[curNode.key] = self.tail
        self.tail = curNode

    def printCache(self):
        pass
        # nodeList = []
        # runner = self.head.next
        # while runner:
        #     nodeList.append((runner.key, runner.val))
        #     runner = runner.next
        # print("->".join([("(" + str(ele[0]) + ":" + str(ele[1])+ ")") for ele in nodeList]))
# Test Cases
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.set(2, 1)
    cache.printCache()
    cache.set(1, 1)
    cache.printCache()
    print(cache.get(2)) # 1
    cache.printCache()
    cache.set(4, 1)
    cache.printCache()
    print(cache.get(1)) # -1
    cache.printCache()
    print(cache.get(2)) # 1
    cache.printCache()
