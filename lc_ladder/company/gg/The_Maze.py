#! /usr/local/bin/python3

# https://leetcode.com/problems/the-maze/
# Example
# There is a ball in a maze with empty spaces and walls.
# The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall.
# When the ball stops, it could choose the next direction.
#
# Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.
# The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space.
# You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.
#
# Example 1:
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
#
# Output: true
#
# Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
#
# Example 2:
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)
#
# Output: false
#
# Explanation: There is no way for the ball to stop at the destination.
# Note:
#
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
"""
Algo: BFS
D.S.:

Solution:
Time: O(mn)
Space: O(mn)

Corner cases:
"""
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        q = collections.deque([start])
        visited[start[0]][start[1]] = True
        while q:
            x, y = q.popleft()
            if [x, y] == destination:
                return True
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                # if can move to nx, ny, move to that dir until cannot
                while 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == 0:
                    nx += dx
                    ny += dy
                # when hit wall, take one step back
                nx -= dx
                ny -= dy
                if not visited[nx][ny]:
                    q.append([nx, ny])
                    visited[nx][ny] = True
        return False
# Test Cases
if __name__ == "__main__":
    solution = Solution()
