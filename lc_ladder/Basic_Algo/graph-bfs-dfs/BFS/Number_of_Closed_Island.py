#! /usr/local/bin/python3

# https://leetcode.com/problems/number-of-closed-islands/
# Example
# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally
# connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.
#
# Return the number of closed islands.
#
# Example 1:
# Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation:
# Islands in gray are closed because they are completely surrounded by water (group of 1s).
#
# Example 2:
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
#
# Example 3:
# Input: grid = [[1,1,1,1,1,1,1],
#                [1,0,0,0,0,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,1,0,1,0,1],
#                [1,0,1,1,1,0,1],
#                [1,0,0,0,0,0,1],
#                [1,1,1,1,1,1,1]]
# Output: 2
#
# Constraints:
#
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1

"""
Algo: BFS
D.S.:

Solution:
Time: O(mn)
Space: O(mn)

Corner cases:
"""

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        row, col = len(grid), len(grid[0])

        # mark all island connected to border as water
        # start tracing from borders
        for i in range(row):
            for j in [0, col - 1]:
                if grid[i][j] == 0:
                    # if it is land, start to flip all related
                    self.bfs(i, j, grid)

        for i in [0, row - 1]:
            for j in range(col):
                if grid[i][j] == 0:
                    # if it is land, start to flip all related
                    self.bfs(i, j, grid)

        # check from inland to find count of enclosed lands
        cnt = 0
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if grid[i][j] == 0:
                    self.bfs(i, j, grid)
                    cnt += 1
        return cnt

    def bfs(self, start_x, start_y, grid):
        row, col = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = collections.deque([(start_x, start_y)])
        # when enqueue, flip visited land from 0 to 1
        grid[start_x][start_y] = 1
        while q:
            (cur_x, cur_y) = q.popleft()
            for (dx, dy) in dirs:
                new_x, new_y = cur_x + dx, cur_y + dy
                if 0 <= new_x < row and 0 <= new_y < col:
                    if grid[new_x][new_y] == 0:
                        q.append((new_x, new_y))
                        grid[new_x][new_y] = 1
        return

# Test Cases
if __name__ == "__main__":
    solution = Solution()
