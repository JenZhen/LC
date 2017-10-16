#!/usr/bin/python

# Array of ascending number find target;
# If found return index, if not found return -1 (Apply to True/False case)

"""
Algo: Binary Search
D.S.: Array Manipulation

Solution:
Binary Search has 2 typical ways
1. loop
2. recursion
See and remember template below
Time Complexity: O(logN)
Space Complexity: O(1)

Corner cases:
- See below
"""

# 1. While loop
class Solution1:
	# @param {int[]} A an integer array sorted in ascending order
	# @param {int} target an integer
	# @return {int} an integer
	def findPosition(self, A, target):
		# Write your code here
		if A is None or target is None or len(A) == 0:
			return -1
		lo, hi = 0, len(A) - 1
		while lo <= hi: # Important loop condition
			mid = (lo + hi) / 2
			if target < A[mid]:
				hi = mid - 1 # Important 有越界风险
			elif target > A[mid]:
				lo = mid + 1 # Important 有越界风险
			else:
				return mid
		return -1

# 2. Recusion
class Solution2:
	# @param {int[]} A an integer array sorted in ascending order
	# @param {int} target an integer
	# @return {int} an integer
	def findPosition(self, A, target):
		# Write your code here
		if A is None or target is None or len(A) == 0:
			return -1
		lo, hi = 0, len(A) - 1
		return self.helper(lo, hi, A, target)

	def helper(self, lo, hi, A, target):
		if lo > hi: # Important exit condition
			return -1
		mid = (lo + hi) / 2
		if target < A[mid]:
			return self.helper(lo, mid - 1, A, target)
		elif target > A[mid]:
			return self.helper(mid + 1, hi, A, target)
		else:
			return mid

# 1. While loop -- handles duplicates well
class Solution3:
	# @param {int[]} A an integer array sorted in ascending order
	# @param {int} target an integer
	# @return {int} an integer
	def findPosition(self, A, target):
		# Write your code here
		if A is None or target is None or len(A) == 0:
			return -1
		lo, hi = 0, len(A) - 1
		while lo + 1 < hi: # Important loop condition (wider lo hi range)
			mid = (lo + hi) / 2
			if target < A[mid]:
				hi = mid # Important
			elif target > A[mid]:
				lo = mid # Important
			else:
				return mid
		if A[lo] == target:
			return lo
		elif A[hi] == target:
			return hi
		else:
			return -1

# Test Cases
if __name__ == "__main__":
	solution1 = Solution1()
	solution2 = Solution2()
	solution3 = Solution3()
	inputs = [ #init an empty input list
	# 1. Invalid inputs - return -1
		{'A': None, 'target': 1},            # -1
		{'A': [1],  'target': None},		 # -1
		{'A': [],   'target': 1},			 # -1
	# 2. weired cases
		{'A': [1, 1],        'target': 0}, 	 # -1
		{'A': [1], 			 'target': 1},	 # 0
		{'A': [1, 1], 		 'target': 1},	 # 0
		{'A': [1, 1], 		 'target': 2},	 # -1
		{'A': [1, 2], 		 'target': 3},	 # -1
		#{'A': , 'target': },
	]
	print "Test Solution 1 --------- "
	for test in inputs:
		A = test['A']
		target = test['target']
		print solution1.findPosition(A, target)

	print "Test Solution 2 --------- "
	for test in inputs:
		A = test['A']
		target = test['target']
		print solution2.findPosition(A, target)

	print "Test Solution 3 --------- "
	for test in inputs:
		A = test['A']
		target = test['target']
		print solution3.findPosition(A, target)





