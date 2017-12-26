#!/usr/bin/python
import linkedlist
# https://leetcode.com/problems/reverse-linked-list/description/
# Use both iteration and recursion

"""
Algo: Iteration/Recursion
D.S.: Linked List

Solution:
1. Iteration
2. Recursion
1->2->3->4->5
1->2->3<-4<-5
            p
   h h.next
   reverse 2->3 arrow
   pass p down

Corner cases:
"""

class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        runner = head
        while runner:
            tmp = runner.next
            runner.next = pre
            pre = runner
            runner = tmp
        return pre

class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        revHead = self.reverseList(head.next)
        # reverse direction
        head.next.next = head
        head.next = None
        return revHead

# Test Cases
if __name__ == "__main__":
	solution = Solution()
