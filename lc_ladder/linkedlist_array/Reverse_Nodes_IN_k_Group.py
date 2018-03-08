#!/usr/bin/python
import linkedlist
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# Use both iteration and recursion

"""
Algo: Iteration/Recursion
D.S.: Linked List

Solution:
1. Iteration
2. Recursion
1->2->3->4->5
1->2->3<-4<-5
            p
   h h.next
   reverse 2->3 arrow
   pass p down

Corner cases:
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Didn't pass
class Solution1(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 1:
            return head

        preHead = None
        pre = ListNode(-1)
        pre.next = head
        cur = head
        nex = cur.next

        cnt = 0
        while cur is not None:
            cnt += 1
            cur = cur.next

        while cnt >= k:
            cur = pre.next
            nex = cur.next
            # revert k numbers meaning revert k -1 in-between arrows
            for i in range(k - 1):
                tmpNode = nex.next
                nex.next = pre.next
                cur.next = tmpNode
                pre.next = nex
                # prepare for next for loop
                next = tmpNode
            if preHead == None:
                preHead = nex
            pre = cur
            cnt -= k

        return preHead

class Solution2:
    # input: 1->2->3
    #      start  end
    # output: 3->2->1
    #      end     start
    def reverse(self, start, end):
        newhead = ListNode(-1)
        newhead.next = start
        while newhead.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = newhead.next
            newhead.next = tmp
        return [end, start]

    """
    @param: head: a ListNode
    @param: k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here

        if head == None or k == 1:
            return head
        nhead = ListNode(-1)
        nhead.next = head
        start = nhead
        while start.next:
            end = start
            for i in range(k - 1):
                end = end.next
                if end.next == None:
                    return nhead.next
            [newStart, newEnd] = self.reverse(start.next, end.next)
            start.next = newStart
            start = newEnd
        return nhead.next
# Test Cases
if __name__ == "__main__":
	solution = Solution()
