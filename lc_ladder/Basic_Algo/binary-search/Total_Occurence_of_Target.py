#!/usr/bin/python

# Given a target number and an integer array sorted in ascending order. 
# Find the total number of occurrences of target in the array.
# Example
# Given [1, 3, 3, 4, 5] and target = 3, return 2.
# Given [2, 2, 3, 4, 6] and target = 4, return 1.
# Given [1, 2, 3, 4, 5] and target = 6, return 0.

"""
Algo: Binary Search
D.S.: Array

Solution:
Similar to "First/Last Position of Target", do binary search twice.
Time Complexity: O(2*logN)
Space: O(1)

Similar with:
Search for a Range
https://leetcode.com/problems/search-for-a-range/description/

Note: Worse case, array of one single number. while search O(N)
Corner cases:
"""

class Solution:
	# @param array: array of number
	# @param target: a number
	# @return {int} an integer, total occurence of target
	def totalOccurence(self, array, target):
		if array is None or target is None or len(array) == 0:
			return 0
		# Find idx of first occurence
		firstIdx = self.findFirstPosition(array, target)
		# Find idx of last occurence
		lastIdx = self.findLastPosition(array, target)
		
		if firstIdx == -1 or lastIdx == -1: #they should be -1 at same time
			return 0
		else:
			return lastIdx - firstIdx + 1

	def findFirstPosition(self, array, target):
		# No need to check invalidity
		lo, hi = 0, len(array) - 1
		while lo + 1 < hi:
			mid = (lo + hi) / 2
			if target < array[mid]:
				hi = mid
			elif target > array[mid]:
				lo = mid
			else: # target == array[mid]
				hi = mid # move hi to mid s.t. push to first position

		if array[lo] == target: # check lo first for first position
			return lo
		elif array[hi] == target:
			return hi
		else:
			return -1

	def findLastPosition(self, array, target):
		# No need to check invalidity
		lo, hi = 0, len(array) - 1
		while lo + 1 < hi:
			mid = (lo + hi) / 2
			if target < array[mid]:
				hi = mid
			elif target > array[mid]:
				lo = mid
			else: # target == array[mid]
				lo = mid # move lo to mid s.t. push to last position

		if array[hi] == target: # check hi first for last position
			return hi
		elif array[lo] == target:
			return lo
		else:
			return -1

# Test Cases
if __name__ == "__main__":
	inputs = [
		{'A': [],              'target': 1}, # 0
		{'A': [1, 3, 3, 4, 5], 'target': 3}, # 2
		{'A': [1, 3, 3, 4, 5], 'target': 4}, # 1
		{'A': [1, 3, 3, 4, 5], 'target': 2}, # 0
		{'A': [1, 1, 1, 1, 1], 'target': 1}, # 5
	]
	solution = Solution()
	for testcase in inputs:
		array = testcase['A']
		target = testcase['target']
		print solution.totalOccurence(array, target)