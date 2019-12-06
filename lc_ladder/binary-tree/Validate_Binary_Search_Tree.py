#!/usr/bin/python

import BinaryTree
# https://leetcode.com/problems/validate-binary-search-tree/description/
# Given a binary tree check if it is a valid binary search tree.

"""
Algo: Divide-and-Conquer / DFS
D.S.: Binary Tree

Solution:
1. Divide-and-Conquer
Conditon:
1. root meets min < root.val < max and
2. children are validated as well

Time Complexity: O(N) -- N is number of nodes
c
Corner cases:
- child cannot be of the same value of parent

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    import sys
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, -sys.maxsize, sys.maxsize)

    def helper(self, node, low, high):
        if not node:
            return True
        return low < node.val < high and \
               self.helper(node.left, low, node.val) and \
               self.helper(node.right, node.val, high)

# Test Cases
if __name__ == "__main__":
	solution = Solution()
