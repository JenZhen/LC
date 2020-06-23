#! /usr/local/bin/python3

# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/submissions/
# Example
# Given a binary tree root, the task is to return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# Example 1:
# Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# Output: 20
# Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
#
# Example 2:
# Input: root = [4,3,null,1,2]
# Output: 2
# Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
#
# Example 3:
# Input: root = [-4,-2,-5]
# Output: 0
# Explanation: All values are negatives. Return an empty BST.
#
# Example 4:
# Input: root = [2,1,3]
# Output: 6
# Example 5:
# Input: root = [5,4,8,3,null,6,3]
# Output: 7
#
# Constraints:
# The given binary tree will have between 1 and 40000 nodes.
# Each node's value is between [-4 * 10^4 , 4 * 10^4].
"""
Algo: Divide-and-Conquer
D.S.:

Solution:
细节：
节点值可以是负数，最后如果和是负数，取0 才能通过AC

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
    def maxSumBST(self, root: TreeNode) -> int:
        import sys
        if not root:
            return 0
        self.res = -sys.maxsize
        low, hi, sum, isValid = self.helper(root)
        return max(self.res, 0)

    def helper(self, node):
        if not node:
            return None, None, None, True
        l_low, l_hi, l_sum, l_valid = self.helper(node.left)
        r_low, r_hi, r_sum, r_valid = self.helper(node.right)

        if not l_valid or not r_valid:
            return None, None, None, False

        # if both left, right child are valid BST
        if l_sum is None and r_sum is None:
            # both child are None
            self.res = max(self.res, node.val)
            return node.val, node.val, node.val, True
        elif r_sum is None:
            # if left child is not None
            if node.val > l_hi:
                self.res = max(self.res, l_sum + node.val)
                return l_low, node.val, l_sum + node.val, True
            else:
                return None, None, None, False
        elif l_sum is None:
            # if right child is not None
            if node.val < r_low:
                self.res = max(self.res, r_sum + node.val)
                return node.val, r_hi, r_sum + node.val, True
            else:
                return None, None, None, False
        else:
            # both are not None
            print(node.val) if node else print('None')
            if l_hi < node.val < r_low:
                self.res = max(self.res, l_sum + r_sum + node.val)
                return l_low, r_hi, l_sum + r_sum + node.val, True
            else:
                return None, None, None, False

# Test Cases
if __name__ == "__main__":
    solution = Solution()
