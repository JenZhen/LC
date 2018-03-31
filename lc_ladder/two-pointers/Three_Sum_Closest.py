#!/usr/bin/python

# https://leetcode.com/problems/3sum-closest/description/
# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# For example, given array S = {-1 2 1 -4}, and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""
Algo: Two sum, 2 pointers
D.S.:

Solution:
Same as twosum_closest
Be careful that this requires return the closest sum not the diff.
Need to keep an extra variable minSum

Similiar to Two Sum Closest To Target

Time: O(N^2) Sort O(nlogn) + 2-fold for loop O(N^2)
Space: O(n)
Corner cases:
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        import sys
        nums.sort()
        minDiff = sys.maxsize
        minSum = None
        length = len(nums)
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, length - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return target
                elif total < target:
                    if minDiff > target - total:
                        minDiff = target - total
                        minSum = total
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    if minDiff > total - target:
                        minDiff = total - target
                        minSum = total
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return minSum

# Test Cases
if __name__ == "__main__":
    solution = Solution()
