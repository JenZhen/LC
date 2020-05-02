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

        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next

        half_size = 0
        if size % 2 == 1:
            # 长度为5，断在2后面
            half_size = size // 2
        else:
            # 长度为4，断在2后面
            half_size = size // 2

        cur = head
        i = 1
        while i < half_size:
            cur = cur.next
            i += 1
        # break after half
        head2 = cur.next
        cur.next = None

        # reverse from head2
        prev = None
        cur = head2
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        head2 = prev

        # merge head & head2, head2 is longer if ttl is odd number
        dummy = ListNode()
        cur = dummy
        c1, c2 = head, head2
        print(head)
        print(head2)
        while c1 and c2:
            cur.next = c1
            c1 = c1.next
            cur = cur.next
            cur.next = c2
            c2 = c2.next
            cur = cur.next
        return dummy.next

# Test Cases
if __name__ == "__main__":
    solution = Solution()
