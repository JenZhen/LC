#! /usr/local/bin/python3

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Example
# Given a binary tree, flatten it to a linked list in-place.
# For example, given the following tree:
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
"""
Algo: Divide Conquer
D.S.:

Solution:
Time: O(N)
Space: O(N)

Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        lefttail = self.flatten(root.left)
        righttail = self.flatten(root.right)
        if lefttail:
            lefttail.right = root.right
            root.right = root.left
            root.left = None
        if righttail: return righttail
        elif lefttail: return lefttail
        else: return root

# Test Cases
if __name__ == "__main__":
    solution = Solution()
