#! /usr/local/bin/python3

# https://leetcode.com/problems/number-of-distinct-islands-ii/
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands. An island is considered to be the same as another
# if they have the same shape, or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction or up/down direction).
#
# Example 1:
# 11000
# 10000
# 00001
# 00011
# Given the above grid map, return 1.
#
# Notice that:
# 11
# 1
# and
#  1
# 11
# are considered same island shapes. Because if we make a 180 degrees clockwise rotation on the first island, then two islands will have the same shapes.
# Example 2:
# 11100
# 10001
# 01001
# 01110
# Given the above grid map, return 2.
#
# Here are the two distinct islands:
# 111
# 1
# and
# 1
# 1
#
# Notice that:
# 111
# 1
# and
# 1
# 111
# are considered same island shapes. Because if we flip the first array in the up/down direction, then they have the same shapes.
# Note: The length of each dimension in the given grid does not exceed 50.

"""
Algo:
D.S.:

Solution1:

BFS 暴力rescale 形状，并遍历所有的可能性

set 可以hash list of strings, 不能hash list of list

形状变形
t1 = tuple(rows)
t2 = tuple(rows[::-1])
t3 = tuple([s[::-1] for s in rows])
t4 = tuple([s[::-1] for s in rows[::-1]])

t5 = tuple(cols)
t6 = tuple(cols[::-1])
t7 = tuple([s[::-1] for s in cols])
t8 = tuple([s[::-1] for s in cols[::-1]])

t1 111
   001
t2 001
   111
t3 111
   100
t4 100
   111

t5 10
   10
   11
t6 11
   10
   10
t7 01
   01
   11
t8 11
   01
   01

为什么取到形状之后要把-1变回0
01110
01000
11011
11000
11110
在这个例子中，一个范围里有2个岛

Solution2:
Canonical Hash Method to identify unique shape
# # TODO: syntax not pass python3 OJ
Corner cases:
"""
class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        row, col = len(grid), len(grid[0])

        shape_set = set()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    # start bfs to collect a shape
                    rows, cols = self.bfs(i, j, grid)
                    self.validate_new_shape(rows, cols, shape_set)
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
        rows_present = []
        cols_present = []

        for i in range(top, bottom + 1):
            row = ""
            for j in range(left, right + 1):
                if grid[i][j] == -1:
                    row += '1'
                else:
                    row += '0'
            rows_present.append(row)

        for j in range(left, right + 1):
            col = ""
            for i in range(top, bottom + 1):
                if grid[i][j] == -1:
                    col += '1'
                    # IMPORTANT to change to 0
                    grid[i][j] = 0
                else:
                    col += '0'
            cols_present.append(col)

        return rows_present, cols_present

    def validate_new_shape(self, rows, cols, shape_set):
        t1 = tuple(rows)
        t2 = tuple(rows[::-1])
        t3 = tuple([s[::-1] for s in rows])
        t4 = tuple([s[::-1] for s in rows[::-1]])

        t5 = tuple(cols)
        t6 = tuple(cols[::-1])
        t7 = tuple([s[::-1] for s in cols])
        t8 = tuple([s[::-1] for s in cols[::-1]])

        if t1 in shape_set: return
        if t2 in shape_set: return
        if t3 in shape_set: return
        if t4 in shape_set: return
        if t5 in shape_set: return
        if t6 in shape_set: return
        if t7 in shape_set: return
        if t8 in shape_set: return

        shape_set.add(t1)# Test Cases
if __name__ == "__main__":
    solution = Solution()
