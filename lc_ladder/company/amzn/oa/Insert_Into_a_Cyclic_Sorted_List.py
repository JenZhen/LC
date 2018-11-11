#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo:
D.S.:

Solution:


Corner cases:
!!!
1) no node
2) 1 node
3) duplicates
4) original list is of one number
2->2->2 insert 3
2->2->2 insert 1
while f != node
DO NOT USE while True: dead loop
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        # write your code here
        if not node:
            newNode = ListNode(x)
            newNode.next = newNode
            return newNode
        if node.next == node:
            newNode = ListNode(x)
            node.next = newNode
            newNode.next = node
            return node
        b, f = node, node.next
        while f != node:
            if b.val <= x <= f.val:
                break
            elif b.val > f.val and (x >= b.val or x <= f.val):
                break
            else:
                b = b.next
                f = f.next
        newNode = ListNode(x)
        b.next = newNode
        newNode.next = f
        return newNode

# Test Cases
if __name__ == "__main__":
    solution = Solution()
