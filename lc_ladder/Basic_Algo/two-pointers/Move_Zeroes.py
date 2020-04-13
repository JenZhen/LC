#!/usr/bin/python

# https://leetcode.com/problems/move-zeroes/description/

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
# Note:
# 1 You must do this in-place without making a copy of the array.
# 2 Minimize the total number of operations.

"""
Algo: Two pointers
D.S.:

Solution:
This is a classic case of partition while keep original order
Corner cases:
"""

class Solution_Partition:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                p += 1
                nums[p], nums[i] = nums[i], nums[p]


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
