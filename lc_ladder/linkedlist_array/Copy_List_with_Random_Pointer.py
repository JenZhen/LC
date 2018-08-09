#!/usr/bin/python
from linkedlist import *
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
# Deep copy a linked list, the node has a random pointer to a node in list or null
#


"""
Algo:
D.S.: Linked List, map

Solution:
1. 2 round of traverse
	- copy next node (save to hashmap)
	- copy the random node (if random is not None, check hashMap)
Time Complexity: O(2 * N)
Space Compelxity: O(N)

2. 1 roudn of travese
	- Copy next node and random node at same time
	- for next and random check hashMap if exist then connects

3. 1 -> 2 -> 3 -> 4
   1 -> 1'-> 2 -> 2'-> 3 -> 3'-> 4- > 4', then split
Time: O(N)
Space: O(1)

Key parts:
- Iterate linked list, it's useful to have a dummy before head, then return dummy.next
- seperate head == None and else, handle head before iteration is easier

Time Complexity: O(2 * N)
Space Compelxity: O(N)

Corner cases:
"""

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution1(object):
	def copyRandomList(self, head):
		"""
		:type head: RandomListNode
		:rtype: RandomListNode
		"""
		if head is None:
			return None

		dummy = RandomListNode(0)
		p = head
		q = RandomListNode(p.label)
		dummy.next = q
		hashMap = {}
		hashMap[p] = q
		while p:
			if p.next:
				q.next = RandomListNode(p.next.label)
				hashMap[p.next] = q.next
			# q.next default as None
			p = p.next
			q = q.next

		q = dummy.next
		p = head
		while p:
			if p.random:
				q.random = hashMap[p.random]
			p = p.next
			q = q.next
		return dummy.next

class Solution2(object):
	def copyRandomList(self, head):
		"""
		:type head: RandomListNode
		:rtype: RandomListNode
		"""
		if head is None:
			return None

		dummy = RandomListNode(0)
		p = head
		q = RandomListNode(p.label)
		dummy.next = q
		hashMap = {}
		hashMap[p] = q
		while p:
			if p.next:
				if p.next in hashMap:
					q.next = hashMap[p.next]
				else:
					q.next = RandomListNode(p.next.label)
					hashMap[p.next] = q.next
			if p.random:
				if p.random in hashMap:
					q.random = hashMap[p.random]
				else:
					q.random = RandomListNode(p.random.label)
					hashMap[p.random] = q.random
			p = p.next
			q = q.next
		return dummy.next


class Solution3(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
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
	solution3 = Solution3()
	orig = LinkedList([3,5,2,1])
	new = solution3.copyRandomList(orig)
	print new
