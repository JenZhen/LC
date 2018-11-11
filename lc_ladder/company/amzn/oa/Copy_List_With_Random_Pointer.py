#! /usr/local/bin/python3

# https://www.lintcode.com/problem/copy-list-with-random-pointer/description?_from=ladder&&fromId=62
# Example

# 给出一个链表，每个节点包含一个额外增加的随机指针可以指向链表中的任何节点或空的节点。
#
# 返回一个深拷贝的链表。
#
# 挑战
# 可否使用O(1)的空间

"""
Algo:
D.S.:

Solution:


Corner cases:
"""

"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return None
        self.copyNext(head)
        self.copyRandom(head)
        return self.splitList(head)

    def copyNext(self, head):
        while head:
            newNode = RandomListNode(head.label)
            newNode.next = head.next
            head.next = newNode
            head = head.next.next

    def copyRandom(self, head):
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next

    def splitList(self, head):
        # the most difficult part
        newHead = head.next
        while head:
            copyNode = head.next
            head.next = copyNode.next
            head = head.next
            if head:
                copyNode.next = head.next
        return newHead

# Test Cases
if __name__ == "__main__":
    solution = Solution()
