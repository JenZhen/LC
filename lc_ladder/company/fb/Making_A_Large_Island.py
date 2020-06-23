#! /usr/local/bin/python3

# https://leetcode.com/problems/making-a-large-island/submissions/
# Example
# In a 2D grid of 0s and 1s, we change at most one 0 to a 1.
# After, what is the size of the largest island? (An island is a 4-directionally connected group of 1s).
#
# Example 1:
# Input: [[1, 0], [0, 1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
#
# Example 2:
# Input: [[1, 1], [1, 0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
#
# Example 3:
# Input: [[1, 1], [1, 1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
#
# Notes:
#
# 1 <= grid.length = grid[0].length <= 50.
# 0 <= grid[i][j] <= 1.
"""
Algo: UnionFind
D.S.:
Solution:
UF 记录每个连通分量的大小

Time: O(mn)
Space: O(mn)

Corner cases:
[[0,0],[0,0]] --> 1
[[1,1],[1,1]] --> 4 这是需要记录当前最大的岛，或是任意一点的根对应的大小
"""


class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    uf.update_size(i * n + j, 1)
                    # 跟上一行合并
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        uf.union(i * n + j, (i - 1) * n + j)
                    # 跟左一列合并
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        uf.union(i * n + j, i * n + j - 1)
        print(uf.father)
        res = 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    size_map = {}
                    for dx, dy in dirs:
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            root = uf.find(nx * n + ny)
                            size = uf.get_size(root)
                            size_map[root] = size

                    sum = 0
                    for root, size in size_map.items():
                        sum += size
                    sum += 1
                    res = max(res, sum)
        if res == 0:
            return uf.get_maxsize()
        return res

class UnionFind:
    def __init__(self, capacity):
        self.father = [i for i in range(capacity)]
        self.size = [0 for _ in range(capacity)]
        self.maxsize = 0

    def find(self, node):
        if self.father[node] == node:
            return node

        self.father[node] = self.find(self.father[node])
        return self.father[node]

    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root != b_root:
            self.father[a_root] = b_root
            self.size[b_root] += self.size[a_root]
            self.maxsize = max(self.maxsize, self.size[b_root])

    def get_size(self, node):
        return self.size[node]

    def update_size(self, node, new_size):
        self.size[node] = new_size
        self.maxsize = max(self.maxsize, new_size)

    def get_maxsize(self):
        return self.maxsize
# Test Cases
if __name__ == "__main__":
    solution = Solution()
