#! /usr/local/bin/python3

# https://leetcode.com/problems/walls-and-gates/
# Example
# You are given a m x n 2D grid initialized with these three possible values.
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF
# as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
#
# Example:
#
# Given the 2D grid:
#
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
#
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4
"""
Algo: BFS
D.S.:

Solution:
BFS 多个起点一起找， queue里带着节点和距离
同烂橘子是一道题
https://leetcode.com/problems/rotting-oranges/submissions/

Time: O(MN)
Space: O(MN)
Corner cases:
"""
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not len(rooms[0]): return

        INF = (1 << 31) - 1
        row, col = len(rooms), len(rooms[0])
        q = collections.deque([])
        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            x,  y, dist = q.popleft()
            for (dx, dy) in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < col:
                    if rooms[nx][ny] == INF:
                        rooms[nx][ny] = dist + 1
                        q.append((nx, ny, dist + 1))
# Test Cases
if __name__ == "__main__":
    solution = Solution()
