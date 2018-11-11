#! /usr/local/bin/python3

# Requirement
# Example

# 1479. 能否到达终点
# 给一个大小为 m*n 的map，1 代表空地，0 代表障碍物，9代表终点。请问如果你从 (0, 0) 开始能否到达终点？
#
# 样例
# Input:[[1,1,1],[1,1,1],[1,1,9]]
# Output:true

"""
Algo: BFS deque implemneted queue
D.S.:

Solution:
BFS -- can reach from 4 directions


Corner cases:
"""

class Solution:
    """
    @param map: the map
    @return: can you reach the endpoint
    """
    def reachEndpoint(self, map):
        # Write your code here
        if not map:
            return False

        if map[0][0] == 0:
            return False
        if map[0][0] == 9:
            return False

        m, n = len(map), len(map[0])
        visited = [[False for j in range(n)] for i in range(m)]
        from collections import deque
        q = deque([(0, 0)])
        visited[0][0] = True
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        def inBoundry(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        while len(q):
            (curx, cury) = q.popleft()
            for d in dirs:
                newx, newy = curx + d[0], cury + d[1]
                if inBoundry(newx, newy):
                    if map[newx][newy] == 9:
                        return True
                    elif not visited[newx][newy] and map[newx][newy] == 1:
                        q.append((newx, newy))
                        visited[newx][newy] = True
        return False

# Test Cases
if __name__ == "__main__":
    solution = Solution()
