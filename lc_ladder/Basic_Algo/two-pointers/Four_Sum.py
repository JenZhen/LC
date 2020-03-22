#!/usr/bin/python

# https://leetcode.com/problems/4sum/description/
# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

"""
Algo:
D.S.:

Solution:
Similar to 3Sum, add one extra for loop outside from 0->length - 3
Time O(n^3) (sort O(nlogn))
Space O(1)

Corner cases:
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 4:
            return []

        res = []
        nums.sort()
        # fix the first element in idx i
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                t = target - (nums[i] + nums[j])
                l, r = j + 1, length - 1
                while l < r:
                    total = nums[l] + nums[r]
                    if total == t:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif total < t:
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    else:
                        r -= 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
