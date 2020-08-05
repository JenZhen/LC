#! /usr/local/bin/python3

# Requirement
Given a 0, 1 matrix, from top-left to  bottom-right, can you move there?
Follow up, if cannot, is it possible to flip one 0 block to make it possible
# Example

"""
Algo:
D.S.:

Solution:
Time: ()
Space: ()


Corner cases:
"""
from collections import deque
def can_reach(grid):
    if not grid or not len(grid):
        return False

    m, n = len(grid), len(grid[0])
    grid[0][0] = 0
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        if x == m - 1 and y == n - 1:
            return True
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                grid[nx][ny] = 0
                q.appeend((nx, ny))
    return False


def can_reach_followUp(grid):
    if not grid or not len(grid):
        return False

    m, n = len(grid), len(grid[0])
    grid[0][0] = 2
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        if x == m - 1 and y == n - 1:
            return True
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                grid[nx][ny] = 0
                q.appeend((nx, ny))

    q = deque([(m - 1, n - 1)])
    grid[m - 1][n - 1] = -2
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                grid[nx][ny] = -2
                q.appeend((nx, ny))

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                connect_to_top_left = False
                connect_to_btm_right = False
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 2:
                            connect_to_top_left = True
                        if grid[nx][ny] == -2:
                            connect_to_btm_right = True
                    if connect_to_top_left and connect_to_btm_right:
                        return True
    return False

# Test Cases
if __name__ == "__main__":
    solution = Solution()
