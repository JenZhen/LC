#!/usr/bin/python
import linkedlist
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
# Singly linked list, sorted, given a node of it and a value
# Return the node where the new value is inserted
# Given a node from a Circular Linked List which is sorted in ascending order,
#write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the circular list.

# If there are multiple suitable places for insertion, you may choose any place to insert the new value.
# After the insertion, the circular list should remain sorted.
#
# If the list is empty (i.e., given node is null), you should create a new single circular list and
# return the reference to that single node. Otherwise, you should return the original given node.

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

Consider cases:
1. [] head is None
2. [1] single node circle
3. [1, 3] 2 or [1, 3] 1 or [1, 3] 3 put in betwee
4. [3, 1] 2 or [3, 1] 3 or [3, 1] 1
5. [1, 2] 3
6. [1, 2] 0
7. [1, 1] 3
8. [1, 1] 0

case 7. 8 需要判断cursor是不是又回到 head
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        p1 = head
        p2 = head.next

        while True:
			# break represents finding the location to insert
			# 1.r
            if p1.val <= insertVal <= p2.val:
                break
            if p1.val > p2.val and (p1.val <= insertVal or insertVal <= p2.val):
                break
            p1 = p2
            p2 = p2.next

            if p1 == head:
                break

        node = Node(insertVal)
        p1.next = node
        node.next = p2
        return head


# Test Cases
if __name__ == "__main__":
	solution = Solution()
