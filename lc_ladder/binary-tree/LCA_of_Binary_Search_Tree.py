#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Example
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between
#two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
"""
Algo: DFS, Divide-and-Conquer
D.S.: Binary Tree

Solution:
Complexity: O(logN) height of tree worst O(N)

Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # root, p, q are not None and in the tree
        cur = root
        minval = min(p.val, q.val)
        maxval = max(p.val, q.val)
        while cur:
            if cur.val < minval:
                cur = cur.right
            elif cur.val > maxval:
                cur = cur.left
            else:
                return cur
        return cur


# Test Cases
if __name__ == "__main__":
	solution = Solution()
