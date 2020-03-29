#! /usr/local/bin/python3

# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# Example

"""
Algo: BFS
D.S.: N-ary Tree

Solution:
BFS Level order traversal
Time Complexity: O(N)
Space Complexity: O(N)

Corner cases:
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        res = []
        q = deque([root])

        while q:
            size = len(q)
            level_tmp = []
            for i in range(size):
                cur = q.popleft()
                level_tmp.append(cur.val)
                for c in cur.children:
                    q.append(c)
            res.append(level_tmp[:])
        return res

# Test Cases
if __name__ == "__main__":
	solution = Solution()
