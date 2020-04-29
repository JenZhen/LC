#! /usr/local/bin/python3

# https://leetcode.com/problems/binary-tree-maximum-path-sum/submissions/
# Example
# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
# The path must contain at least one node and does not need to go through the root.
#
# Example 1:
#
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
# Example 2:
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42

"""
Algo: Divide-Conquer
D.S.:

Solution:

At node, it's path could be
- single 1) from left, 2) from right
- double from left + right + node.val

if from left < 0 then don't take it mark it as 0, same for from right
在node 能得到的最大path sum = double (left + right + node.val) --> 用来更新全局解

Time complexity: O(N) where N is number of nodes, since we visit each node not more than 2 times.
Space complexity: O(logN) We have to keep a recursion stack of the size of the tree height.

Similar:
687 Longest Univalue Path
543 Diameter of Binary Tree

Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):c
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -sys.maxsize
        _ = self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return 0

        l_res = max(self.helper(node.left), 0)
        r_res = max(self.helper(node.right), 0)

        by_node_path = node.val + l_res + r_res

        self.res = max(self.res, by_node_path)

        return node.val + max(l_res, r_res)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
