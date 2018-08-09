#! /usr/local/bin/python3

# https://lintcode.com/problem/clone-binary-tree/description
# Example

"""
Algo: BFS
D.S.: deque implemented queue

Solution:
BFS a tree
- round 1: copy nodes
- round 2: copy edges

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
    @param root: The root of binary tree
    @return: root of new tree
    """
    def cloneTree(self, root):
        # write your code here

        if not root:
            return None
        nodeMap = {}
        q = deque([])
        q.append(root)
        nodeMap[root] = TreeNode(root.val)
        while len(q):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
                nodeMap[cur.left] = TreeNode(cur.left.val)
                nodeMap[cur].left = nodeMap[cur.left]
            if cur.right:
                q.append(cur.right)
                nodeMap[cur.right] = TreeNode(cur.right.val)
                nodeMap[cur].right = nodeMap[cur.right]
        return nodeMap[root]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
