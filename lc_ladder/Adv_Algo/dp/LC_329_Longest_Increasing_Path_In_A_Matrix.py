#! /usr/local/bin/python3

# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# Example
# Given an integer matrix, find the length of the longest increasing path.
# From each cell, you can either move to four directions: left, right, up or down.
# You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
#
# Example 1:
# Input: nums =
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
# Example 2:
# Input: nums =
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
Algo: DP + DFS
D.S.:

Solution:
重点 常考题
Time: O(mn)
Space: O(mn)

Corner cases:
[[1]] --> 1
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        cache = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, cache, i, j))
        return res

    def dfs(self, matrix, cache, row, col):
        if cache[row][col] != 0:
            return cache[row][col]
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in dirs:
            nx, ny = row + dx, col + dy
            # matrix[nx][ny] < matrix[row][col] or matrix[nx][ny] > matrix[row][col]
            # 都一样
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] < matrix[row][col]:
                cache[row][col] = max(cache[row][col], self.dfs(matrix, cache, nx, ny))
        # this way works for [[1]] corner case
        cache[row][col] += 1
        return cache[row][col]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
