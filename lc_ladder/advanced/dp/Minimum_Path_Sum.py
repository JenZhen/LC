#! /usr/local/bin/python3

# https://www.lintcode.com/problem/minimum-path-sum/description
# Example
# Given a m x n grid filled with non-negative numbers,
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Notice
# You can only move either down or right at any point in time.

"""
Algo: DP -- 二维滚动数组
D.S.:

Solution:
Time: O(mn) space: O(n)

DP 分析
1. 状态
f[i]: 到位置i， Minsum 是多大
2. 方程
f[i] = min(f[i - 1], f[i]) + grid[i][j]
f[i]为来自上一行，f[i-1]为来自左边

3. 初始化
第一行从左到右cumulate
第一列从上倒下cumulate
4. 答案
f[col - 1]

Corner cases:
Be carefull about the initiation of this grid
"""

class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0

        row = len(grid)
        col = len(grid[0])
        f = [grid[0][0]] * col
        for j in range(1, col):
            f[j] = f[j - 1] + grid[0][j]

        for i in range(1, row):
            for j in range(col):
                if j == 0:
                    f[j] += grid[i][j]
                else:
                    f[j] = min(f[j - 1], f[j]) + grid[i][j]
        return f[col - 1]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
