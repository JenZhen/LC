#! /usr/local/bin/python3

# https://leetcode.com/problems/split-array-largest-sum/
# Given an array which consists of non-negative integers and an integer m,
# you can split the array into m non-empty continuous subarrays.
# Write an algorithm to minimize the largest sum among these m subarrays.
#
# Note:
# If n is the length of array, assume the following constraints are satisfied:
#
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# Examples:
#
# Input:
# nums = [7,2,5,10,8]
# m = 2
#
# Output:
# 18
#
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
"""
Algo: DP
D.S.:

Solution1:
DP
Time: O(row * col * col)
Space: O(row * col)

Solution2:
# TODO:
Binary Search + Greedy

Corner cases:
"""
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        import sys
        n = len(nums)
        f = [[sys.maxsize for _ in range(n)] for _ in range(m)]
        presum = [0] * n
        # init presum array
        presum[0] = nums[0]
        for i in range(1, n):
            presum[i] = presum[i - 1] + nums[i]
        # init f first row as presum
        for j in range(n):
            f[0][j] = presum[j]

        for i in range(1, m):
            for j in range(i, n):
                for k in range(j):
                    f[i][j] = min(f[i][j], max(f[i - 1][k], presum[j] - presum[k]))
        print(presum)
        print(f)
        return f[-1][-1]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
