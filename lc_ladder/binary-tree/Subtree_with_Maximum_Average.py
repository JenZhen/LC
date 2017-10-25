#!/usr/bin/python
import BinaryTree

# Given a binary tree, find the subtree with maximum average. 
# Return the root of the subtree.
# http://www.jiuzhang.com/solution/subtree-with-maximum-average/

"""
Algo: Divide Conquer
D.S.: Binary Tree

Solution:
Divide and Conquer to calculate 2 metrics
	- sumValue
	- sumNode
Keep a global maxNode(root) and update when needed

Note: In the context, where global maxNode and maxAvg needs to be updated,
	it is not proper to make helper as enclosure within findSubtree2, unless
	maxNode is passed in each helper recursion (not necessary)

Time Complexity: O(N) each node is examed

Corner cases:
"""

class Solution:
	# @param {TreeNode} root the root of binary tree
	# @return {TreeNode} the root of the maximum average of subtree
	
	# Define as member variables
	maxNode = None
	maxAvg = 0.0 # defined as float

	def findSubtree2(self, root):
		# Write your code here
		if root is None:
			return None
		# rootVal, rootNode = self.helper(root)
		# It has return value which is root sumValue and sumNode
		# We don't care, we only care self.maxNode
		self.helper(root)
		return maxNode

	# +++++++++++++ helper function starts ++++++++++++
	def heler(self, node):
		# recursively return sumValue and sumNode
		# update globaly defined maxNode and maxAvg

		if root is None:
			# return sumValue and sumNode
			return 0, 0
		# recursive get left/right sumVal and sumNode
		leftValue, leftNode = self.helper(node.left)
		rightValue, rightNode = self.helper(node.right)

		# add up left and right to get current node sumVal and sumNode
		sumValue = leftValue + rightValue + node.val
		sumNode = leftNode + rightNode + 1

		# Compare with global tracked avg and node, update if needed
		# Convert to floating to precise comparison
		avg = sumValue * 0.1 / sumNode 
		if self.maxNode is None or avg > self.maxAvg:
			self.maxNode = node
			self.maxAvg = avg

		return sumValue, sumNode
	# +++++++++++++ helper function ends ++++++++++++


# Test Cases
if __name__ == "__main__":
	solution = Solution()
