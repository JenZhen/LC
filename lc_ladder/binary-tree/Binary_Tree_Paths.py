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
Algo: DFS, Divide-and-Conquer
D.S.: Binary Tree

Core variations of this problems:
- Does it have?
- How many does it have?
- What are they?

Solution_0: Divide-and-Conquer
Time Complexity: O(N) -- N is number of nodes
Space Complexity: ## TODO:

Solution_1 to Solution_4: DFS traversal (Backtracking)
Time Complexity: O(N) -- N is number of node
Space Complexity: ## TODO:

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

class Solution_0:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
		# 返回以当前节点为root所有的paths
        if not root:
			# null node 返回[]
            return []
        if not root.left and not root.right:
            # at leaf node, return value built from leaves up to root
			# 叶节点返回自己
            return [str(root.val)]

		# 左孩子为root时的所有paths
        leftPaths = self.binaryTreePaths(root.left)
		# 右孩子为root时的所有paths
        rightPaths = self.binaryTreePaths(root.right)

		# 合并左右的paths 把当前node加在前面
        curNodePath = []
        for path in rightPaths + leftPaths:
			# 巧用[]不会进入这层循环
            curNodePath.append(str(root.val) + '->' + path)
        return curNodePath

class Solution_1:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        path = []
        self.helper(root, res, path)
        return res

    def helper(self, node, res, path):
		# append current level node
        path.append(node.val)
        if not node.left and not node.right:
            res.append('->'.join([str(ele) for ele in path]))
            return # return optional
        if node.left:
            self.helper(node.left, res, path)
			# pop node.left, path ends with current level node
            path.pop()
        if node.right:
            self.helper(node.right, res, path)
			# pop node.right, path ends with current level node
            path.pop()

class Solution_2:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        path = []
        self.helper(root, res, path)
        return res

    def helper(self, node, res, path):
		# append current level node
        path.append(node.val)
        if not node.left and not node.right:
            res.append('->'.join([str(ele) for ele in path]))
			# pop leaf, which is current level node
            path.pop()
            return # must have this return
        if node.left:
            self.helper(node.left, res, path)
        if node.right:
            self.helper(node.right, res, path)
		# pop current level node
        path.pop()

class Solution_3:
	# same as Solution_2
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        path = []
        self.helper(root, res, path)
        return res

    def helper(self, node, res, path):
        if node is None:
            return
		# path append current level node
        path.append(str(node.val))
        if node.left is None and node.right is None:
            res.append('->'.join(path))
        self.helper(node.left, res, path)
        self.helper(node.right, res, path)
		# path pop current level node
        path.pop()

class Solution_3_1:
	# same as Solution_2
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        path = []
        self.helper(root, res, path)
        return res

    def helper(self, node, res, path):
        if node is None:
            return
		# path append current level node
        path.append(str(node.val))
        if node.left is None and node.right is None:
            res.append('->'.join(path))
			path.pop()
			return # this return is a must
        self.helper(node.left, res, path)
        self.helper(node.right, res, path)
		# path pop current level node
        path.pop()

class Solution_4:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
		# append current level node to path before recursion level starts
        path = [root.val]
        self.helper(root, res, path)
        return res

    def helper(self, node, res, path):
		# path ends with current level node
        if node.left is None and node.right is None:
            res.append('->'.join(str(ele) for ele in path))
        if node.left:
			# path append node.left before recursion of node.left
            path.append(node.left.val)
            self.helper(node.left, res, path)
			# path pop node.left, ends with current level node
            path.pop()
        if node.right:
			# path append node.right before recursion of node.right
            path.append(node.right.val)
            self.helper(node.right, res, path)
			# path pop node.right, ends with current level node
            path.pop()

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
