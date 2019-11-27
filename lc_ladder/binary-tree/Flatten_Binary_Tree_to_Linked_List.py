#!/usr/bin/python
import BinaryTree
# Requirement
# Example

"""
Algo: DFS/Divide-and-Conquer/Traverse/Iteration
D.S.: Binary Tree

Solution:
1. Divide-and-Conquer
- Given root, get left child tree right-most end node and right child tree
- If left child tree right most node non-None, connect to right.child
- return the right-most node of root (check right child then left child, if both None return root)

1.1 Divide-and-Conquer (no helper)
- Same as soluton1, recursion function don't return anything

Time Complexity: O(N) all nodes are visited
Space Complexity: O(1)

2. Iteration -- follow PreOrder iteration template
Time Complexity: O(N)
Space Complexity: worst case O(N) all lined up on left child side

Corner cases:
- Only root one element
"""

class Solution1(object):
	def flatten(self, root):
		"""
		:type root: TreeNode
		:rtype: void Do not return anything, modify root in-place instead.
		"""
		# Note: rtype require not return anything, hence needs a helper
		self.helper(root)
	
	def helper(self, root):
		if root is None:
			return None
		leftEnd = self.flatten(root.left)
		rightEnd = self.flatten(root.right)
		# connect left end to right child
		if leftEnd:
			leftEnd.right = root.right
			root.right = root.left
			root.left = None
		if rightEnd:
			return rightEnd
		elif leftEnd:
			return leftEnd
		else:
			return root

class Solution1_1(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        
        # connect left sub tree to right child
        # need to find right-most of left-sub tree
        runner = root.left
        # remember to check if root.left (runner) is None
        if runner:
            while runner.right:
                runner = runner.right
            runner.right = root.right
            root.right = root.left
            root.left = None
        return

class Solution2(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        top = root
        stack = [None]
        
        while top:
        	# save right child then left child
            if top.right:
                stack.append(top.right)
            if top.left:
                stack.append(top.left)
            # connect
            # new right child is just pushed left child
            top.right = stack[-1]
            # remember to clean left child
            top.left = None
            # after last of stack is fitted in new position,
            # top update and remove from stack
            top = stack.pop()

# Test Cases
if __name__ == "__main__":
	solution = Solution()