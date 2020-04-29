#! /usr/local/bin/python3

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Example
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
# between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

"""
Algo: Divide-Conquer
D.S.:

Solution:
Time Complexity: O(N), where NN is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.
Space Complexity: O(N). This is because the maximum amount of space utilized by the recursion stack would be NN since the height of a skewed binary tree could be NN.


Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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

# Test Cases
if __name__ == "__main__":
    solution = Solution()
