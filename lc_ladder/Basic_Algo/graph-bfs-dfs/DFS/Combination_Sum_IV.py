#! /usr/local/bin/python3

# https://leetcode.com/problems/combination-sum-iv/submissions/
# Given an integer array with all positive numbers and no duplicates,
# find the number of possible combinations that add up to a positive integer target.
#
# Example:
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
#
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?

"""
Algo: DP
D.S.:

Solution:
问有几个解 典型的DP

Corner cases:
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(1, target + 1):
            # outer iterate all possible sum
            for j in range(len(nums)):
                # inner iterate all candidates
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]
        return dp[target]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
