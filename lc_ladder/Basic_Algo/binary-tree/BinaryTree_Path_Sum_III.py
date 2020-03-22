#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/path-sum-iii/description/
# Example
# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11

"""
Algo: DFS
D.S.: Binary Tree

Solution:
1. 2-Layers of bfs
Time: O(nlogn) - O(n^2)
2. Memorization bfs
https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-:-)
Time: O(n) -- each node visited once Spcae: O(n)

Corner cases:
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.res = 0
        cache = {0:1}
        self.dfs(root, cache, 0, sum)
        #self.dfs(root, sum, 0, cache)
        return self.res

    def dfs(self, root, cache, curSum, target):
        if not root:
            return
        curSum += root.val
        self.res += cache.get(curSum - target, 0)
        cache[curSum] = cache.get(curSum, 0) + 1

        self.dfs(root.left, cache, curSum, target)
        self.dfs(root.right, cache, curSum, target)
        cache[curSum] -= 1

# Test Cases
if __name__ == "__main__":
	solution = Solution()
