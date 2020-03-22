#!/usr/bin/python

# https://leetcode.com/problems/find-the-duplicate-number/
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
# Example 1:
#
# Input: [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: [3,1,3,4,2]
# Output: 3
# Note:
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

"""
Algo: Binary Search, hash
D.S.:

Solution:
1. Binary Search
Time: O(nlogn) -- in-place sort takes O(nlogn)
Space: O(1) -- in-place

2. Hash
Time: O(n) linear scan
Space: O(n) implement of hash, either map or simply an array

Corner cases:
"""

class Solution1:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return None
        nums.sort()
        print(nums)
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if mid < nums[mid]:
                l = mid
            else:
                r = mid
        if nums[l] == l:
            return l
        if nums[r] == r:
            return r

class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return None
		# array slots[0] won't be used
        slots = [None] * len(nums)
        for i in nums:
            if slots[i] == None:
                slots[i] = i
            else:
                return i

# Test Cases
if __name__ == "__main__":
	solution = Solution()
