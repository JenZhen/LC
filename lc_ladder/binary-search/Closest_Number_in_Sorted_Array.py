#!/usr/bin/python

# Given a target number and an integer array A sorted in ascending order
# find the index i in A such that A[i] is closest to the given target.
# Return -1 if there is no element in the array.
# Example:
# Index = [0, 1, 2, 3, 4,  5,  6,  7]
# Array = [0, 1, 3, 7, 15, 31, 63, 127]
# taget:  [0, 1, 4, 127, 5, -1, 130]
# result: [0, 1, 2, 7,  2/3, 0,  7]

"""
Algo: Binary Search 
D.S.: Array

Solution:
Loop/Recursion
Difference from classical binary search: how to handle not found cases
Key points: understand template algo scenarios when not found
(using prev example)
1. 4 not found WITHIN array - idx_hi = 2, idx_lo = 3 (swapped)  
2. -1 not found LEFT Boundry - idx_hi = -1(out of boundry), idx_lo = 0
3. 130 not found RIGHT Boundry - idx_hi = 7, idx_lo = 8 (out of boundry)

Corner cases:
- Invalid inputs
- Found right in-between 2 numbers, return either
- Not found within array
- Not found out LEFT/RIGHT array
"""

class Solution1:
	# @param array: array of number
	# @param target: a number
	# @return {int} an integer, the idx of closest array
	def closestNumber(self, array, target):
		# Write you code here
		if array is None or target is None or len(array) == 0:
			return -1
		lo, hi = 0, len(array) - 1
		while lo <= hi:
			mid = (lo + hi) / 2
			if target < array[mid]:
				hi = mid - 1
			elif target > array[mid]:
				lo = mid + 1
			else:
				return mid
		# Check corner cases/unfound cases
		if hi == -1:
			return lo
		if lo == len(array):
			return hi
		if target - array[hi] <= array[lo] - target:
			return hi
		else:
			return lo

class Solution2: # Get more familiar with this way
	# @param array: array of number
	# @param target: a number
	# @return {int} an integer, the idx of closest array
	def closestNumber(self, array, target):
		# Write you code here
		if array is None or target is None or len(array) == 0:
			return -1
		lo, hi = 0, len(array) - 1
		while lo + 1 < hi:
			mid = (lo + hi) / 2
			if target < array[mid]:
				hi = mid
			elif target > array[mid]:
				lo = mid
			else:
				return mid
		if abs(target - array[hi]) < abs(array[lo] - target):
			return hi
		else:
			return lo


# Test Cases
if __name__ == "__main__":
	array = [0, 1, 3, 7, 15, 31, 63, 127]
	# taget:  [0, 1, 4, 127, 5, -1, 130]
	# result: [0, 1, 2, 7,  2/3, 0,  7]
	inputs = [
		{'A': [],    'target': 1},   #-1
		{'A': array, 'target': None},#-1
		{'A': array, 'target': 0},   #0
		{'A': array, 'target': 1},   #1
		{'A': array, 'target': 4},   #2
		{'A': array, 'target': 127}, #7
		{'A': array, 'target': 5},   #2
		{'A': array, 'target': -1},  #0
		{'A': array, 'target': 130}, #7

	]
	solution1 = Solution1()
	solution2 = Solution2()
	print "Test solution 1 ------------"
	for testcase in inputs:
		array = testcase['A']
		target = testcase['target']
		print solution1.closestNumber(array, target)

	print "Test solution 2 ------------"
	for testcase in inputs:
		array = testcase['A']
		target = testcase['target']
		print solution2.closestNumber(array, target)