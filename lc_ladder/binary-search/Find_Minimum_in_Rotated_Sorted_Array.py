#!/usr/bin/python

# Suppose an array sorted in ascending order is rotated at some pivot 
# unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# Find the minimum element.
# You may assume no duplicate exists in the array.

"""
Algo: Binary Search
D.S.: Array

Solution:
Binary Search template Solution3 to deal with comparison and avoid
out of boundry
After pivoting, 2 sections - left and right
The min number is the leftmost point of right section
lowest/leftmost of left section is GREATER than highest/rightmost of right section
So, key point comparing w/ last idx i.e. rightmost idx to tell on which section
There are 2 scenarios - 
1. pivots on left of original arrary ->
	A[mid] > A[last] -> mid falls on left section -> lo = mid to push search on right
2. pivots on right of original array ->
	A[mid] < A[last] -> mid falls on right section -> hi = mid to push search on left 

Time Complexity: O(logN)
Space Complexity:O(1)

Similar to "Find Minimum in Rotated Sorted Array II"
If duplicate allows, CANNOT use binary search (sim to "mountain sequence")
Since when comparing A[mid] w/ A[last] may equal, cannot tell mid falls
on left or right section. It will have to be O(N) linear.

Corner cases:
- Invalid inputs
- 1 or 2 element only (to avoid out of broundry use template Solution3)
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return -1
        lo, hi = 0, len(nums) - 1
        last = len(nums) - 1 
        while lo + 1 < hi:
            mid = (lo + hi) / 2
            if nums[mid] < nums[last]:
                hi = mid
            else:
                lo = mid
        return min(nums[hi], nums[lo])

# Test Cases
if __name__ == "__main__":
	inputs = [
		{'A': [1]}, 		 # 1
		{'A': [2,1]},		 # 1 
		{'A': [4,0,1,2,3]},  # 0
		{'A': [2,3,4,0,1]},  # 0
		{'A': [0,1,2,3,4]},  # 0
	]
	solution = Solution()
	for testcase in inputs:
		nums = testcase['A']
		print solution.findMin(nums)

