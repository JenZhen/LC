#! /usr/local/bin/python3

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Example
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q
# as descendants (where we allow a node to be a descendant of itself).”
#
# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
"""
Algo: BST Search
D.S.:

Solution:
Time Complexity: O(N), where N is the number of nodes in the BST.
Could be the height of tree. In the worst case we might be visiting all the nodes of the BST.

Space Complexity: O(N).
This is because the maximum amount of space utilized by the recursion stack would be NN since the height of a skewed BST could be NN.


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
        # root, p, q are not None and in the tree
        cur = root
        minval = min(p.val, q.val)
        maxval = max(p.val, q.val)
        while cur:
            if minval <= cur.val <= maxval:
                return cur
            elif cur.val < minval:
                cur = cur.right
            else:
                cur = cur.left
        return cur
# Test Cases
if __name__ == "__main__":
    solution = Solution()
