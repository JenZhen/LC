#! /usr/local/bin/python3

# https://leetcode.com/problems/odd-even-linked-list/
# Example
# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
# Example 1:
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# Example 2:
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
# Note:
#
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...
"""
Algo:
D.S.:

Solution:
build 2 head and connect

Time: O(n)
Space: O(1)
Corner cases:
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        h1, h2 = ListNode(), ListNode()
        c1, c2 = h1, h2
        i = 1
        cur = head
        while cur:
            if i % 2 == 1:
                c1.next = cur
                cur = cur.next
                c1 = c1.next
                # 注意 要挪next to None
                c1.next = None
            else:
                c2.next = cur
                cur = cur.next
                c2 = c2.next
                # 注意 要挪next to None
                c2.next = None
            i += 1
        c1.next = h2.next
        return h1.next

# Test Cases
if __name__ == "__main__":
    solution = Solution()
