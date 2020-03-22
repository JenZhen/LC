#!/usr/bin/python
# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/submissions/
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
因为black pixels 是连续存在的所以可以用binary search 否则就要一次查找

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

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if image is None or len(image) == 0 or len(image[0]) == 0:
            return 0

        m = len(image)
        n = len(image[0])

        left, right, top, bottom = 0, 0, 0, 0

        # scan left row = x, col = [0: y]
        lo, hi = 0, y
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self.checkCol(image, mid):
                hi = mid
            else:
                lo = mid
        if self.checkCol(image, lo):
            left = lo
        else:
            left = hi
        # scan right row = x, col = [y: n - 1]
        lo, hi = y, n - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self.checkCol(image, mid):
                lo = mid
            else:
                hi = mid
        if self.checkCol(image, hi):
            right = hi
        else:
            right = lo

        # scan top row = [0, x], col = y
        lo, hi = 0, x
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self.checkRow(image, mid):
                hi = mid
            else:
                lo = mid
        if self.checkRow(image, lo):
            top = lo
        else:
            top = hi

        # scan bottom row = [x, m - 1], col = y
        lo, hi = x, m - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self.checkRow(image, mid):
                lo = mid
            else:
                hi = mid
        if self.checkRow(image, hi):
            bottom = hi
        else:
            bottom = lo

        return (right - left + 1) * (bottom - top + 1)

    def checkCol(self, image, col):
        # fix column, scan all rows, to find if black pixel exists or not
        m = len(image)
        for i in range(m):
            if image[i][col] == '1':
                return True
        return False

    def checkRow(self, image, row):
        # fix row, scan all columns, to find if black pixel exists or not
        n = len(image[0])
        for j in range(n):
            if image[row][j] == '1':
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
