#!/usr/bin/python

# Given a mountain sequence of n integers which increase firstly and 
# then decrease, find the mountain top.
# Note: There is no flat region
# Example: 
# Given nums = [1, 2, 4, 8, 6, 3] return 8 
# Given nums = [10, 9, 8, 7], return 10
# Return -1 is array empty

"""
Algo: Binary Search
D.S.: Array

Solution:
There are comparison during binary search, classical binary search
Solution3 is a better approach
There are 5 scenarios -- (which don't matter)
1. 单升； 2. 单降； 3. 峰在正中间； 4. 峰偏左； 5. 峰偏右
Goal is to find at mid if it increasing or decresing (compare w/ mid+1)
Move hi/lo toward increasing direction

This is exactly the same with "Find Peak Element", in which there may
be multiple peaks, and return any of the peaks is fine.

Corner cases:
"""

class Solution:
	# @param array: array of number
	# @param target: a number
	# @return {int} the max number
	def mountainSequence(self, array):
		# Write you code here
		if array is None or len(array) == 0:
			return -1
		lo, hi = 0, len(array) - 1
		while lo + 1 < hi: # when exit loop, lo + 1 = hi
			mid = (lo + hi) / 2
			if array[mid] > array[mid + 1]: # decresasing
				hi = mid
			else: # increasing
				lo = mid
			# Note no flat region otherwise not binary search
		return array[hi] if array[hi] > array[lo] else array[lo]


# Test Cases
if __name__ == "__main__":
	solution = Solution()
