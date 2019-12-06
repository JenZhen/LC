#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/find-mode-in-binary-search-tree/submissions/
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# For example:
# Given BST [1,null,2,2],
#
#    1
#     \
#      2
#     /
#    2
#
#
# return [2].
#
# Note: If a tree has more than one mode, you can return them in any order.
#
# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

"""
Algo: DFS, traversal
D.S.: Binary Tree

Solution:
Time Complexity: O(N) -- each node has to be visited once.
Space Complexity: O(N)

Corner cases:
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.cache = {}
        self.helper(root)
        res = []
        max_curr = 0
        for key, val in self.cache.items():
            if val > max_curr:
                res = [key]
                max_curr = val
            elif val == max_curr:
                res.append(key)
        return res

    def helper(self, node):
        if not node:
            return
        self.cache[node.val] = self.cache.get(node.val, 0) + 1
        self.helper(node.left)
        self.helper(node.right)

# Test Cases
if __name__ == "__main__":
	solution = Solution()
