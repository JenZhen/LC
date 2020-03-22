#!/usr/bin/python

# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
# Example

"""
Algo: DFS
D.S.: Binary Tree

Solution:
1. Recursion -- refer to illustration
2. Iteration *** Important

Time Complexity: O(n), n is number of nodes

Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
	def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		if root is None:
			return res
		def helper(res, root):
			if root is None:
				return
			res.append(root.val)
			helper(res, root.left)
			helper(res, root.right)
		helper(res, root)
		return res

class Solution2(object):
	def preorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		if root is None:
			return res
		top = root
		stack = [None] #Sentinal, when top reads None meaning all elements read
		while top:
			res.append()
			if top.right:
				stack.append(top.right) #Save right child then left
			if top.left:
				stack.append(top.left)
			top = stack.pop()

# Test Cases
if __name__ == "__main__":
	solution1 = Solution()
