#! /usr/local/bin/python3

# https://leetcode.com/problems/count-square-submatrices-with-all-ones/submissions/
# Example
# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
# Example 1:
#
# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation:
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# Example 2:
#
# Input: matrix =
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation:
# There are 6 squares of side 1.
# There is 1 square of side 2.
# Total number of squares = 6 + 1 = 7.
#
#
# Constraints:
#
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1
"""
Algo: DP
D.S.:

Solution:
Same as maximal square
Time: O(mn)
Space: O(mn)

Corner cases:
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not len(matrix):
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # init first row and first col
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(m):
            dp[i][0] = matrix[i][0]

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        print(dp)
        res = 0
        for i in range(m):
            for j in range(n):
                res += dp[i][j]
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
