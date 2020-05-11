#! /usr/local/bin/python3

# https://leetcode.com/problems/copy-list-with-random-pointer/
# Example

"""
Algo:
D.S.:

Solution:
Time: O(N)
Space: O(1)

Corner cases:
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        cur = head
        # add node after node
        while cur:
            new_node = Node(cur.val)
            tmp = cur.next
            new_node.next = tmp
            cur.next = new_node
            cur = tmp

        # add random pointer
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # break list
        dummy = Node(-1)
        dummy.next = head.next
        c1 = head
        c2 = dummy.next
        while c2.next:
            tmp = c2.next
            c1.next = tmp
            c2.next = tmp.next
            c1 = c1.next
            c2 = c2.next
        c1.next = None
        return dummy.next
# Test Cases
if __name__ == "__main__":
    solution = Solution()
