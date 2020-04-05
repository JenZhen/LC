#! /usr/local/bin/python3

# https://leetcode.com/problems/max-area-of-island/
# Example
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally
#  (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
#
# Example 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
#
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.
"""
Algo: BFS
D.S.:

Solution:
Time: O(mn)
Space: O(mn)

Corner cases:
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        maxSize = 0

        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    size = self.bfs(i, j, grid)
                    maxSize = max(size, maxSize)
        return maxSize

    def bfs(self, start_x, start_y, grid):
        row, col = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = collections.deque([(start_x, start_y)])
        # flip cell value to 0 when indx enqueued
        grid[start_x][start_y] = 0
        # size += 1 when enqueue
        size = 1
        while q:
            (cur_x, cur_y) = q.popleft()
            for (dx, dy) in dirs:
                new_x, new_y = cur_x + dx, cur_y + dy
                # check boundry
                if 0 <= new_x < row and 0 <= new_y < col:
                    if grid[new_x][new_y] == 1:
                        size += 1
                        q.append((new_x, new_y))
                        grid[new_x][new_y] = 0
        return size


# Test Cases
if __name__ == "__main__":
    solution = Solution()
