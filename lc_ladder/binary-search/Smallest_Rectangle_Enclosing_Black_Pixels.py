#!/usr/bin/python

# An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. 
# The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. 
# Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

"""
Algo: Binary Search/Linear Search
D.S.: Array/Matrix

Solution:
[
	[0, 0, 0, 1|, 0, 0],
	[0, 1, 1, 1|, 1, 0],
	[0,_0,_1,_1|,_0,_0],
	[0, 0, 0, 0|, 0, 0],
]
Starting (black pixel) (2, 3).
- To search a rectangle's range, given a starting point (2, 3) expand 4
directions based on it and do 4 search.
- Search leftward for example, col = 0:3, row = 2
	Horizontally, 0 and 1 are connected or sorted, so can do binary search moving idx(left, right)
	At each col (no matter matrix val is 0 or 1), search vertically
		if found 1, move right to mid, which denotes the leftmost boundry of black region
		if not 1, move left idx rightward to mid
- 4 directions are symetric
- After finding 4 boundries, calculated region area

Time Complexity:
Search left and right -- binary search horizontally, scan all vertically
	log(m) * n
Search top and bottom -- binary search vertically, scan all horizontally
	log(n) * m
Space Complexity: O(1)

Corner cases:
"""

class Solution(object):
	# @param image {List[List[str]]}  a binary matrix with '0' and '1'
	# @param x, y {int} the location of one of the black pixels
	# @return an integer
	def minArea(self, image, x, y):
		# Write your code here
		if image is None or len(image) == 0 or len(image[0]) == 0:
			return 0
		m = len(image)
		n = len(image[0])

		# left, right, top, bottom denotes final coordination of the area
		left, right, top, bottom = 0, 0, 0, 0
		
		# Similar to search the first position of target
		# Check left-side of (x,y) -- row = x, col = [0, y]
		x1, x2 = 0, y
		while x1 + 1 < x2:
			mid = (x1 + x2) / 2
			print "check left, mid = ", mid
			if self.checkRows(image, mid):
				x2 = mid
			else:
				x1 = mid
		if self.checkRows(image, x1):
			left = x1
		else:
			left = x2

		# Checking right-side of (x,y) -- row = x, col = [y, n]
		x1, x2 = y, n - 1
		while x1 + 1 < x2:
			mid = (x1 + x2) / 2
			if self.checkRows(image, mid):
				x1 = mid
			else:
				x2 = mid
		if self.checkRows(image, x2):
			right = x2
		else:
			right = x1

		# Check top-side of (x,y) -- col = y, row = [0, x]
		y1, y2 = 0, x
		while y1 + 1 < y2:
			mid = (y1 + y2) / 2
			if self.checkCols(image, mid):
				y2 = mid
			else:
				y1 = mid
		if self.checkCols(image, y1):
			top = y1
		else:
			top = y2

		# Check bottom-side of (x,y) -- col = y, row = [x, m]
		y1, y2 = x, m - 1
		while y1 + 1 < y2:
			mid = (y1 + y2) / 2
			print "check bottom, mid = ", mid
			if self.checkCols(image, mid):
				y1 = mid
			else:
				y2 = mid
		if self.checkCols(image, y2):
			bottom = y2
		else:
			bottom = y1

		print "dimension: ", left, " ", right, " ", top, " ", bottom
		return (right - left + 1) * (bottom - top + 1)


	def checkRows(self, image, col):
		# Given a column check if any rows of this col is 1
		# Return True if there is 1; False if no
		m = len(image)
		for row in range(m):
			if image[row][col] == 1:
				return True
		return False

	def checkCols(self, image, row):
		# Given a row check if any cols of this row is 1
		# Return True if there is 1; False if no
		n = len(image[0])
		for col in range(n):
			if image[row][col] == 1:
				return True
		return False

# Test Cases
if __name__ == "__main__":
	solution = Solution()
	image1 = [
		[0, 0, 0, 1, 0, 0],
		[0, 1, 1, 1, 1, 0],
		[0, 0, 1, 1, 0, 0],
		[0, 0, 0, 0, 0, 0],
	]
	image2 = [
		[0, 0, 1, 0],
		[0, 1, 1, 0],
		[0, 1, 0, 0]
	]	
	inputs = [
		{'image': image1,
		 'x': 2,
		 'y': 3,
		},
		{'image': image2,
		 'x': 0,
		 'y': 2,
		},
		{'image': image1,
		 'x': 1,
		 'y': 1},
	]
	for testcase in inputs:
		image = testcase['image']
		x = testcase['x']
		y = testcase['y']
		print solution.minArea(image, x, y)