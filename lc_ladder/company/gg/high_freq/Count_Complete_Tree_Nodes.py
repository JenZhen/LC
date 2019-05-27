#! /usr/local/bin/python3

# https://leetcode.com/problems/count-complete-tree-nodes
# Example
# Given a complete binary tree, count the number of nodes.
#
# Note:
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
# Example:
#
# Input:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# Output: 6
"""
Algo:
D.S.: complete binary tree

Solution:
1. Time: O(logN * logN)
2. dfs divide conquer = O(N)

Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def depth(root):
            if not root: return 0
            return 1 + depth(root.left)


        if not root: return 0
        lh = depth(root.left)
        rh = depth(root.right)
        if lh == rh:
            return 1 + (2**lh - 1) + self.countNodes(root.right)
        else:
            return 1 + (2**rh - 1) + self.countNodes(root.left)


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
