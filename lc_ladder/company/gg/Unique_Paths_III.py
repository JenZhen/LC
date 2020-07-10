#! /usr/local/bin/python3

# https://leetcode.com/problems/unique-paths-iii/
# On a 2-dimensional grid, there are 4 types of squares:
#
# 1 represents the starting square.  There is exactly one starting square.
# 2 represents the ending square.  There is exactly one ending square.
# 0 represents empty squares we can walk over.
# -1 represents obstacles that we cannot walk over.
# Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
#
#
#
# Example 1:
#
# Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# Output: 2
# Explanation: We have the following two paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
# Example 2:
#
# Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
# Output: 4
# Explanation: We have the following four paths:
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
# Example 3:
#
# Input: [[0,1],[2,0]]
# Output: 0
# Explanation:
# There is no path that walks over every empty square exactly once.
# Note that the starting and ending square can be anywhere in the grid.
#
# Note:
#
# 1 <= grid.length * grid[0].length <= 20
"""
Algo: DFS search, state map
D.S.:

Solution1:
Time: O(4 ^ (mn)) -- 每个格子，都有4个搜索的方向
Space: O(mn) -- grid大小

Solution2：
Time: O((mn) * 2 ^ (mn))
Space: O((mn) * 2 ^ (mn)) -- memo 大小
self.memo = [[[None for _ in range(bitmap_size)] for _ in range(n)] for _ in range(m)] # m * n * bitmap_size
m * n * state_size
memo[x][y][state] 表示在x, y位置，状态是state有几个解
每个格子有2个可能，visited or not visited 共有 2 ^ (mn) 个可能
state 是bitmap 共有 mn 位
例子：（x,y) 位置 是0  在第 y * column + x 位，如果是2, 那么 ...000010 这个第二位mark as 1, 访问后变为0

把所有的memo填充好，需要的时间、空间复杂度就是memo 的大小
O((mn) * 2 ^ (mn))

类似： 943 Find the shortest Superstring

Corner cases:
"""

class Solution1_Naiive:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_x, start_y = None, None
        m, n = len(grid), len(grid[0])
        # note cnt start from 1, start_x, start_y is counted as 1
        cnt = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_x, start_y = i, j
                elif grid[i][j] == 0:
                    cnt += 1
        print(cnt, start_x, start_y)
        return self.dfs(grid, start_x, start_y, cnt)

    def dfs(self, grid, x, y, cnt):
        m, n = len(grid), len(grid[0])
        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == -1:
            return 0

        if grid[x][y] == 2:
            # find exist:
            return 1 if cnt == 0 else 0

        # current position is 0 should continue from here
        grid[x][y] = -1 # mark it as visited (or an obstable)
        path_cnt = self.dfs(grid, x + 1, y, cnt - 1) + self.dfs(grid, x - 1, y, cnt - 1) +  self.dfs(grid, x, y + 1, cnt - 1) + self.dfs(grid, x, y - 1, cnt - 1)
        grid[x][y] = 0
        return path_cnt


class Solution2_DP_Memo:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_x, start_y = None, None
        target_x, target_y = None, None
        m, n = len(grid), len(grid[0])
        target_bitmap = 0
        bitmap_size = 1 << (m * n)
        self.memo = [[[None for _ in range(bitmap_size)] for _ in range(n)] for _ in range(m)] # m * n * bitmap_size

        for i in range(m):
            for j in range(n):
                if grid[i][j] % 2 == 0:
                    target_bitmap |= self.encode(i, j, n)

                if grid[i][j] == 1:
                    start_x, start_y = i, j
                elif grid[i][j] == 2:
                    target_x, target_y = i, j

        return self.dfs(grid, start_x, start_y, target_bitmap)

    def encode(self, x, y, col):
        return 1 << (x * col + y)

    def dfs(self, grid, x, y, target_bitmap):
        m, n = len(grid), len(grid[0])
        if self.memo[x][y][target_bitmap]:
            # if bitmap position at x, y is calculated, return it
            return self.memo[x][y][target_bitmap]

        if grid[x][y] == 2:
            # reach to target
            if target_bitmap == 0:
                # all empty places all visited, find a solution
                return 1
            else:
                return 0

        res = 0
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if target_bitmap & self.encode(nx, ny, n) != 0:
                    # if nx, ny not visited
                    # remove nx, ny digit from target_bitmap
                    res += self.dfs(grid, nx, ny, target_bitmap ^ self.encode(nx, ny, n))
        self.memo[x][y][target_bitmap] = res
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
