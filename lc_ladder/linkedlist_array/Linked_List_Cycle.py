#!/usr/bin/python
import linkedlist
# https://leetcode.com/problems/linked-list-cycle/description/
# Given a list decide if there is a cycle

"""
Algo:
D.S.: Linked List/Array

Solution:
2 pointer faster and slower
- starting head and head.next

Corner cases:
"""

class Solution(object):
	def hasCycle(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		if head is None or head.next is None:
			return False
		r1, r2 = head, head.next
		while r2.next and r2.next.next:
			r2 = r2.next.next
			r1 = r1.next
			if r1 == r2:
				return True
		return False
# Test Cases
if __name__ == "__main__":
	solution = Solution()
