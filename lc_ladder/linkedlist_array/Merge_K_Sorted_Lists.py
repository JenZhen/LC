#!/usr/bin/python
import linkedlist
# https://leetcode.com/problems/merge-k-sorted-lists/description/
# Example

"""
Algo:
D.S.: Linked List/Array

Solution:

Corner cases:
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# python heapq is min heap api
from heapq import heappop, heappush

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        preHead = ListNode(-1)
        runner = preHead
        heap = []

        for ll in lists:
            if ll:
                self.heapPushNode(heap, ll)
        while heap:
            runner.next = heapq.heappop(heap)[1]
            runner = runner.next
            if runner.next:
                self.heapPushNode(heap, runner.next)
        return preHead.next

    # heap item is a tuple (value, node)
    # value is the comparison
    def heapPushNode(self, heap, node):
        heapq.heappush(heap, (node.val, node))

# Test Cases
if __name__ == "__main__":
	solution = Solution()
