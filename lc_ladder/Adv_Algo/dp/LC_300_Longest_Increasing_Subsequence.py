#! /usr/local/bin/python3

# https://www.lintcode.com/problem/longest-increasing-subsequence/description
# Given a sequence of integers, find the longest increasing subsequence (LIS).
#
# You code should return the length of the LIS.
#
# Example
# For [5, 4, 1, 2, 3], the LIS is [1, 2, 3], return 3
# For [4, 2, 4, 5, 3, 7], the LIS is [2, 4, 5, 7], return 4
#
# Challenge
# Time complexity O(n^2) or O(nlogn)
#
# Clarification
# What's the definition of longest increasing subsequence?
#
# The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique.
#
# https://en.wikipedia.org/wiki/Longest_increasing_subsequence

"""
Algo:
D.S.:

Solution1. DP, 暴力
Time: O(n^2), Space(n)
f[i] i:0->n 以nums[i]结尾的lic

Solution2. Binary Search
Time: O(nlogn) Space: O(n)
TODO

Corner cases:
"""

class Solution1:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums:
            return 0
        l = len(nums)
        res = 1
        lic = [1 for _ in range(l)]
        for i in range(1, l):
            tempLongest = 1
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    tempLongest = max(tempLongest, lic[j] + 1)
            lic[i] = tempLongest
            res = max(res, tempLongest)
        return res

class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []

        for i in nums:
            idx = bisect.bisect_left(dp, i)
            if idx == len(dp):
                dp.append(i)
            else:
                dp[idx] = i
        return len(dp)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
