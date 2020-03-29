#! /usr/local/bin/python3

# https://lintcode.com/problem/binary-tree-zigzag-level-order-traversal/description
# Example

"""
Algo: BFS
D.S.: deque implemented queue

Solution:
BFS same as level order traverse, use isReversed = false then negate after each level

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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        res = []
        if not root:
            return res
        q = deque([root])
        isReversed = False
        while len(q):
            level = []
            levelSize = len(q)
            for i in range(levelSize):
                cur = q.popleft()
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if isReversed:
                level.reverse()
            isReversed = not isReversed
            res.append(level)
        return res



# Test Cases
if __name__ == "__main__":
    solution = Solution()
