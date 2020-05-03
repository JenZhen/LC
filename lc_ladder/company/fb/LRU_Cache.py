#! /usr/local/bin/python3

# https://leetcode.com/problems/lru-cache/submissions/
# Example

"""
Algo:
D.S.:

Solution:

Time: O(1)
Space: O(1)
Corner cases:
"""

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = {} # key: key, val: ref to node
        self.cache = DoubleLinkedList()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.cache.remove_node(node)
        self.cache.add_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.cache.remove_node(node)
            self.cache.add_to_head(node)
        else:
            node = ListNode(key, value)
            self.map[key] = node
            self.cache.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                # 不要忘记这一步
                del self.map[self.cache.tail.pre.key]
                self.size -= 1
                self.cache.remove_tail()

class ListNode:
    def __init__(self, key=None, val=None, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        # head<->node...node<->tail
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def remove_node(self, node):
        pre_node, next_node = node.pre, node.next
        pre_node.next = next_node
        next_node.pre = pre_node

    def add_to_head(self, node):
        pre_node, next_node = self.head, self.head.next
        pre_node.next = node
        node.pre = pre_node
        node.next = next_node
        next_node.pre = node

    def remove_tail(self):
        pre_node, next_node = self.tail.pre.pre, self.tail
        pre_node.next = next_node
        next_node.pre = pre_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
