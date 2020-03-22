#!/usr/bin/python
import linkedlist
# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

"""
Algo:
D.S.: Linked List

Solution:

Corner cases:
"""

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def getListLen(head):
            cnt = 0
            while head:
                cnt += 1
                head = head.next
            return cnt

        def moveDiff(head, diff):
            while diff:
                head = head.next
                diff -= 1
            return head

        lenA = getListLen(headA)
        lenB = getListLen(headB)

        diff = abs(lenA - lenB)
        if lenA > lenB:
            headA = moveDiff(headA, diff)
        else:
            headB = moveDiff(headB, diff)

        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA

# Test Cases
if __name__ == "__main__":
	solution = Solution()
