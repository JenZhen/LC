#! /usr/local/bin/python3

# https://lintcode.com/problem/number-of-islands/description
# Example

"""
Algo: BFS
D.S.:

Solution:
Union-Find solution in
/lc_ladder/advanced/data-structure/union-find/

BFS
Time: O(2n) -- each node visted twice, main function once (check if its starting point of bfs)
                                        bfs once

Corner cases:
"""
from collections import deque
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        visited = [[False for j in range(n)] for i in range(m)]

        cnt = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] == False and grid[i][j] == 1:
                    self.bfs(visited, i, j, grid)
                    cnt += 1
        return cnt

    def bfs(self, visited, i, j, grid):
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque([(i, j)])
        visited[i][j] = True

        while len(q):
            cur = q.popleft()
            print("cur: %s" %cur[0])
            for d in dirs:
                print("current dir: %s" %repr(d))
                newx, newy = cur[0] + d[0], cur[1] + d[1]
                # if valid in grid
                if not (0 <= newx < len(grid) and 0 <= newy < len(grid[0])):
                    continue
                if grid[newx][newy] == 0:
                    continue

                if visited[newx][newy] == False:
                    q.append((newx, newy))
                    visited[newx][newy] = True
        return

# Test Cases
if __name__ == "__main__":
    testCases = [
        [[1,1,0,0,0],[0,1,0,0,1],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,1]],
    ]
    s = Solution()
    for t in testCases:
        res = s.numIslands(t)
        print("res: %s" %res)
