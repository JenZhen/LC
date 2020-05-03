#!/usr/bin/python

# Suppose an array sorted in ascending order is rotated
# at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search.
# If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.

"""
Algo: Binary Search
D.S.: Array

Solution:
Binary template 3 -- search covers all elements
Note: Buggy error, when comparing with nums[hi] with target >= or <=

All cases:
nums[mid] ~ nums[hi]
	-- A: > : mid on left of rotating(breaking) point
	-- B: < : mid on right of rotating(breaking) point
target ~ nums[hi]
	-- C: < : target on right of rotating point
	-- D: > : target on left of rotating point

4 Combinations:
	-- A & C, left and right, lo = mid
	-- A & D. both left, compare nums[mid] ~ target
	-- B & C, right and left, hi = mid
	-- B & D, both right, compare nums[mid] ~ target

Complexity O(logN)

Similar to "Find Minimum in Rotated Sorted Array"
-- If duplicate allows, worst case would be all of the same value but goal.
	Cannot tell should go left or right, O(n)
Corner cases:
"""

class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0 or target is None:
            return -1
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid
                else:
                    r = mid
        if nums[l] == target: return l
        if nums[r] == target: return r
        return -1
# Test Cases
if __name__ == "__main__":
	solution = Solution()
	inputs = [
		{
			'nums': [1, 3, 5],
			'target': 5
		}
	]

	for testcase in inputs:
		nums = testcase['nums']
		target = testcase['target']
		print solution.search(nums, target)
