#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from 
# he root node down to the farthest leaf node.



"""
Algo: DFS / Divide and Conquer
D.S.: Binary Tree

Solution:
1. Divide and Conquer
- if node is None, level counts 0
- if not None, max(leftChildDepth, rightChildDepth) + 1 (remember to add 1)

Time Complexity: O(N)

2. DFS (Traverse)
- No need to return anything in recursion function helper, each call update the
	current level
- Important that curDepth init as 1 (not 0)

Similar to "Minimum Depth of Binary Tree"

Corner cases:
- root is None
- only root itself
"""

class Solution1(object):
	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if root is None:
			return 0
		# Next line is core of divide and conquer
		return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1

class Solution2(object):
	# Remember to init depth here as 0
	maxDepth = 0
	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		def helper(node, curDepth):
			if node is None:
				return
			# Update private member varible self.depth
			# When get into a new level
			self.maxDepth = max(self.maxDepth, curDepth)
			
			helper(node.left, curDepth + 1)
			helper(node.right, curDepth + 1)
		
		helper(root, 1)
		return self.depth


# Test Cases
if __name__ == "__main__":
	solution = Solution()