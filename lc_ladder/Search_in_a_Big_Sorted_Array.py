#!/usr/bin/python

# Given a big sorted array with positive integers sorted by ascending order.
# The array is so big so that you can not get the length of the whole array directly,
# and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).
# Find the first index of a target number. Your algorithm should be in O(log k),
# where k is the first index of the target number.
#
# Return -1, if the number doesn't exist in the array.
#
# Have you met this question in a real interview? Yes
# Example
# Given [1, 3, 6, 9, 21, ...], and target = 3, return 1.
#
# Given [1, 3, 6, 9, 21, ...], and target = 4, return -1.
#
# Challenge
# O(log k), k is the first index of the given target number.
# Example

"""
Algo: Binary Search
D.S.: Array Manipulation

Solution:
Binary Search - Loop or recursion
- Since there is no definite length of array, need to estimate
	length = length * 2 + 1
	Double the estimated length till
		1. longer than whole array reader return -1
		2. value greater than target
- After finding estimated length, do binary search
	If index exceeds the length of array, it will safely return -1.

Time Complexity: O(2*log(k))
Space Complexity: O(1)
Corner cases:
- Invalid input:
	1. Big array and ArrayReader are given, no need to check validity
	2. target may be None
- Weired cases see below
"""


"""
Definition of ArrayReader:
"""
class ArrayReader:
	def __init__(self, array):
		self.array = array

	def get(self, index):
		# this would return the number on the given index
		# return -1 if index is less than zero.
		return -1 if index >= len(self.array) else self.array[index] 


class Solution1:
	# @param {ArrayReader} reader: An instance of ArrayReader
	# @param {int} target an integer
	# @return {int} an integer
	def __init__(self, array):
		self.array = array

	def searchBigSortedArray(self, reader, target):
	# write your code here
		if target is None:
			return -1
		length = 0
		while reader.get(length) != -1 and reader.get(length) < target:
			length = length * 2 + 1

		lo, hi = 0, length
		while lo <= hi:
			mid = (lo + hi) / 2
			# print "Value of mid: ", reader.get(mid)
			if target < reader.get(mid):
				hi = mid - 1
			elif reader.get(mid) == -1: #in case mid outside array
				hi = mid - 1
			elif target > reader.get(mid): #mid within array
				lo = mid + 1
			else:
				return mid
		return -1

class Solution2:
	# @param {ArrayReader} reader: An instance of ArrayReader
	# @param {int} target an integer
	# @return {int} an integer
	def __init__(self, array):
		self.array = array

	def searchBigSortedArray(self, reader, target):
	# write your code here
		if target is None:
			return -1
		length = 0
		while reader.get(length) != -1 and reader.get(length) < target:
			length = length * 2 + 1

		lo, hi = 0, length
		while lo + 1 < hi:
			mid = (lo + hi) / 2
			# print "Value of mid: ", reader.get(mid)
			if target < reader.get(mid):
				hi = mid
			elif reader.get(mid) == -1: #in case mid outside array
				hi = mid
			elif target > reader.get(mid): #mid within array
				lo = mid
			else:
				return mid

		if reader.get(lo) == target:
			return lo
		elif reader.get(hi) == target:
			return hi
		else:
			return -1


# Test Cases
if __name__ == "__main__":
	# Input array as value == idx
	# expa path[0,1,  3,      7,                   15,            31,63...]
	inputArray = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
	inputs = [   
		{'target': 0}, #0
		{'target': 4}, #4
		{'target': 15},#15
		{'target': 17},#17
		{'target': 20},#-1
		{'target': 7.5},#-1
		{'target': 19},#19
	]

	solution1 = Solution1(inputArray)
	solution2 = Solution2(inputArray)
	reader = ArrayReader(inputArray)

	print "Test solution 1 ----------"
	for testcase in inputs:
		target = testcase['target']
		print solution1.searchBigSortedArray(reader, target)

	print "Test solution 2 ----------"
	for testcase in inputs:
		target = testcase['target']
		print solution2.searchBigSortedArray(reader, target)
