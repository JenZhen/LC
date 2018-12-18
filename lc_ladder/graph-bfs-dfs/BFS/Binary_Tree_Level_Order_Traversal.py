#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo: BFS
D.S.: deque implmented queue;

Solution:
1. BFS
Time: O(n) all nodes iterate once

2. DFS：not recommended
Corner cases:
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
        q = deque([])
        q.append(root)
        res = []
        while len(q):
            levelSize = len(q)
            level = []
            for i in range(levelSize):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            res.append(level)
        return res




# Test Cases
if __name__ == "__main__":
    solution = Solution()
