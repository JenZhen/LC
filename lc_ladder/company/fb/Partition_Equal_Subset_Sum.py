#! /usr/local/bin/python3

# https://leetcode.com/problems/partition-equal-subset-sum/submissions/
# Example
# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that
# the sum of elements in both subsets is equal.
# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
#
# Example 1:
# Input: [1, 5, 11, 5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
# Example 2:
# Input: [1, 2, 3, 5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
"""
Algo: 背包DP
D.S.:

Solution:
找到一个SUBSET 和为 总和的一半
背包问题
Time: O(len(nums) * sum)
Space: O(sum) --> 2D ->1D

Solution2 不知道为什么不对
例子： [23,13,11,7,6,5,5] 返回TRUE 为什么不是FALSE

Corner cases:
"""

class Solution1(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mySum =  sum(nums);
        if mySum % 2 == 1:
            return False
        mySum //= 2
        dp = [False for x in range(mySum + 1)]
        dp[0] = True
        for i in range(0, len(nums)):
            for j in range(mySum, nums[i] - 1, -1):
                dp[j] |= dp[j - nums[i]]
        return dp[mySum]


class Solution2(object):
    def canPartition(self, nums):
        if not nums: return False
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2
        # does nums have a subset sum as target
        m = len(nums)
        f = [[False for _ in range(target + 1)] for _ in range(m + 1)]
        # init f[0][0]
        f[0][0] = True
        # dp
        for i in range(1, m + 1):
            for j in range(1, target + 1):
                if j < nums[i - 1]:
                    f[i][j] = f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j - nums[i - 1]]
        return f[m][target]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
