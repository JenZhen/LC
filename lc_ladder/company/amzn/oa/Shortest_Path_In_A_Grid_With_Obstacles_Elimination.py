#! /usr/local/bin/python3

# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# Example
# Given a m * n grid, where each cell is either 0 (empty) or 1 (obstacle). In one step, you can move up, down, left or right from and to an empty cell.
# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m-1, n-1)
# given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
#
# Example 1:
# Input:
# grid =
# [[0,0,0],
#  [1,1,0],
#  [0,0,0],
#  [0,1,1],
#  [0,0,0]],
# k = 1
# Output: 6
# Explanation:
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
#
# Example 2:
# Input:
# grid =
# [[0,1,1],
#  [1,1,1],
#  [1,0,0]],
# k = 1
# Output: -1
# Explanation:
# We need to eliminate at least two obstacles to find such a walk.
#
# Constraints:
# grid.length == m
# grid[0].length == n
# 1 <= m, n <= 40
# 1 <= k <= m*n
# grid[i][j] == 0 or 1
# grid[0][0] == grid[m-1][n-1] == 0
"""
Algo:
D.S.:

Solution:


Corner cases:
"""

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        row, col = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # 到达X,Y 最少要消除的障碍个数
        min_ob = [[sys.maxsize for _ in range(col)] for _ in range(row)]

        q = collections.deque([(0, 0, 0, 0)]) # x, y, cnt_ob, step
        while q:
            x, y, ob, step = q.popleft()
            if x == row - 1 and y == col - 1:
                return step
            for dx, dy in dirs:
                nx, ny = dx + x, dy + y
                if not (0 <= nx < row and 0 <= ny < col):
                    continue
                nob = ob + grid[nx][ny]
                if nob >= min_ob[nx][ny] or nob > k:
                    continue
                min_ob[nx][ny] = nob
                q.append((nx, ny, nob, step + 1))
        return -1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
