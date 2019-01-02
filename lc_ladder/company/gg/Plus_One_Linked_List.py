#! /usr/local/bin/python3

# https://www.lintcode.com/problem/plus-one-linked-list/description?_from=ladder&&fromId=18
# Example
# 给定一个非负整数，这个整数表示为一个非空的单链表，每个节点表示这个整数的一位。返回这个整数加一。
# 除了0本身，所有数字在最高位前都没有0。
#
# 列表的头节点存的是这个整数的最高位。
# 样例
# 给出链表1 -> 2 -> 3 -> null，返回 1 -> 2 -> 4 -> null。

"""
Algo:
D.S.: Linked list, stack, reverse a linked list

Solution:
要点：这个题给出的链表方向从高位到低位，不利于做加法。
要reverse order有2个办法 1）stack，2）reverse Linkedlist
1. stack 要
Corner cases:
"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here
        if not head:
            return ListNode(1)

        reversedList = self.reverse(head)
        self.print(reversedList)
        carry = 1
        cur = reversedList
        while cur:
            sum = cur.val + carry
            cur.val = sum % 10
            carry = sum // 10
            cur = cur.next
        self.print(reversedList)

        if carry == 1:
            cur = reversedList
            while cur.next is not None:
                cur = cur.next
            cur.next = ListNode(1)

        self.print(reversedList)
        return self.reverse(reversedList)

    def reverse(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def print(self, list):
        res = []
        cur = list
        while cur:
            res.append(cur.val)
            cur = cur.next
        print(res)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
