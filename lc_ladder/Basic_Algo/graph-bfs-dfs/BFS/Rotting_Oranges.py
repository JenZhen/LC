#! /usr/local/bin/python3

# https://leetcode.com/problems/rotting-oranges/submissions/
# Example
# In a given grid, each cell can have one of three values:
#
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
# Example 1:
#
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:
#
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
#
# Note:
#
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.
"""
Algo: BFS 数层
D.S.:

Solution:
注意 Corner cases:
- 有剩余橘子
- 一开始就没有橘子

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if self.count_of_fresh(grid) == 0:
            return 0
        row, col = len(grid), len(grid[0])
        q = collections.deque([])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        res = 0
        while q:
            (x, y, step) = q.popleft()
            res = max(res, step)
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col:
                    if grid[nx][ny] == 1:
                        q.append((nx, ny, step + 1))
                        grid[nx][ny] = -1
        if self.count_of_fresh(grid) != 0:
            return -1
        return res

    def count_of_fresh(self, grid):
        row, col = len(grid), len(grid[0])
        cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    cnt += 1
        return cnt


# Test Cases
if __name__ == "__main__":
    solution = Solution()
