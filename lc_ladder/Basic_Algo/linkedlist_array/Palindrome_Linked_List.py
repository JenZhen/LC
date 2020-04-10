#!/usr/local/bin/python3
import linkedlist
# https://leetcode.com/problems/palindrome-linked-list/
# Example
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
# Input: 1->2
# Output: false
# Example 2:
#
# Input: 1->2->2->1
# Output: true
# Follow up:
# Could you do it in O(n) time and O(1) space?
"""
Algo: Reverse linkedlist
D.S.: Linked List/Array

Solution:
挑战： O(1) space
找到重点 将前半个 list reverse
注意：重点在哪？ 奇数和偶数 个节点的计数问题
Corner cases:
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        size = self.get_length(head)
        cur = head
        for _ in range(size // 2 - 1):
            cur = cur.next
        if size % 2 == 1:
            head1 = cur
            head2 = cur.next.next
        else:
            head1 = cur
            head2 = cur.next

        self.reverse(head, head1.next)
        cur1, cur2 = head1, head2
        while cur1 and cur2:
            if cur1.val == cur2.val:
                cur1 = cur1.next
                cur2 = cur2.next
            else:
                return False
        return True

    def get_length(self, head):
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
        return cnt

    def reverse(self, head, tail):
        # [head, tail)
        if head == tail:
            return
        pre = None
        cur = head
        nxt = cur.next
        while cur != tail:
            cur.next = pre
            pre = cur
            cur = nxt
            nxt = nxt.next


# Test Cases
if __name__ == "__main__":
	solution = Solution()
