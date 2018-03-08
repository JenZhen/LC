#!/usr/bin/python
import linkedlist
# https://leetcode.com/problems/linked-list-cycle-ii/description/
# Given a list to find the start of the cycle

"""
Algo:
D.S.: Linked List/Array

Solution:
2 pointer faster and slower
- starting head and head.next

Common case:
head--------start----|(meet)
			  |______|

Corner case:
start/heaad----|(meet)
		|______|

head->start: x
cycle: y
start-> meet: z
need to find meet->start z', z' = y - z
When at meet, fast pointer surpass slow pointer length of cycle and fast is slow's twice distance

x + y + z = 2(x + z)
y = x + z
y - z = x = z'

So, after fast meets slow, put slow at head and move one node per step
HOWEVER, this doesn't work if head->meet is only 1 node away, ie the corner case
Solution, DO NOT init slow/faster at a preHead pointer position, just put it at head, meaning 1 node offset

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        fast = head; slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

# Test Cases
if __name__ == "__main__":
	solution = Solution()
