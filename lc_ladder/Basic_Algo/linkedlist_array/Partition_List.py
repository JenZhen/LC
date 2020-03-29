#!/usr/bin/python
import linkedlist
# https://leetcode.com/problems/partition-list/description/
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of the two partitions.
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.

"""
Algo:
D.S.: Linked List/Array

Solution:
1. in-place arrange list, too complex and error prone
2. seperate 2 list, but to be careful about the end of list should be None(clean)

Corner cases:
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
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        if head is None:
            return None
        leftDummy = ListNode(-1)
        rightDummy = ListNode(-1)
        leftCur = leftDummy; rightCur = rightDummy

        while head:
            # When reconnecting, don't need to make sure
            # new leftCur/rightCur points at None ie. break original list
            # But make sure after the loop, leftCur/rightCur breaks
            if head.val < x:
                leftCur.next = head
                leftCur = leftCur.next
            else:
                rightCur.next = head
                rightCur = rightCur.next
            head = head.next
        leftCur.next = rightDummy.next
        # Make sure rightCur.next breaks from original list
        rightCur.next = None
        return leftDummy.next

# Test Cases
if __name__ == "__main__":
	solution = Solution()
