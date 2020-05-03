#! /usr/local/bin/python3

# https://leetcode.com/problems/longest-univalue-path/submissions/
# Example
# Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
# The length of path between two nodes is represented by the number of edges between them.
# Example 1:
# Input:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# Output: 2
#
# Example 2:
# Input:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output: 2
# Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""
Algo: Divide and Conquer
D.S.:

Solution:
Time: O(N) -- # of node
Space: O(H) -- height of tree

Corner cases:
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        self.dfs(root)
        return self.res - 1

    def dfs(self, node):
        if not node: return 0
        left_length = self.dfs(node.left)
        right_length = self.dfs(node.right)
        cur_length = 1
        cur_single_length = 1
        if node.left and node.left.val == node.val:
            cur_length += left_length
            cur_single_length = max(cur_single_length, left_length + 1)
        if node.right and node.right.val == node.val:
            cur_length += right_length
            cur_single_length = max(cur_single_length, right_length + 1)
        self.res = max(self.res, cur_length)

        return cur_single_length


# Test Cases
if __name__ == "__main__":
    solution = Solution()
