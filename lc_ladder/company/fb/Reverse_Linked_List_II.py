#! /usr/local/bin/python3

# https://leetcode.com/problems/reverse-linked-list-ii/submissions/
# Example
# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL

"""
Algo: reverse linked list模板
D.S.:

Solution:

Time: O(N)
Space: O()
Corner cases:
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head: return head
        if m == n: return head

        dummy = ListNode()
        dummy.next = head
        i = 0
        pre_node, m_node, n_node, post_node = None, None, None, None
        cur = dummy
        while cur:
            if i == m - 1: pre_node = cur
            if i == m: m_node = cur
            if i == n: n_node = cur
            if i == n + 1: post_node = cur
            i += 1
            cur = cur.next

        # reverse list 模板
        # reverse from m to n
        prev = pre_node
        cur = m_node
        # cur not equal to the one after n
        while cur != post_node:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        pre_node.next = n_node
        m_node.next = post_node
        return dummy.next




# Test Cases
if __name__ == "__main__":
    solution = Solution()
