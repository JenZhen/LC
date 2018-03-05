#!/usr/bin/python

# Find the last position of a target number in a sorted array. 
# Return -1 if target does not exist.
# Example, given [1, 2, 2, 4, 5, 5]. For target = 2, return 2.

"""
Algo: Binary Search
D.S.: Array

Solution:
Searching a duplicate or an interval, using classical binary search
Solution3. Same method applies to "Fist Position of Target"
Time Complexity: O(logN)
Space Complexity: O(1)
Corner cases:
"""
class SolutionLast:
	# @param array: array of number
	# @param target: a number
	# @return {int} an integer, the idx of closest array
	def lastPosition(self, array, target):
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
			else: # target == array[mid]
				lo = mid # move lo to mid s.t. push to last position

		if array[hi] == target: # check hi first for last position
			return hi
		elif array[lo] == target:
			return lo
		else:
			return -1

class SolutionFirst:
	# @param array: array of number
	# @param target: a number
	# @return {int} an integer, the idx of closest array
	def firstPosition(self, array, target):
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
			else: # target == array[mid]
				hi = mid # move hi to mid s.t. push to first position

		if array[lo] == target: # check lo first for first position
			return lo
		elif array[hi] == target:
			return hi
		else:
			return -1

# Test Cases
if __name__ == "__main__":
	# input array: 
	# indx  [0, 1, 2, 3, 4, 5, 6]
	array = [1, 1, 2, 2, 4, 5, 5]
	inputs = [					   #Last  #First
		{'A': array, 'target': 1}, # 1     0  
		{'A': array, 'target': 2}, # 3	   2
		{'A': array, 'target': 3}, # -1	   -1
		{'A': array, 'target': 4}, # 4	   4	
		{'A': array, 'target': 5}, # 6	   5
		{'A': [1, 1],'target': 1}, # 1     0
		{'A': [1],   'target': 1}, # 0     0
	]
	
	solutionLast = SolutionLast()
	solutionFirst = SolutionFirst()
	print "Test Last Position ---------- "
	for testcase in inputs:
		array = testcase['A']
		target = testcase['target']
		print solutionLast.lastPosition(array, target)

	print "Test First Position ---------- "
	for testcase in inputs:
		array = testcase['A']
		target = testcase['target']
		print solutionFirst.firstPosition(array, target)

