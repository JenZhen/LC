#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/inorder-successor-in-bst/
# Example
# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
#
# The successor of a node p is the node with the smallest key greater than p.val.
#
# Example 1:
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the answer is null.
#
# Note:
#
# If the given node has no in-order successor in the tree, return null.
# It's guaranteed that the values of the tree are unique.
"""
Algo: Tree-Iteration
D.S.: Binary Tree

Solution:
Time Complexity: O(N)
Space Complexity: O(N)

Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

       # 1. if successor in p's right subtree
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        # 2. if successor in p's upper node
        import sys
        stack = []
        inorder = -sys.maxsize
        cur_node = root
        while stack or cur_node:

            # 1. from cur_node trace to left most node
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left

            # 2. now cur_node is the min of the stack node
            cur_node = stack.pop()
            if inorder == p.val:
                # inorder tracks value before the min of the stack
                return cur_node
            # update inorder to be cur_node's value
            inorder = cur_node.val

            # 3. move to cur_node's right child, if no, will continue pop from stack
            cur_node = cur_node.right
        return None


# Test Cases
if __name__ == "__main__":
	solution = Solution()
