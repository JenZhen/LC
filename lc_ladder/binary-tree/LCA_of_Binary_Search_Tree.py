#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

"""
Algo: Binary Search
D.S.: Binary Search Tree

Solution1:
Time complexity: O(logN)
Limitation: doesn't work if nodes not in the same root tree

Solution2: can handle if not in same trees
Time complexity: O(N)
TBR by persalized test cases
- Step1, like solution use BST property to find subtree root
	This function is recursivedly called until p and q are on two sides of root
	in solution1, process stops here and return root
	in solution2, need to proceeds to make sure both p and q are under this root
- Step2, similar to "LCA_Binary_Tree_I", need to recursively find two sides of
	root to check if p or q are there.
	No need to return "nodes" as "LCA_Binary_Tree_I" since step1 already narrows
	down the scope

Corner cases:
"""

class Solution1(object):
	def lowestCommonAncestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		if root is None:
			return None

		if root.val > p.val and root.val > q.val:
			return self.lowestCommonAncestor(root.left, p, q)
		elif root.val < p.val and root.val < q.val:
			return self.lowestCommonAncestor(root.right, p, q)
		else:
			return root


class Solution2(object):
	def lowestCommonAncestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""

		if root is None or p is None or q is None:
			return None
		return self.findSubTree(root, p, q)

	def findSubTree(self, node, p, q):
		# return node
		if node.val > p.val and node.val > q.val:
			return self.findSubTree(node.left, p, q)
		elif node.val < p.val and node.val < q.val:
			return self.findSubTree(node.right, p, q)
		else:
			pFound, qFound = \
				self.findNode(node, p, q)
			if pFound and qFound:
				return node
			else:
				return None

	def findNode(self, node, p, q):
		# return if pFound, qFound
		if node is None:
			return False, False

		leftPFound, leftQFound = self.findNode(node.left, p, q)
		rightPFound, rightQFound = self.findNode(node.right, p, q)

		pFound = leftPFound or rightPFound or node == p
		qFound = leftQFound or rightQFound or node == q

		return pFound, qFound


# Test Cases
if __name__ == "__main__":
	solution = Solution()
