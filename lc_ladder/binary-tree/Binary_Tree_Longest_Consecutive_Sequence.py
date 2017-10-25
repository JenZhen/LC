#!/usr/bin/python
import BinaryTree
# http://www.jiuzhang.com/solution/binary-tree-longest-consecutive-sequence/
# Example
#      1
#    /  \
#   2    5
#  / \    \
# 1   3    2
#    / \  /
#   5   4 5
# Return 4 (1,2,3,4)
"""
Algo: Divide and Conquer
D.S.: Binary Tree

Solution:
Starting from any node(not have to be root), ends any node
Goes from parent to child
Similar to "Binary Tree Maximum Path Sum"

FollowUp1:
http://www.jiuzhang.com/solution/binary-tree-longest-consecutive-sequence-ii/
Start/ends from any node
Goes from child or parent
#      2
#    /  \
#(1)1    3(2)
# 2 as root leftup(LU)->root->rightdown(RD)
#      2
#    /  \
#(3)3    1(4)
# 2 as root rightup(RU)->root->leftdown(LD)
Need to calculate 2 types of value at root 2
- 2 as the end of single path, could come from either left or right child
	- Up direction, including (1) Left Up(LU) and (4) Right Up(RU)
		up value init as 0 (may not have an up path)
	- Down direction, including (2) Right Down(RD) and (3) Left Down(LD)
		down value init as 0 (may not have a down path)
- 2 as turning point connecting path from both childre, aka 2 as root, the max length it has
	- curLen = down + up + 1

FollowUp1:
http://www.jiuzhang.com/solution/binary-tree-longest-consecutive-sequence-iii/
Based on FollowUp1, change from binary tree to k-chidren tree
node.children is an array of child tree nodes

Corner cases:
"""

class Solution(object):
	maxLength = 0
	def longestConsecutive(self, root):
		"""
		:type root: TreeNodd
		:rtype: number
		"""
		def helper(node):
			if node is None:
				return 0
			leftLen = helper(node.left)
			rightLen = helper(node.right)
			curLen = 1
			if leftLen != 0 and node.left.val - 1 = node.val:
				curLen = max(curLen, leftLen + 1)
			if rightLen != 0 and node.right.val - 1 = node.val:
				curLen = max(curLen, rightLen + 1)
			self.maxLength = max(self.maxLength, curLen)

		helper(root)
		return self.maxLength

class Solution_FollowUp1:
	# @param {TreeNode} root the root of binary tree
	# @return {int} the length of the longest consecutive sequence path
	def longestConsecutive2(self, root):
		# Write your code here
		def helper(node):
			# return
			# maxLen: when node is turning point
			# upLen: up direction single path sent to node's parent
			# downLen: down direction single path sent to node's parent
			if node is None:
				return 0, 0, 0

			leftLen, leftUp, leftDown = helper(node.left)
			rightLen, rightUp, rightDown = helper(node.right)

			up, down = 0, 0
			if node.left is not None and node.left.val + 1 = node.val:
				# (1)
				up = max(up, leftUp + 1)
				# alternatively up = leftUp + 1, first time update up
				# format concern to be consistent with following
			if node.right is not None and node.right.val + 1 = node.val:
				# (4)
				up = max(up, rightUp + 1)
			if node.right is not None and node.right.val - 1 = node.val:
				# (2)
				down = max(down, rightDown + 1)
			if node.left is not None and node.left.val - 1 = node.val:
				down = max(down, leftDown + 1)

			curLen = up + down + 1
			maxLen = max(curLen, max(leftLen, rightLen))
			return maxLen, up, down

		maxLen, up, down = helper(root)
		# Alternatively can use "throw-away" variables
		# maxLen, _, _, = helper(root)
		# meaning 2nd, 3rd return variables are ignored
		return maxLen

class Solution_FollowUp2:
	# @param {MultiTreeNode} root the root of k-ary tree
	# @return {int} the length of the longest consecutive sequence path
	def longestConsecutive3(self, root):
		# Write your code here
		def helper(node):
			# return
			# maxLen: when node is turning point, iterate all children's maxLen, then compare witch case of node as turning point
			# upLen: up direction single path sent to node's parent
			# downLen: down direction single path sent to node's parent
			maxLen, up, down = 0, 0, 0
			if node is None:
				return maxLen, up, down
			for child in node.children:
				childMaxLen, childUp, childDown = \
					helper(node.child)
				# Update maxLen to pick the larget amoung children
				maxLen = max(maxLen, childMaxLen)
				if child is not None and child.val + 1 = node.val:
					up = max(up, childUp + 1)
				if child is not None and child.val - 1 = node.val:
					down = max(down, childDown + 1)
				maxLen = max(maxLen, up + down + 1)

			return maxLen, up, down


# Test Cases
if __name__ == "__main__":
	solution = Solution()
