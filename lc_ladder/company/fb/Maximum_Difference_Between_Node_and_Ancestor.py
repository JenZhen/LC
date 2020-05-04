#! /usr/local/bin/python3

# Requirement
# Example
# Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
# (A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)
#
# Example 1:
# Input: [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation:
# We have various ancestor-node differences, some of which are given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
#
# Note:
# The number of nodes in the tree is between 2 and 5000.
# Each node will have value between 0 and 100000.

"""
Algo: Divide and Conquer
D.S.:

Solution:
每个节点返回 从叶子到当前的最大 最小值，全局 res 记录当前最优解
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
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, node):
        # return min, max of tree with node as root
        if not node:
            return None, None

        lmin, lmax = self.dfs(node.left)
        rmin, rmax = self.dfs(node.right)

        curmin, curmax = node.val, node.val
        if lmin != None and lmax != None:
            self.res = max(self.res, abs(node.val - lmin))
            self.res = max(self.res, abs(node.val - lmax))
            curmin = min(curmin, lmin)
            curmax = max(curmax, lmax)

        if rmin != None and rmax != None:
            self.res = max(self.res, abs(node.val - rmin))
            self.res = max(self.res, abs(node.val - rmax))
            curmin = min(curmin, rmin)
            curmax = max(curmax, rmax)

        return curmin, curmax
# Test Cases
if __name__ == "__main__":
    solution = Solution()
