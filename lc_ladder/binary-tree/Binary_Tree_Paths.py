#!/usr/bin/python
import BinaryTree
# Given a binary tree, return all root-to-leaf paths.
# For example, given the following binary tree:
#    1
#  /   \
# 2     3
#  \
#   5
# Return ["1->2->5", "1->3"]
# https://leetcode.com/problems/binary-tree-paths/description/

"""
Algo: DFS
D.S.: Binary Tree

Core variations of this problems:
- Does it have?
- How many does it have?
- What are they?

Solution:
Classic DFS questions, template, very important
1. recursively handle subres and push to res when necessary
	res in each recursion level is different
2. Use a stack to control path
	DFS template, memorize it.

FollowUp1:
How many paths does this tree have?

Keys: how to handle the first element

Corner cases:
"""

class Solution1(object):
	def binaryTreePaths(self, root):
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		res = []
		if root is None:
			return res
		self.helper(root, res, "")
		return res

	def helper(self, node, res, subres):
		if subres == "":
			subres = str(node.val)
		else:
			subres = subres + "->" + str(node.val)

		if node.left is None and node.right is None:
			# note here no need to deep-copy
			res.append(subres)
		if node.left:
			self.helper(node.left, res, subres) # this subres is same with node.right subres (since it's string type)
		if node.right:
			self.helper(node.right, res, subres)
		# this "return is optional"
		return

class Solution1_1:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        res = []
        path = []
        if not root:
            return res
        self.helper(res, path, root)
        return res

    def helper(self, res, path, node):
        path.append(node.val)
        if node.left is None and node.right is None:
            res.append("->".join([str(c) for c in path]))
        if node.left:
            self.helper(res, path, node.left)
            path.pop() # is using path, need to pop latest, it's passing reference to recusion
        if node.right:
            self.helper(res, path, node.right)
            path.pop()

class Solution2(object):
	def binaryTreePaths(self, root):
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		res = []
		if root is None:
			return res
		self.helper(root, res, [])
		return res

	def helper(self, node, res, stack):
		# stack is stack of string ver of node.val
		stack.append(str(node.val))
		if node.left is None and node.right is None:
			res.append('->'.join(stack))
		if node.left:
			self.helper(node.left, res, stack)
		if node.right:
			self.helper(node.right, res, stack)
		# Important
		# After a node is recgonized as leaf and pushed in stack
		# or it's both children are handled
		# Meaning path thru this node is done, pop it.
		stack.pop()
		# This "return" is optional
		return

	# Alternative way of dfs function, same as above
	# Most suggested way!!!!
	def dfs(self, node, res, path):
		# stack is stack of node.val
		if node is None:
			return
		path.append(str(node.val))
		if node.left is None and node.right is None:
			res.append('->'.join(path))
		self.helper(node.left, res, path)
		self.helper(node.right, res, path)
		path.pop()
		return

class Solution_FollowUp_1(object):
	def binaryTreePaths(self, root):
		"""
		:type root: TreeNode
		:rtype: List[str]
		"""
		res = 0
		if root is None:
			return res
		if node.left is None and if node.right is None:
			res += 1
		res += self.binaryTreePaths(node.left)
		res += self.binaryTreePaths(node.right)
		return res

# Test Cases
if __name__ == "__main__":
	solution = Solution()
