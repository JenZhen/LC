#!/usr/bin/python

# Requirement
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

#     Integers in each row are sorted from left to right.
#     The first integer of each row is greater than the last integer of the previous row.
# Example
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Target 3: return True; Target 4: return False

"""
Algo: Binary Search
	  Generally two ways of doing binary search as below
D.S.: Array manipulation; array indexing

a m * n matrix can be stringingfied to a m*n array then do binary search
- key part is to convert array index to matrix index
- e.g. index x in array mapped to index in m*n matrix is
	   x / n, x % n
Exact same as "Classical Binary Search"
Solution 1: Loop
Solution 2: Recursion

Corner cases:

"""
# Solution 1 Loop
class Solution1(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if matrix is None or target is None or \
			len(matrix) == 0 or len(matrix[0]) == 0:
			return False
		m = len(matrix)
		n = len(matrix[0])
		# Sticke to template 3
		lo, hi = 0, m * n - 1
		while lo + 1 < hi:
		 	mid = (lo + hi) / 2
		 	x = mid / n
			y = mid % n
			if target < matrix[x][y]:
				hi = mid
			elif target > matrix[x][y]:
				lo = mid
			else:
				return True
		if target == matrix[lo / n][lo % n]:
			return True
		elif target == matrix[hi / n][hi % n]:
			return True
		else:
			return False


# Solution 2 Recursion
class Solution2(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
			return False
		self.m = len(matrix)
		self.n = len(matrix[0]) # use self member varible easier for later use
		lo, hi = 0, self.m * self.n - 1
		return self.helper(lo, hi, matrix, target)

	def helper(self, lo, hi, matrix, target):
		if lo > hi:
			return False
		mid = (lo + hi) / 2
		x = mid / self.n # here in recursion only use n, easy to be as a self variable
		y = mid % self.n
		if target < matrix[x][y]:
			return self.helper(lo, mid - 1, matrix, target)
		elif target > matrix[x][y]:
			return self.helper(mid + 1, hi, matrix, target)
		else:
			return True

# Test Cases
if __name__ == "__main__":
	solution1 = Solution1()
	Solution2 = Solution2()
	# 1.
	# 2.
	# 3.
