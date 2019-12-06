#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Example
# Given the root node of a binary search tree (BST) and a value to be inserted into the tree,
# insert the value into the BST. Return the root node of the BST after the insertion.
# It is guaranteed that the new value does not exist in the original BST.
# Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
# For example,
# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
# And the value to insert: 5
# You can return this binary search tree:
#
#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5
# This tree is also valid:
#
#          5
#        /   \
#       2     7
#      / \
#     1   3
#          \
#           4
"""
Algo: Tree-Iteration
D.S.: Binary Tree

Solution:
Time Complexity: O(N)
Space Complexity: O(1)

Corner cases:
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        pre = TreeNode(0)
        pre.left = root
        cur = root
        while cur:
            if cur.val > val:
                pre = cur
                cur = cur.left
            elif cur.val < val:
                pre = cur
                cur = cur.right
        if pre.val < val:
            pre.right = TreeNode(val)
        elif pre.val > val:
            pre.left = TreeNode(val)
        return root

# Test Cases
if __name__ == "__main__":
	solution = Solution()
