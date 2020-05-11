#! /usr/local/bin/python3

# https://leetcode.com/problems/count-univalue-subtrees/submissions/
# Example
# Given a binary tree, count the number of uni-value subtrees.
# A Uni-value subtree means all nodes of the subtree have the same value.
# Example :
# Input:  root = [5,1,5,5,5,null,5]
#
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
#
# Output: 4
"""
Algo:
D.S.:

Solution:

Time: O(N)
Space: O(H)
Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return True
        if not node.left and not node.right:
            self.res += 1
            return True
        is_uni = True
        if node.left:
            is_uni = self.dfs(node.left) and is_uni and node.val == node.left.val
        if node.right:
            is_uni = self.dfs(node.right) and is_uni and node.val == node.right.val

        if is_uni:
            self.res += 1
        return is_uni

# Test Cases
if __name__ == "__main__":
    solution = Solution()
