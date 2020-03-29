#!/usr/bin/python

# https://leetcode.com/problems/sort-colors/description/
# Example

"""
Algo: Two pointers
D.S.:

Solution:
- a cursor moves from left most to right
- l marks right boundry of 0, where next 0 stays
- r marks left boundry of 2, where next 2 stays
- cursor should check case when == r, when swap with l, it must be 1, because it's passed
Corner cases:
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l, r, cur = 0, len(nums) - 1, 0
        while cur <= r:
            if nums[cur] == 0:
                nums[cur], nums[l] = nums[l], nums[cur]
                l += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur], nums[r] = nums[r], nums[cur]
                r -= 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
