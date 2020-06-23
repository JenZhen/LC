#! /usr/local/bin/python3

# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/submissions/

"""
Algo:
D.S.:

Solution:

Time: O()
Space: O()
Corner cases:
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        import collections

        if not root:
            return root

        q = collections.deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i < size - 1:
                    # there are still nodes in q
                    node.next = q[0]

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
# Test Cases
if __name__ == "__main__":
    solution = Solution()
