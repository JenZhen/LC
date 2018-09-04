#! /usr/local/bin/python3

# https://lintcode.com/problem/subarray-sum/description
# Example
# Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

# Example
# Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].

# Notice
# There is at least one subarray that it's sum equals to zero.

"""
Algo: map, presum
D.S.: continuous subarray sum

Solution:
Time: O(N), Space: O(N) -- for map

Naiive solution: enumate starting and ending point i, j Time: O(N^2)
Build presum
nums:      [-3, 1, 2, -3, 4]
presum: [0, -3, -2, 0, -3, 1] (with padding -1)
sum[i:j] (range inclusive) = presum[j] - presum[i - 1] (i - 1 means there should be a padding)
presum[j] - presum[i - 1] = 0 -->
presum[j] = presum[i - 1]
Therefore needs a map to find presum value if equal

Corner cases:
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        dic = {0: -1}
        presum = 0
        for i in range(len(nums)):
            presum += nums[i]
            if presum in dic:
                return [dic[presum] + 1, i]
            dic[presum] = i

# Test Cases
if __name__ == "__main__":
    solution = Solution()
