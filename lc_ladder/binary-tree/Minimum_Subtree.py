#!/usr/bin/python
import BinaryTree

# http://www.jiuzhang.com/solution/minimum-subtree/
# Given a binary tree, find the subtree with minimum sum.
# Return the root of the subtree.

"""
Algo: Divide and Conquer
D.S.: Binary Tree

Solution:
Recursively calculate sum of each subtree.
Update global minSum when necessary.

Similar to;
This is a sub-problem of "Subtree with Maximum Average"
Corner cases:
"""

class Solution:
	# @param {TreeNode} root the root of binary tree
	# @return {int} the minimun weight node

	# An alternative way to init min/max other than float('inf')
	# import sys
    # minumun_weight = sys.maxint
	minSum = 0
	minNode = None

	def findSubtree(self, root):
		# Write your code here
		if root is None:
			return None
		# Don't care return of self.helper(root)
		self.helper(root)
		return self.minNode

	def helper(self, node):
		# return each node's sum
		if node is None:
			# when None node, return 0(weight 0)
			return 0
		leftSum = self.helper(node.left)
		rightSum = self.helper(node.right)
		nodeSum = leftSum + rightSum + node.val

		if minNode is None or nodeSum < minSum:
			minSum = nodeSum
			minNode = node
		# don't forget to return nodeSum
		return nodeSum

# Test Cases
if __name__ == "__main__":
	solution = Solution()
