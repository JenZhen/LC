#! /usr/local/bin/python3

# https://lintcode.com/problem/binary-tree-level-order-traversal-ii/description
# Example

"""
Algo:
D.S.:

Solution:
BFS -- Same with Level Order traversal, just need to append at head or reverse the whole order
Time: O(N)
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
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
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

            res.insert(0, level)
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
