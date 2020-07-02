#! /usr/local/bin/python3

# https://www.lintcode.com/problem/maximum-product-subarray/description
# https://leetcode.com/problems/maximum-product-subarray/
# Example
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""
Algo: DP
D.S.:

Solution:


Corner cases:
Can "0.5" "-0.5" be handled well?
"""


class Solution1:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        if not nums:
            return 0

        res = nums[0]
        minArr = [0] * len(nums)
        maxArr = [0] * len(nums)
        minArr[0] = maxArr[0] = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > 0:
                maxArr[i] = max(maxArr[i - 1] * nums[i], nums[i])
                minArr[i] = min(minArr[i - 1] * nums[i], nums[i])
            else:
                maxArr[i] = max(minArr[i - 1] * nums[i], nums[i])
                minArr[i] = min(maxArr[i - 1] * nums[i], nums[i])
        return max(maxArr)


class Solution_Wrong:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        if not nums:
            return 0

        minNum = nums[0]
        maxNum = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > 0:
                maxNum = max(maxNum * nums[i], nums[i])
                minNum = min(minNum * nums[i], nums[i])

            else:
                # IMPORTANT: here is a cross use of maxNum and minNum
                # first line updated the original maxNum value
                maxNum = max(minNum * nums[i], nums[i])
                minNum = min(maxNum * nums[i], nums[i])
            res = max(res, maxNum)
        return res

class Solution2:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        if not nums:
            return 0

        minNum = nums[0]
        maxNum = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > 0:
                maxNum = max(maxNum * nums[i], nums[i])
                minNum = min(minNum * nums[i], nums[i])

            else:
                newMax = max(minNum * nums[i], nums[i])
                newMin = min(maxNum * nums[i], nums[i])
                maxNum = newMax
                minNum = newMin
            res = max(res, maxNum)
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
