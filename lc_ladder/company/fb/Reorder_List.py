#! /usr/local/bin/python3

# https://leetcode.com/problems/reorder-list/submissions/
# Example
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example 1:
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
Algo:
D.S.:

Solution:
1. Middle of the Linked List.
2. Reverse Linked List.
3. Merge Two Sorted Lists.

Time: O(N)
Space: O(1)
Corner cases:
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return head

        s, f = head, head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        head2 = s.next
        s.next = None

        head3 = self.reverse(head2)
        # self.print(head)
        # self.print(head3)
        return self.merge(head, head3)

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def merge(self, h1, h2):
        dummy = ListNode()
        cur = dummy
        while h1 and h2:
            cur.next = h1
            h1 = h1.next
            cur = cur.next
            cur.next = h2
            h2 = h2.next
            cur = cur.next
        if h1:
            cur.next = h1
        head = dummy.next

    def print(self, head):
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
