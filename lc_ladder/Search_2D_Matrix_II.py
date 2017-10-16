#!/usr/bin/python

# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
# Given target = 20, return false.

"""
Algo: Search but not strictly ordered, hence not binary
D.S.: Array

Solution:
Starting from bottom left or top right element (18 or 15) search
Say if from 18. If element > target move left; if element < target move up
Index only moves up and right then, there is only one direction of moving
If starting from topleft or bottom right, direction is not unique.
Starting point bottom-left and top-right are symmetric.

Time Complexity: O(m + n) matrix is m*n
Space Complexity: O(1)
Corner cases:
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or target is None or \
        	len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        
        #Starting from bottom-left, move up and right
        r, c = row - 1, 0
        while r >= 0 and c < col:
            if matrix[r][c] > target:
                r -= 1
            elif matrix[r][c] < target:
                c += 1
            else:
                return True
        """
        #Starting from top-right, move down and left
        r, c = 0, col - 1
        while r < row and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        """
        return False
# Test Cases
if __name__ == "__main__":
	solution = Solution()
	matrix = [
		[1,   4,  7, 11, 15],
		[2,   5,  8, 12, 19],
		[3,   6,  9, 16, 22],
		[10, 13, 14, 17, 24],
		[18, 21, 23, 26, 30]
	]
	inputs = [
		{
			'matrix': matrix,
			'target': 21,
		},
		{
			'matrix': matrix,
			'target': 1,
		},
		{
			'matrix': matrix,
			'target': 25,
		},
	]

	for testcase in inputs:
		matrix = testcase['matrix']
		target = testcase['target']
		print solution.searchMatrix(matrix, target)