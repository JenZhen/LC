#! /usr/local/bin/python3

# https://leetcode.com/problems/sparse-matrix-multiplication/submissions/
# Example
# Given two sparse matrices A and B, return the result of AB.
# You may assume that A's column number is equal to B's row number.
# Example:
# Input:
#
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]
#
# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]
# Output:
#
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |
"""
Algo:
D.S.:

Solution:

Time: O()
Space: O()
Corner cases:
"""

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ma, na = len(A), len(A[0])
        mb, nb = len(B), len(B[0])
        res = [[None for _ in range(nb)] for _ in range(ma)]
        for i in range(ma):
            for j in range(nb):
                res[i][j] = self._get_value(A, B, i, j)
        return res

    def _get_value(self, A, B, row, col):
        res = 0
        for k in range(len(B)):
            res += A[row][k] * B[k][col]
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
