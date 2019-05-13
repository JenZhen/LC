#! /usr/local/bin/python3

# https://leetcode.com/problems/flip-equivalent-binary-trees/
# Example
# For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
#
# A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
#
# Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.
#
#
#
# Example 1:
#
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.
"""
Algo: divide-conquer,
D.S.: binary tree

Solution:


Corner cases:
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1: return not root2
        if not root2: return not root1
        if root1.val != root2.val:
            return False
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))

# Test Cases
if __name__ == "__main__":
    solution = Solution()
