#!/usr/bin/python
import linkedlist
# http://www.jiuzhang.com/solution/insert-into-a-cyclic-sorted-list/
# Singly linked list, sorted, given a node of it and a value
# Return the node where the new value is inserted

"""
Algo: Traverse a singly list
D.S.: Linked List/Array

Solution:
Singly linked list is hard to binary serach.
Based on where the given node is, find the position new nodes shold be.
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> (1)
1. Given node = 1, x = 4.5
2. Given node = 5, x = 4.5
3. Given node = 1, x = 7
4. Given node = 1, x = 0

Keep a small searching window of 2 nodes, p1, p2, where p1.next = p2
Case1. p1 < p1 (mostly) and p1 <= x <= p2, x should be in-between
	Very important, this case handle value equal case
Case2. p1 > p2 (p1 max, p2 min),
	if x > p1, x > max, insert after p1
	if x < p2, x < min, insert before p2 (after p1)

Time Complexity: O(N) iterate thru the whole list
Corner cases:
1. Given node is None, list is empty
2. Given list has one node (can be merged in regular case)
Consider value equal case
"""

"""
Definition of ListNode
class ListNode(object):

	def __init__(self, val, next=None):
		self.val = val
		self.next = next
"""
class Solution:
	# @param {ListNode} node a list node in the list
	# @param {int} x an integer
	# @return {ListNode} the inserted new list node
	def insert(self, node, x):
		# Write your code here
		if node is None:
			curNode = listNode(x)
			curNode.next = curNode
			return curNode

		p1 = node
		p2 = node.next
		while True:
			# case 1 and p1 == p2 case
			if p1.val <= x and p2.val:
				break
			# case 2
			if p1.val > p1.val and (x > p1.val or x < p2.val):
				break
			p1 = p2
			p2 = p2.next

		# Insert in between p1, p2
		curNode = listNode(x)
		p1.next = curNode
		curNode.next = p2
		return curNode


# Test Cases
if __name__ == "__main__":
	solution = Solution()
