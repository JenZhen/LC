#! /usr/local/bin/python3

# https://leetcode.com/problems/first-missing-positive/submissions/
# Example
# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
# Input: [1,2,0]
# Output: 3
# Example 2:
#
# Input: [3,4,-1,1]
# Output: 2
# Example 3:
#
# Input: [7,8,9,11,12]
# Output: 1
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.
"""
Algo: array index as map
D.S.:

Solution:
Time: O(n) -- 几个pass
Space: O(1)

Corner cases:
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # if 1 not in nums, return 1
        if 1 not in nums:
            return 1
        # 这里不要忘记
        if n == 1: return 2

        # for size = n, it could be from 1 - n
        # max missing positive could be n + 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        for i in range(n):
            a = abs(nums[i])

            if a == n:
                # val to idx, n 顺移到idx = 0位置
                nums[0] = - abs(nums[0])
            else:
                nums[a] = - abs(nums[a])

        print(nums)
        for i in range(1, n):
            if nums[i] > 0:
                # 没有元素占这个位置
                return i
        if nums[0] > 0:
            return n
        return n + 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
