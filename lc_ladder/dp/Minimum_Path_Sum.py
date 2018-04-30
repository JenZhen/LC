#!/usr/bin/python

# http://lintcode.com/en/problem/minimum-path-sumGrid/
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sumGrid of all numbers along its path. (Can only move down or right at a point.)
# Example

"""
Algo: Matrix DP
D.S.:

Solution:
Same as Unique Path
- State:
- Function:
- Initialization:
- Answer:

Time: O(m * n)
Space: O(1) - Modify input grid

Corner cases:
"""

class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sumGrid of all numbers along its path
    """
    def minPathsumGrid(self, grid):
        # write your code here
        m = len(grid) if grid is not None else 0
        n = len(grid[0]) if m != 0 else 0
        if m == 0 or n == 0:
            return 0
        # init first row and first column
        i, j = 1, 1

        while i < m:
            grid[i][0] += grid[i - 1][0]
            i += 1
        while j < n:
            grid[0][j] += grid[0][j - 1]
            j += 1
        i, j = 1, 1
        while i < m:
            j = 1
            while j < n:
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
                j += 1
            i += 1
        return grid[m - 1][n - 1]

    def repr(self, grid):
        print("[")
        for row in grid:
            print "[" + ", ".join([str(ele) for ele in row]) + "]"
        print("]")

# Test Cases
if __name__ == "__main__":
    testCases = [
        {"grid":
            [
             [1,3,1],
             [1,5,1],
             [4,2,1]
            ]
        },
        {"grid":
            [
              [2]
            ]
        },
        {"grid":
            [] # grid[0] is IndexError
        },
        {"grid": None
        },
    ]
    solution = Solution()
    for t in testCases:
        grid = t["grid"]
        res = solution.minPathsumGrid(grid)
        print("res: %s" %res)
