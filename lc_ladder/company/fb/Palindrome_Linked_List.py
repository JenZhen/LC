#! /usr/local/bin/python3

# https://www.lintcode.com/problem/palindrome-linked-list/description
# Example
# 设计一种方式检查一个链表是否为回文链表。
#
# 样例
# 样例 1:
#
# 输入: 1->2->1
# 输出: true
# 样例 2:
#
# 输入: 2->2->1
# 输出: false
# 挑战
# O(n)的时间和O(1)的额外空间。

"""
Algo:
D.S.: linked list, reverse linked list

Solution:
Time: O(n)
Space: O(1)
要注意奇偶情况
奇数，中间分两半共享一个节点，这时候翻转前半部分需要创建一个新的节点
偶数，不需要左右两半是不同的节点

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
    @param head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):
        # write your code here
        if not head:
            return True

        n = self._find_length(head)
        if n <= 1:
            return True
        mid = n // 2 if n % 2 == 0 else n // 2 + 1
        midleft, midright = head, None
        for i in range(mid - 1):
            midleft = midleft.next
        midright = midleft.next if n % 2 == 0 else midleft

        midleft = self._reverse(head, midleft, n)
        # self.print(midleft)
        # self.print(midright)
        # print(self._find_length(midleft))
        # print(self._find_length(midright))
        while midleft and midright:
            if midleft.val != midright.val:
                return False
            else:
                midleft = midleft.next
                midright = midright.next
        return True

    def _find_length(self, head):
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        return n

    def _reverse(self, head, midleft, n):
        pre = None
        cur = head
        nxt = head.next
        while cur != midleft:
            cur.next = pre
            pre = cur
            cur = nxt
            nxt = nxt.next
        if n % 2 == 1:
            newhead = ListNode(midleft.val)
            newhead.next = pre
            return newhead
        else:
            cur.next = pre
            return cur

    def print(self, head):
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        print('->'.join([str(i) for i in res]))

# Test Cases
if __name__ == "__main__":
    solution = Solution()
