#! /usr/local/bin/python3

# https://www.lintcode.com/problem/maximal-square/my-submissions
# Example
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

Example
For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

"""
Algo:
D.S.:

Solution:


Corner cases:
Only one row or one column
[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]] -> 1
"""

class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # write your code here
        res = 0
        if not matrix or not matrix[0]:
            return res

        row = len(matrix)
        col = len(matrix[0])
        print("r: %s, c: %s" %(row, col))
        nm = [[0] * col for i in range(row)]

        # init first row
        for j in range(col):
            nm[0][j] = matrix[0][j]
            res = max(res, nm[0][j])

        for i in range(row):
            nm[i][0] = matrix[i][0]
            res = max(res, nm[i][0])

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    nm[i][j] = 0
                else:
                    nm[i][j] = min(nm[i-1][j], nm[i][j-1], nm[i-1][j-1]) + 1
                    res = max(res, nm[i][j])
        return res ** 2


# Test Cases
if __name__ == "__main__":
    solution = Solution()
