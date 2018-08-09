#! /usr/local/bin/python3

# https://www.lintcode.com/problem/knight-shortest-path/description
# Example
# Knight can only go this way
# (x + 1, y + 2)
# (x + 1, y - 2)
# (x - 1, y + 2)
# (x - 1, y - 2)
# (x + 2, y + 1)
# (x + 2, y - 1)
# (x - 2, y + 1)
# (x - 2, y - 1)
"""
Algo: BFS
D.S.: deque-implemented queue

Solution:
BFS a grid from source to destination
Time: O(mn) -- nearly all grid element visited once
Space: O(mn) -- for dist grid

Corner cases:
"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import sys
from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if not source or not destination or \
            not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        # dist notes how many step away from source
        dist = [[sys.maxsize for j in range(n)] for i in range(m)]
        dist[source.x][source.y] = 0

        dirs = [(1, 2),
                (1, -2),
                (-1, 2),
                (-1, -2),
                (2, 1),
                (2, -1),
                (-2, 1),
                (-2, -1)]
        q = deque([source])
        while len(q):
            cur = q.popleft()
            for d in dirs:
                newx, newy = cur.x + d[0], cur.y + d[1]
                if 0 <= newx < m and 0 <= newy < n and \
                    grid[newx][newy] != 1 and \
                    dist[newx][newy] > dist[cur.x][cur.y] + 1:
                    q.append(Point(newx, newy))
                    dist[newx][newy] = dist[cur.x][cur.y] + 1
        return -1 if dist[destination.x][destination.y] == sys.maxsize else dist[destination.x][destination.y]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
