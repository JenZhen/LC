#!/usr/bin/python

# https://leetcode.com/problems/array-partition-i/description/
# Example Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

"""
Algo: math
D.S.:

Solution:
Sort array, (a1, a2), (a3, a4), a1 + a3 gets the max min-pair

Time: O(nlogn)
Space: o(1)

Corner cases:
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        maxSum = 0
        for i in range(0, len(nums), 2):
            maxSum += nums[i]
        return maxSum

# Test Cases
if __name__ == "__main__":
    solution = Solution()
