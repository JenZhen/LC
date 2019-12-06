#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/path-sum-ii/description/
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


"""
Algo: DFS, Backtracking
D.S.: Binary Tree

Solution:
Solution 1 - 3
Time Complexity: O(N) -- each node visited once

Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_1:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        path = []
        self.helper(root, res, path, sum)
        return res

    def helper(self, node, res, path, sum):
        path.append(node.val)
        if not node.left and not node.right:
            # if leaf node
            if node.val == sum:
                res.append(path[:])
			# return is optional
        if node.left:
            self.helper(node.left, res, path, sum - node.val)
            path.pop()

        if node.right:
            self.helper(node.right, res, path, sum - node.val)
            path.pop()

class Solution_2:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        path = []
        self.helper(root, res, path, sum)
        return res

    def helper(self, node, res, path, sum):
        path.append(node.val)
        if not node.left and not node.right:
            if node.val == sum:
                res.append(path[:])
			# pop leaf node and return are optional
			# pop leaf
            path.pop()
            return # this return is required, otherwise the pop at the end may pop empty list
        if node.left:
            self.helper(node.left, res, path, sum - node.val)
        if node.right:
            self.helper(node.right, res, path, sum - node.val)
		# pop current level node, after its left and right children completed
        path.pop()

class Solution_3:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        path = []
        self.helper(root, res, path, sum)
        return res

    def helper(self, node, res, path, sum):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:
            if node.val == sum:
                res.append(path[:])
			path.pop()
			return
        self.helper(node.left, res, path, sum - node.val)
        self.helper(node.right, res, path, sum - node.val)
        path.pop()

class Solution_3_1:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        path = []
        self.helper(root, res, path, sum)
        return res

    def helper(self, node, res, path, sum):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:
            if node.val == sum:
                res.append(path[:])
        self.helper(node.left, res, path, sum - node.val)
        self.helper(node.right, res, path, sum - node.val)
        path.pop()

# Test Cases
if __name__ == "__main__":
	solution = Solution()
