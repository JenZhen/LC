#!/usr/bin/python

# http://lintcode.com/en/problem/longest-increasing-subsequence/
# Given a sequence of integers, find the longest increasing subsequence (LIS).
# You code should return the length of the LIS.
# Example
# For [5, 4, 1, 2, 3], the LIS is [1, 2, 3], return 3
# For [4, 2, 4, 5, 3, 7], the LIS is [2, 4, 5, 7], return 4

"""
Algo: Sequence DP
D.S.:

Solution:
- State: f[i]: ends with nums[i], how long the increasing sub-sequence is
- Function: f[i] = max(f[i], f[j] + 1)
- Initialization: f[] init as all 1 since worst case -- decreasing sequence -- value of be 1 (the min case)
- Answer: max of f[]

Time: O(n ^ 2)
Space: O(n)

Corner cases:
"""
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums: # not nums includes len(nums) == 0
            return 0
        #init f array
        f = [1] * len(nums)
        # iterate to build f
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] <= nums[j]:
                    continue
                else:
                    f[i] = max(f[i], f[j] + 1)
        return max(f)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
