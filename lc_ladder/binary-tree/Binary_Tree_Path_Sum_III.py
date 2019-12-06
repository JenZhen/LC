#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/path-sum-iii/
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
Algo: DFS, Backtracking
D.S.: Binary Tree

Solution:
Important:
1) use self.res a member/global variable to track final result
2) Do need to check res before save the new value into cache,
An example: tree of a single node [5] target sum = 0, should return 0,
if save curSum in cache first it will return 1, which is the none node value

Time Complexity: O(N) -- N is number of nodes
Space Complexity: O(N) -- N is number of nodes

Corner cases:
"""

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.res = 0
        cache = {0: 1} # it's like a padding
        self.helper(root, sum, 0, cache)
        return self.res

    def helper(self, node, sum, curSum, cache):
        if not node:
            return
        curSum += node.val
		# Do need to check res before save the new value into cache
		# none node is 0 which should not be considered
        self.res += cache.get(curSum - sum, 0)
        cache[curSum] = cache.get(curSum, 0) + 1

        self.helper(node.left, sum, curSum, cache)
        self.helper(node.right, sum, curSum, cache)
        cache[curSum] -= 1
        # curSum is just a variable no need to remove

# Test Cases
if __name__ == "__main__":
	solution = Solution()
