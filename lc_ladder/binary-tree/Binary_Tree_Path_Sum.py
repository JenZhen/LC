#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/path-sum/description/
# Given a binary tree and a sum, determine if the tree 
# has a root-to-leaf path such that adding up all the values along the path equals the given sum

"""
Algo: Divide-and-Conquer
D.S.: Binary Tree

Core variations of this problems:
- Does it have?
- How many does it have?
- What are they?

Solution1:
root hasPathSum <==>
	if root is leaf, root.val == sum
	if not leaf, root.left or root.right hasPathSum at sum - root.val
Solution1_1:
use classical dfs template in "Binary Tree Paths"

FollowUp1:
https://leetcode.com/problems/path-sum-ii/description/
Return the a list of paths

Corner cases:
"""

class Solution1(object):
	# Note, it's bad use sum, a built-in function as a variable
	# after this, sum cannot refer to a function anymore
	def hasPathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		if root is None:
			return False
		if not root.left and not root.right:
			return root.val == sum
		else:
			return self.hasPathSum(root.left, sum - root.val) or \
					self.hasPathSum(root.right, sum - root.val)


class Solution1_1(object):
	def hasPathSum(self, root, target):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		def dfs(node, res, path, target):
			path.append(node.val)
			# subSum += node.val 
			if node.left is None and node.right is None and sum(path) == target:
				# Each time find target push in
				# a bit waste of space
				res.append(target)
			if node.left:
				dfs(node.left, res, path, target)
			if node.right:
				dfs(node.right, res, path, target)
			path.pop()
			return
		
		res = []
		path = []
		if root is None:
			return False
		
		dfs(root, res, path, target)
		if len(res):
			return True
		else:
			return False

class Solution1_2(object):
	def hasPathSum(self, root, target):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		if root is None:
			return False
		# dfs records how many satisfying paths it has
		# Compared with 1_1 save much space for path[] and res[]
		numPath = self.dfs(root, target)
		return True if numPath != 0 else False
	
	def dfs(self, node, target):
		res = 0
		if node is None:
			return res
		if node.left is None and node.right is None and node.val == target:
			res += 1
		res += self.dfs(node.left, target - node.val)
		res += self.dfs(node.right, target - node.val)
		return res
		
class Solution_FollowUp(object):
	def pathSum(self, root, target):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: List[List[int]]
		"""
		
		def dfs(node, res, path, target):
			if node is None:
				return
			path.append(node.val)
			if node.left is None and node.right is None and node.val == target:
				# Important to have a deep copy of path
				# otherwise res = [[],[],[]]
				res.append(copy.deepcopy(path))
			dfs(node.left, res, path, target - node.val)
			dfs(node.right, res, path, target - node.val)
			path.pop()
			return
			
		res = []
		path = []
		if root is None:
			return res
		dfs(root, res, path, target)
		return res


# Test Cases
if __name__ == "__main__":
	solution = Solution()