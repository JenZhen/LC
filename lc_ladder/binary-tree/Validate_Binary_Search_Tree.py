#!/usr/bin/python

import BinaryTree
# https://leetcode.com/problems/validate-binary-search-tree/description/
# Given a binary tree check if it is a valid binary search tree.

"""
Algo: Divide and Conquer / DFS
D.S.: Binary Tree

Solution:
1. Divide and Conquer
Conditon:
1. root meets min < root.val < max and
2. children are validated as well

Corner cases:
- child cannot be of the same value of parent

"""
# tbd
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, min, max):
            if node is None:
                return True
            if min < node.val and node.val < max:
                return helper(node.left, min, node.val) and \
                       helper(node.right, node.val, max)
            else:
                return False

        import sys
        return helper(root, -sys.maxint, sys.maxint)

# Test Cases
if __name__ == "__main__":
	solution = Solution()
