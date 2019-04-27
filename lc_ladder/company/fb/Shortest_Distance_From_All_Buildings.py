#! /usr/local/bin/python3

# https://www.lintcode.com/problem/shortest-distance-from-all-buildings/description
# Example
# 你想在一个空旷的土地上盖房子，在最短的距离内到达所有的建筑物。你只能上下左右移动。你得到的是一个二维数组网格的值为0、1或2，其中:
#
# 每一个0标记一个空的土地，你可以自由地通过。
# 每一个1标记一个你不能通过的建筑物。
# 每一个2标记一个你不能通过的障碍。
# 样例
# Example 1
#
# Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# Output: 7
# Explanation:
# In this example, there are three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.
# Example 2
#
# Input: [[1,0],[0,0]]
# Output: 1
# In this example, there is one buildings at (0,0).
# 1 - 0
# |   |
# 0 - 0
# The point (1,0) or (0,1) is an ideal empty land to build a house, as the total travel distance of 1 is minimal. So return 1.

"""
Algo: BFS
D.S.:

Solution:
从房子想空地搜
记录从房子到空地的距离
最后的空地要能让所有的房子都到达

Corner cases:
"""

class Solution:
    """
    @param grid: the 2D grid
    @return: the shortest distance
    """
    def shortestDistance(self, grid):
        # write your code here
        m = len(grid)
        n = len(grid[0])
        self.dist = [[0 for _ in range(n)] for _ in range(m)]
        self.reach_cnt = [[0 for _ in range(n)] for _ in range(m)]
        num_of_houses = 0

        for i in range(m):
            for j in range(n):
                # bfs search from house to all empty places
                if grid[i][j] == 1:
                    num_of_houses += 1
                    self.bfs(i, j, grid)

        print(self.dist)
        import sys
        res = sys.maxsize
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and self.dist[i][j] < res and self.reach_cnt[i][j] == num_of_houses:
                    res = self.dist[i][j]
        return res


    def bfs(self, i, j, grid):
        from collections import deque
        m = len(grid)
        n = len(grid[0])
        q = deque([(i, j, 0)])
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[i][j] == True
        while q:
            curx, cury, curdist = q.popleft()
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx = curx + dx
                ny = cury + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0 and visited[nx][ny] == False:
                    self.dist[nx][ny] += curdist + 1
                    self.reach_cnt[nx][ny] += 1
                    q.append((nx, ny, curdist + 1))
                    visited[nx][ny] = True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
