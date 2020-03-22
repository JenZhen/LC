#!/usr/bin/python
from linkedlist import LinkedList
from linkedlist import ListNode
# https://leetcode.com/problems/merge-two-sorted-lists/description/

"""
Algo:
D.S.: Linked List/Array

Solution:
1. Merging one list into another is difficult, easier way is to
2. For Linked list manipulation, using a dummyHead is easier to handle the first node

Time Complexity: O(N), all accessed

Similar to "Merge two sorted arrays"
Corner cases:
"""

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if l1 is None:
			return l2
		if l2 is None:
			return l1

		# It's hard to merge l1 into l2 or l2 into l1
		# The merging may be alternating
		# It's easier to form a new list
		dummyHead = ListNode(-1)
		runner = dummyHead
		while l1 and l2:
			if l1.val <= l2.val:
				runner.next = l1
				l1 = l1.next
				runner = runner.next
			else:
				runner.next = l2
				l2 = l2.next
				runner = runner.next
		if l1 is not None:
			runner.next = l1
		if l2 is not None:
			runner.next = l2

		return dummyHead.next

# Test Cases
if __name__ == "__main__":
	solution = Solution()
	a1 = [1,3,5,7]
	a2 = [2,4]
	l1 = LinkedList(a1)
	l2 = LinkedList(a2)
	newList = LinkedList()
	newHead = solution.mergeTwoLists(l1.getHead(), l2.getHead())
	newList.setHead(newHead)
	print newList.__repr__()

