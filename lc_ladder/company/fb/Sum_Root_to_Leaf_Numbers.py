#! /usr/local/bin/python3

# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Example
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:
#
# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
"""
Algo: Divide and Conquer
D.S.:

Solution:
Time: O(N) -- all nodes
Space: O(H) -- stack height, TBD
Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        res_list = self.dfs(root)
        print(res_list)
        return sum([int(x) for x in res_list])

    def dfs(self, node):
        if not node:
            return None
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if not left and not right:
            return [str(node.val)]

        node_list = []
        if left:
            for s in left:
                node_list.append(str(node.val) + s)
        if right:
            for s in right:
                node_list.append(str(node.val) + s)
        return node_list
# Test Cases
if __name__ == "__main__":
    solution = Solution()
