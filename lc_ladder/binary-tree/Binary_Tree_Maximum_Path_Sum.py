#!/usr/bin/python
import BinaryTree

# Given a binary tree, find the maximum path sum from root.
# The path may end at any node in the tree and contain at least 
# one node in it.
# Start from root, ends anywhere
# http://www.jiuzhang.com/solution/binary-tree-maximum-path-sum-ii/
 
"""
Algo: DFS
D.S.: Binary Tree

Solution:

Follow Up:
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

Corner cases:
2 -- -1
-2 -- 1
"""
class Solution:
    """
    @param root the root of binary tree.
    @return an integer
    """
    def maxPathSum2(self, root):
        # Write your code here
    	if root is None:
    		return 0
    	leftMax = self.maxPathSum2(root.left)
    	rightMax = self.maxPathSum2(node.right)
    	return root.val + max(max(leftMax, 0), rightMax)


class Solution_FollowUp1_1(object):
	import sys
	globalMax = -sys.maxint
	def maxPathSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		def helper(node):
			# find max path sum with node as root
			if node is None:
				return 0
			curSum = node.val
			leftMaxSum = helper(node.left)
			rightMaxSum = helper(node.right)
			if leftMaxSum > 0:
				curSum += leftMaxSum
			if rightMaxSum > 0:
				curSum += rightMaxSum
			self.globalMax = max(curSum, self.globalMax)
			return node.val + max(max(0, leftMaxSum), rightMaxSum)
			
		if root is None:
			return 0
		helper(root)
		return self.globalMax


class Solution_FollowUp1_2(object):
	def maxPathSum(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		def helper(node):
			# find max path sum with node as root
			# return singleSum: node as root single path max sum 
			#        multSum: node as turning point, max sum
			#                 (including node and its children's singleSum)
			if node is None:
				return 0, 0
			multSum = node.val
			leftS, leftM = helper(node.left)
			rightS, rightM = helper(node.right)
			if leftS > 0:
				multSum += leftS
			if rightS > 0:
				multSum += rightS
			singleSum = node.val + max(max(0, leftS), rightS)
			return singleSum, multSum

		if root is None:
			return 0
		sSum, mSum = helper(root)
		return mSum



# Test Cases
if __name__ == "__main__":
	solution = Solution()