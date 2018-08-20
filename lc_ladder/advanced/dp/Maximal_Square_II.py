#! /usr/local/bin/python3

# https://www.lintcode.com/problem/maximal-square-ii/my-submissions
# Example

# Given a 2D binary matrix filled with 0's and 1's, find the largest square which diagonal is all 1 and others is 0.
#
# Example
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 0 1 0
# 1 1 0 0 1
# 1 0 0 1 0
# Return 9
#
# Notice
# Only consider the main diagonal situation.

"""
Algo:
D.S.:

Solution:


Corner cases:
"""
class Solution:
    """
    @param matrix: a matrix of 0 an 1
    @return: an integer
    """
    def maxSquare2(self, matrix):
        # write your code here
        res = 0
        if not matrix or not matrix[0]:
            return res

        row = len(matrix)
        col = len(matrix[0])
        f = [[0] * col for i in range(row)]
        u = [[0] * col for i in range(row)]
        l = [[0] * col for i in range(row)]

        length = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    f[i][j] = 0
                    u[i][j] = 1 # how many 0 from up (including itself)
                    l[i][j] = 1 # how many 0 from left (including itself)
                    if i > 0:
                        u[i][j] = u[i - 1][j] + 1
                    if j > 0:
                        l[i][j] = l[i][j - 1] + 1
                else:
                    u[i][j] = 0
                    l[i][j] = 0
                    if i > 0 and j > 0:
                        f[i][j] = min(f[i - 1][j - 1], min(l[i][j - 1], u[i - 1][j])) + 1
                    else:
                        f[i][j] = 1
                length = max(length, f[i][j])

        return length ** 2

# Test Cases
if __name__ == "__main__":
    solution = Solution()
