#! /usr/local/bin/python3

# https://www.lintcode.com/problem/build-post-office-ii/
# https://leetcode.com/problems/shortest-distance-from-all-buildings/
# Example
# 给出一个二维的网格，每一格可以代表墙 2 ，房子 1，以及空 0 (用数字0,1,2来表示)，在网格中找到一个位置去建立邮局，使得所有的房子到邮局的距离和是最小的。
# 返回所有房子到邮局的最小距离和，如果没有地方建立邮局，则返回-1.
#
# 样例
# 给出一个网格：
#
# 0 1 0 0 0
# 1 0 0 2 1
# 0 1 0 0 0
# 返回 8，你可以在(1,1)处建立邮局 (在(1,1)处建立邮局，所有房子到邮局的距离是最近的)。
#
# 挑战
# 在O(n^3)内的时间复杂度解决此问题。
#
# 注意事项
# 你不能穿过房子和墙，只能穿过空地。
# 你只能在空地建立邮局。

"""
Algo: BFS
D.S.:

Solution:
Search space from each house, when reach a space, increment #houses reaches to this space and increase the distance
Time: O(mn * mn)
Space: O(mn)

Corner cases:
"""

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # write your code here
        if not grid or not len(grid):
            return -1

        import sys

        m, n = len(grid), len(grid[0])
        numHouses = [[0 for _ in range(n)] for _ in range(m)]
        dist = [[0 for _ in range(n)] for _ in range(m)]

        ttlHouse = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ttlHouse += 1
                    # from house to find empty space
                    self.bfs(i, j, grid, numHouses, dist)
        res = sys.maxsize
        for i in range(m):
            for j in range(n):
                if numHouses[i][j] == ttlHouse and dist[i][j] < res:
                    res = dist[i][j]
        return res if res < sys.maxsize else -1

    def bfs(self, i, j, grid, numHouses, dist):
        # starting from a house to find all possible empty space
        # increment numHouses and add dist
        from collections import deque
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        # mark True when put in queue
        visited[i][j] = True
        q = deque([(i, j, 0)]) # 0 is dist, dist to source, starting from 0
        while q:
            (x, y, d) = q.popleft()

            for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    # only enqueue empty spaces
                    if grid[nx][ny] == 0:
                        numHouses[nx][ny] += 1
                        q.append((nx, ny, d + 1))
                        dist[nx][ny] += d + 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
