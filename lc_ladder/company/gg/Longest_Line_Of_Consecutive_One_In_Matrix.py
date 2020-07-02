#! /usr/local/bin/python3

# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/submissions/
# Example
# Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
# Example:
# Input:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# Output: 3
# Hint: The number of elements in the given matrix will not exceed 10,000.
"""
Algo: DP
D.S.:

Solution:
Time: O(N^2)
Space: O(N^2)

Corner cases:
"""

class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M or not len(M):
            return 0

        m, n = len(M), len(M[0])
        dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(m)]

        # dirs up, left, up-left, up-right
        dirs = [(-1, 0), (0, -1), (-1, -1), (-1, 1)]
        res = 0
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    for idx in range(len(dirs)):
                        (dx, dy) = dirs[idx]
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            if M[nx][ny] == 1:
                                dp[i][j][idx] = dp[nx][ny][idx] + 1
                            else:
                                dp[i][j][idx] = 1
                        else:
                            dp[i][j][idx] = 1
                        res = max(res, dp[i][j][idx])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
