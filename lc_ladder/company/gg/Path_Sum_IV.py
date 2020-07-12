#! /usr/local/bin/python3

# https://leetcode.com/problems/path-sum-iv/submissions/
# Example
# If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.
# For each integer in this list:
#
# The hundreds digit represents the depth D of this node, 1 <= D <= 4.
# The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
# The units digit represents the value V of this node, 0 <= V <= 9.
# Given a list of ascending three-digits integers representing a binary tree with the depth smaller than 5, you need to return the sum of all paths from the root towards the leaves.
#
# It's guaranteed that the given list represents a valid connected binary tree.
#
# Example 1:
#
# Input: [113, 215, 221]
# Output: 12
# Explanation:
# The tree that the list represents is:
#     3
#    / \
#   5   1
#
# The path sum is (3 + 5) + (3 + 1) = 12.
#
#
# Example 2:
#
# Input: [113, 221]
# Output: 4
# Explanation:
# The tree that the list represents is:
#     3
#      \
#       1
#
# The path sum is (3 + 1) = 4.
"""
Algo: DFS, Divide and conquer
D.S.:

Solution:
根据数据特性 把树用map构建出来
Time: O(n)
Space: O(n)

Corner cases:
"""

class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.res = 0
        self.mp = {} # key: node_local (11), val: node_value (2)
        for n in nums:
            self.mp[n // 10] = n % 10

        self.dfs(nums[0] // 10, 0)
        return self.res

    def dfs(self, node, ttl):
        if node not in self.mp: # none node
            return
        ttl += self.mp[node]

        depth = node // 10
        pos = node % 10
        left_node = (depth + 1) * 10 + pos * 2 - 1
        right_node = left_node + 1

        if left_node not in self.mp and right_node not in self.mp:
            self.res += ttl
        self.dfs(left_node, ttl)
        self.dfs(right_node, ttl)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
