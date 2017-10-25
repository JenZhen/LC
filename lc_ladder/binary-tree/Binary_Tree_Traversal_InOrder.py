#!/usr/bin/python

# https://leetcode.com/problems/binary-tree-inorder-traversal/description

"""
Algo: DFS
D.S.: Binary Tree

Solution:
1. Recursion -- refer to illustration
2. Ireration *** Important

Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        top = root
        def helper(res, top):
            if not top:
                return
            helper(res, top.left)
            res.append(top.val)
            helper(res, top.right)
            
        helper(res, top)
        return res


class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root is None:
            return res
        top = root
        stack = [] # stack used for saving root and it's right child
        while top or len(stack) != 0:
        	# top non-None meaning needs to seach left first
            if top:
            	# tmpl save top in stack
                stack.append(top)
                # move to top's left child
                top = top.left
            # top is None while stack non-empty, meaning left till None
            # Should retrieve top back (stack.pop()) then move right child
            else:
                top = stack.pop()
                res.append(top.val)
                top = top.right         
        return res

# Test Cases
if __name__ == "__main__":
	solution = Solution()
