#!/usr/bin/python

# http://lintcode.com/en/problem/unique-paths/
# A robot is located at the top-left corner of a m x n grid.
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
# How many possible unique paths are there?
# Example
# Given m = 3 and n = 3, return 6.
# Given m = 4 and n = 5, return 35.

"""
Algo: Matrix DP
D.S.: Array

Solution:
- State: how many solutions to each a certain cell
- Function: grid[i][j] = grid[i - 1][j] + grid[i][j - 1], comes from up cell or left cell
- Initialization: grid[i: 0, m - 1][0] first column and grid[0][j: 0, n - 1] first row, all init as 1, since only 1 way of getting there.
- Answer: value of grid[m - 1][n - 1]

Time: O(m * n) - need to iterate and get number of solution for each cell.
Space: O(m * n) - need to build a grid to memorize all solution for each cell.
Corner cases:
"""

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        grid = [[1] * n] * m
        for i in range(1, m):
            grid[i][0] = 1
        for j in range(1, n):
            grid[0][j] = 1
        for i in range (1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
