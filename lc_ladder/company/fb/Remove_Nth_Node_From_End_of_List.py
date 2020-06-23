#! /usr/local/bin/python3

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
#
# Follow up:
# Could you do this in one pass?

"""
Algo: sliding window for list
D.S.:

Solution:
1, 2, 3, 4, 5 n = 2
p1, p2 相距 2
注意 corner case N 特别大，比List还长

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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n <= 0 or not head: return head

        dummy = ListNode(-1)
        dummy.next = head

        p1 = head
        for _ in range(n):
            if not p1:
                return None
            p1 = p1.next
        p2 = head
        pre = dummy
        while p1:
            p1 = p1.next
            p2 = p2.next
            pre = pre.next

        pre.next = p2.next
        p2.next = None
        return dummy.next

# Test Cases
if __name__ == "__main__":
    solution = Solution()
