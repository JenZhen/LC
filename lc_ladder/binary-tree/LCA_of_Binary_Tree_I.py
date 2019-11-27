#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# Given 1) Tree root, 2) two other tree nodes
# Find the LCA

"""
Algo: Divide-and-Conquer
D.S.: Binary Tree

Solution:
#     BF
#    /  \
#   BB   nG
#  / \    \
#AA  ED   nI
#    / \  /
#  nC  EE Hn
#  n n   nn
Given F, find LCA of A & E. (result B)

- When reaches A, node == A, return A to prev Level as leftNode of B
- When reaches C, leaf, both left/right of C return None, C returns None
	to prevLevel as leftNode of D
- When reaches D, leftNode returns None (from C), rightNode returns E (from E)
	take the non-None one return to prev level as rightNode of B
- When reaches B, both left and right are non-None return node B to pre level
- When search right side of F, all None
- When reaches F, left is B right is None return B

Limitation: cannot work if either of them not in the same tree
if in case 1 -- 2, where 1 is parent of 2, when reaches to 1 return back
2 will never to accessed, cannot tell if 2 is in this root tree. By default,
this algo assume 2 is under 1

Time Complexity: O(N)
Space Complexity: O(1)

A stright forward way:
1. traverse to find q, save path in an array,
2. do the same to find p
3. compare two arrays to find LCA
Time complexity: 2 * O(N)
Space complexity: 2 * O(N)

Follow-Up 1
# http://www.jiuzhang.com/solution/lowest-common-ancestor-iii/
# How to solve cases when two nodes not in same trees
Solution:
To solve previous question is limitation that in the process of iteration,
it cannot tell if node p or q has been found, this version should keep
extra return info of the recursion function to pass if pFound qFound in the
whole process of iteration.

Complexity: O(N)

Follow-Up 2
# http://www.jiuzhang.com/solution/lowest-common-ancestor-ii/
# What if node has pointer points at parent
# See "LCA of Binary Tree II"

Corner cases:
- None for inputs
- If inputs tree nodes locate in the same tree
- 1--2, p and q one of them is the root of another

"""

class Solution1(object):
	def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		# A,B 都在 root 为根的二叉树里, return lca(A,B)
        # 如果 A,B 都不在 root 为根的二叉树里, return None
        # 如果只有 A 在，return A
        # 如果只有 B 在，return B
        if root is None:
            return None
        if p is root or q is root:
            return root

        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        if left_lca and right_lca:
            return root
        elif left_lca:
            return left_lca
        elif right_lca:
            return right_lca
        else:
            return None

class Solution_Follow_Up_1(object):
	def lowestCommonAncestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		if root is None or p is None or q is None:
			return None
		pFound, qFound, node = self.helper(root, p, q)
		if pFound and qFound:
			return node
		return None

	def helper(self, node, p, q):
		# return type
		# pFound: boolean, if p node is found
		# pFound: bollean, if q node is found
		# node: TreeNode, previously found node passed up
		if node is None:
			return False, False, None

		# Divide
		leftFoundp, leftFoundq, leftNode = self.helper(node.left, p, q)
		rightFoundp, rightFoundq, rightNode = self.helper(node.right, p, q)

		# Conquer -- based on left right node result decide
		# what to return to upper level
		# pFound is True only it's been found in lower level in either
		# left or right subtrees or current node is p, same for node q
		pFound = leftFoundp or rightFoundp or node == p
		qFound = leftFoundq or rightFoundq or node == q

		# Don't forget this part!!!
		# Used when pFound: False, qFound: False, but node == p or node == q
		if node == p or node == q:
			return pFound, qFound, node

		# Both nonNone
		if leftNode and rightNode:
		# 	return True, True, node
			return pFound, qFound, node
		# Either is None
		elif leftNode:
			return pFound, qFound, leftNode
		elif rightNode:
			return pFound, qFound, rightNode
		# Both are None
		else:
		#	return False, False, None
			return pFound, qFound, None


# Test Cases
if __name__ == "__main__":
	solution = Solution()
