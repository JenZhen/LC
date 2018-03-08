#!/usr/bin/python
import linkedlist
# https://leetcode.com/problems/sort-list/description/
# Example

"""
Algo: Divide and Conquer
D.S.: Linked List/Array

Solution:
Merge Sort
Complexity O(NlogN)
Corner cases:
"""
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p1, p2 = head, head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

        p2 = p1.next
        p1.next = None

        leftHalf = self.sortList(head)
        rightHalf = self.sortList(p2)
        return self.merge(leftHalf, rightHalf)

    def merge(self, l, r):
        import sys
        dummy = ListNode(0)
        runner = dummy
        while l or r:
            valL = sys.maxint if l is None else l.val
            valR = sys.maxint if r is None else r.val
            if valL <= valR:
                runner.next = l
                l = l.next
            else:
                runner.next = r
                r = r.next
            runner = runner.next

        return dummy.next
# Test Cases
if __name__ == "__main__":
	solution = Solution()
