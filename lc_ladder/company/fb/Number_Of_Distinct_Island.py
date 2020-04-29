#! /usr/local/bin/python3

# https://leetcode.com/problems/number-of-distinct-islands/submissions/
# Example
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the same as another
# if and only if one island can be translated (and not rotated or reflected) to equal the other.
#
# Example 1:
# 11000
# 11000
# 00011
# 00011
# Given the above grid map, return 1.
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.
#
# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered different island shapes, because we do not consider reflection / rotation.
# Note: The length of each dimension in the given grid does not exceed 50.

"""
Algo BFS
D.S.:

Solution:
tuple of strings can be used as key in set
Same as number of distinct island_ii
因为不需要 翻转，所以只需要 按照行 来记录形状

Time: O(MN)
Time: O(MN)
Corner cases:
"""

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        row, col = len(grid), len(grid[0])

        shape_set = set()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    # start bfs to collect a shape
                    shape = self.bfs(i, j, grid)
                    self.validate_new_shape(shape, shape_set)
        return len(shape_set)

    def bfs(self, start_x, start_y, grid):
        row, col = len(grid), len(grid[0])

        # prepare for this shape
        # init boundry
        top, bottom, left, right = start_x, start_x, start_y, start_y

        # prepare for bfs queue
        q = collections.deque([(start_x, start_y)])
        grid[start_x][start_y] = -1 # flip value to not to visit again

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q:
            (cur_x, cur_y) = q.popleft()

            # update shape boundry
            top = min(top, cur_x)
            bottom = max(bottom, cur_x)
            left = min(left, cur_y)
            right = max(right, cur_y)

            for (dx, dy) in dirs:
                new_x, new_y = cur_x + dx, cur_y + dy
                # check boundry
                if 0 <= new_x < row and 0 <= new_y < col:
                    if grid[new_x][new_y] == 1:
                        # enqueue and flip value
                        q.append((new_x, new_y))
                        grid[new_x][new_y] = -1 # change to -1 not 0 so it can be identified later

        # when a shape completed (at the end of a bfs), collect shape
        # search in refined boundry
        shape = []

        for i in range(top, bottom + 1):
            row = ""
            for j in range(left, right + 1):
                if grid[i][j] == -1:
                    row += '1'
                    # IMPORTANT to change to 0
                    grid[i][j] = 0
                else:
                    row += '0'
            shape.append(row)
        return shape

    def validate_new_shape(self, shape, shape_set):
        t = tuple(shape)
        if t in shape_set: return
        shape_set.add(t)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
