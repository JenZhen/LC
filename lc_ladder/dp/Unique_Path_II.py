#!/usr/bin/python

# http://lintcode.com/en/problem/unique-paths-ii/
# Follow up for "Unique Paths":
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Example
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.

"""
Algo: Matrix DP
D.S.:

Solution:
- State: how many solutions to each a certain cell
- Function: grid[i][j] = grid[i - 1][j] + grid[i][j - 1], comes from up cell or left cell
            Special condition, if original grid marks as 1, cell inaccessible, grid[i][j] = 0
- Initialization: grid[i: 0, m - 1][0] first column and grid[0][j: 0, n - 1] first row, all init as 1, since only 1 way of getting there. If original grid marks as 1, cell inaccessible, grid[i][j] = 0
- Answer: value of grid[m - 1][n - 1]

Time: O(m * n) - need to iterate and get number of solution for each cell.
Space: O(m * n) - need to build a grid to memorize all solution for each cell.

Corner cases:
"""

class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        grid = obstacleGrid
        self.reprGrid(grid)
        m = len(grid) if grid is not None else 0
        n = len(grid[0]) if grid[0] is not None else 0
        if m == 0 or n == 0:
            return 0
        # init [0][0]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            grid[0][0] = 1
        self.reprGrid(grid)

        # init grid[i][0] i: 1, m - 1
        i = 1
        while i < m:
            if grid[i - 1][0] == 0 or obstacleGrid[i][0] == 1:
                grid[i][0] = 0
            else:
                grid[i][0] = 1
            i += 1
        # init grid[0][j] j: 1, n - 1
        j = 1
        while j < n:
            if grid[0][j - 1] == 0 or obstacleGrid[0][j] == 1:
                grid[0][j] = 0
            else:
                grid[0][j] = 1
            j += 1
        self.reprGrid(grid)
        # iterate through other cells in the grid
        # i, j starts from 1, 1
        i, j = 1, 1
        while i < m:
            j = 1
            while j < n:
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i][j - 1] + grid[i - 1][j]
                j += 1
            i += 1

        print("size %s" %len(grid))
        self.reprGrid(grid)
        return grid[m - 1][n - 1]

    def reprGrid(self, grid):
        m = len(grid) if grid is not None else 0
        n = len(grid[0]) if grid[0] is not None else 0
        if m == 0 or n == 0:
            print("Invalid Grid")
        print("[")
        for i in range(m):
            print(",".join([str(s) for s in grid[i]]))
        print("]")

# Test Cases
if __name__ == "__main__":
    testCases = [
        {
        "obstacleGrid":
            [
              [0,0,0],
              [0,1,0],
              [0,0,0]
            ]
        },
        {
        "obstacleGrid":
            [
              [0]
            ]
        },
        {
        "obstacleGrid":
            [
              [1]
            ]
        }
    ]
    solution = Solution()
    for t in testCases:
        obstacleGrid = t["obstacleGrid"]
        res = solution.uniquePathsWithObstacles(obstacleGrid)
        print("res: %s" %res)
