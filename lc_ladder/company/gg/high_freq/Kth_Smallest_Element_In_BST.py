#! /usr/local/bin/python3

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Example
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
#
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""
Algo:
D.S.:

Solution: Stack, BST iteration
1. recursion:
Time: O(n)
Space: O(n)
所有点访问一遍
2. iteration
Time: O(logN + k) worst O(n + k)
Space: O(logN + k)

Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_Recursion:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = []
        self.inorder(root)
        return self.res[k - 1]
    def inorder(self, node):
        if not node: return
        self.inorder(node.left)
        self.res.append(node.val)
        self.inorder(node.right)

class Solution_Iteration:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        node = root
        while 1:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right

# Test Cases
if __name__ == "__main__":
    solution = Solution()
