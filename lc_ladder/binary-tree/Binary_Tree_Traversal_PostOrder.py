#!/usr/bin/python

# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

"""
Algo: DFS
D.S.: Binary Tree

Solution:
1.Recursion -- refer to illustration
2.Iteration -- Important yet complicate, memorize it

Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
	def postorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		if root is None:
			return res
		
		top = root
		def helper(res, top):
			# left, right, mid
			if top is None:
				return
			helper(res, top.left)
			helper(res, top.right)
			res.append(top.val)
			
		helper(res, top)
		return res

class Solution2(object):
	def postorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		if root is None:
			return res

		# stack saves nodes in order of root, right, left
		# when pop, the order is as post-order
		stack = [root]
		# keep track of previously poped node
		# if a node's child is prev travelled
			# if left child, means top has no right child, otherwise right child should be the top
			# if right child, means top's children all handled, time to pop top
        # init of travel should be a random TreeNode
        	# cannot do travelled = None, since None is a singleton, making it
        	# the same if a node has no left child then top.left == travelled
        travelled = TreeNode(0)
        while len(stack):
        	# each loop top is the LAST element of stack
            top = stack[-1]
            # case: time to handle top
            # - top has no children
            # - top's children are handled
            if (top.left is None and top.right is None) or \
                (top.left == travelled) or (top.right == travelled):
                res.append(top.val)
                travelled = top
                stack.pop()
            # case: top has children
            else:
                if top.right:
                    stack.append(top.right)
                if top.left:
                    stack.append(top.left)
        return res

# Test Cases
if __name__ == "__main__":
	solution = Solution()
