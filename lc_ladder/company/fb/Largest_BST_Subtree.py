#! /usr/local/bin/python3

# https://leetcode.com/problems/largest-bst-subtree/submissions/
# Example
# Given a binary tree, find the largest subtree which is a Binary Search Tree (BST),
# where largest means subtree with largest number of nodes in it.
#
# Note:
# A subtree must include all of its descendants.
#
# Example:
#
# Input: [10,5,15,1,8,null,7]
#
#    10
#    / \
#   5  15
#  / \   \
# 1   8   7
#
# Output: 3
# Explanation: The Largest BST Subtree in this case is the highlighted one.
#              The return value is the subtree's size, which is 3.
# Follow up:
# Can you figure out ways to solve it with O(n) time complexity?
"""
Algo: Divide-and-Conquer
D.S.:

Solution:

Time: O(N) -- N is the number of node in tree
Space: O(1)
Corner cases:
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        low, hi, cnt, isValid = self.helper(root)
        return self.res

    def helper(self, node):

        if not node:
            return None, None, 0, True
        l_low, l_hi, l_cnt, l_valid = self.helper(node.left)
        r_low, r_hi, r_cnt, r_valid = self.helper(node.right)

        if not l_valid or not r_valid:
            return None, None, -1, False

        # if both left, right child are valid
        if l_cnt == 0 and r_cnt == 0:
            # both child are None
            self.res = max(self.res, l_cnt + r_cnt + 1)
            return node.val, node.val, 1, True
        elif l_cnt == 0:
            # if left child is None
            if node.val < r_low:
                self.res = max(self.res, l_cnt + r_cnt + 1)
                return node.val, r_hi, l_cnt + r_cnt + 1, True
            else:
                return None, None, -1, False
        elif r_cnt == 0:
            # if right child is None
            if node.val > l_hi:
                self.res = max(self.res, l_cnt + r_cnt + 1)
                return l_low, node.val, l_cnt + r_cnt + 1, True
            else:
                return None, None, -1, False
        else:
            # both are not None
            # print(node.val) if node else print('None')
            if l_hi < node.val < r_low:
                self.res = max(self.res, l_cnt + r_cnt + 1)
                return l_low, r_hi, l_cnt + r_cnt + 1, True
            else:
                return None, None, -1, False
# Test Cases
if __name__ == "__main__":
    solution = Solution()
