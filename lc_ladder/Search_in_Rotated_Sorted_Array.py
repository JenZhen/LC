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
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		if nums is None or len(nums) == 0 or target is None:
			return -1
		lo, hi = 0, len(nums) - 1
		while lo + 1 < hi:
			mid = (lo + hi) / 2
			if nums[mid] == target:
				return mid
			if nums[mid] > nums[hi] and target <= nums[hi]:
				lo = mid
			elif (nums[mid] > nums[hi] and target >= nums[hi]) or \
				(nums[mid] < nums[hi] and target <= nums[hi]):
				if nums[mid] > target:
					hi = mid
				else:
					lo = mid
			else:
				hi = mid
		if nums[lo] == target:
			return lo
		elif nums[hi] == target:
			return hi
		else:
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
