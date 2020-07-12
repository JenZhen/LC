#! /usr/local/bin/python3

# https://leetcode.com/problems/number-of-corner-rectangles/
# Example
# Given a grid where each entry is only 0 or 1, find the number of corner rectangles.
# A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle.
# Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.
#
# Example 1:
# Input: grid =
# [[1, 0, 0, 1, 0],
#  [0, 0, 1, 0, 1],
#  [0, 0, 0, 1, 0],
#  [1, 0, 1, 0, 1]]
# Output: 1
# Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
#
# Example 2:
# Input: grid =
# [[1, 1, 1],
#  [1, 1, 1],
#  [1, 1, 1]]
# Output: 9
# Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
#
# Example 3:
# Input: grid =
# [[1, 1, 1, 1]]
# Output: 0
# Explanation: Rectangles must have four distinct corners.
#
# Note:
#
# The number of rows and columns of grid will each be in the range [1, 200].
# Each grid[i][j] will be either 0 or 1.
# The number of 1s in the grid will be at most 6000.

"""
Algo:
D.S.:

Solution:
Time: O(mn * n)
Time: O(c^2)

这道题给了我们一个由0和1组成的二维数组，这里定义了一种边角矩形，其四个顶点均为1，
让我们求这个二维数组中有多少个不同的边角矩形。那么最简单直接的方法就是暴力破解啦，
我们遍历所有的子矩形，并且检验其四个顶点是否为1即可。先确定左上顶点，每个顶点都可以当作左上顶点，
所以需要两个for循环，然后我们直接跳过非1的左上顶点，接下来就是要确定右上顶点和左下顶点了，
先用一个for循环确定左下顶点的位置，同理，如果左下顶点为0，直接跳过。再用一个for循环确定右上顶点的位置，
如果右上顶点位置也确定了，那么此时四个顶点中确定了三个，右下顶点的位置也就确定了，此时如果右上和右下顶点均为1，则结果res自增1，参见代码如下：

Corner cases:
"""

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mp = {} # key: (j1, j1)pair, val: cnt
        res = 0
        for i1 in range(m):
            for j1 in range(n):
                if grid[i1][j1] == 1:
                    for j2 in range(j1 + 1, n):
                        if grid[i1][j2] == 1:
                            if (j1, j2) not in mp:
                                mp[(j1, j2)] = 0
                            res += mp[(j1, j2)]
                            mp[(j1, j2)] += 1
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
