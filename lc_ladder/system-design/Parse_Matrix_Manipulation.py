#!/usr/local/bin/python3

# https://www.lintcode.com/problem/sparse-matrix-multiplication/description?_from=ladder&&fromId=8
# Example
#
# 给定两个 稀疏矩阵 A 和 B，返回AB的结果。
# 您可以假设A的列数等于B的行数。
#
# 样例
# A = [
#    [ 1, 0, 0],
#    [-1, 0, 3]
# ]
#
# B = [
#    [ 7, 0, 0 ],
#    [ 0, 0, 0 ],
#    [ 0, 0, 1 ]
# ]
#
#
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |

"""
Solution:
https://en.wikipedia.org/wiki/Sparse_matrix
注意，parse matrix 计算不同于矩阵相乘

Corner cases:
"""

class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        if not A or not len(A) or not len(A[0]) or \
            not B or not len(B) or not len(B[0]):
                return None
        rowA = len(A)
        colA = len(A[0])
        rowB = len(B)
        colB = len(B[0])
        if colA != rowB:
            return None

        res = [[0 for _ in range(colB)] for _ in range(rowA)]
        for i in range(rowA):
            for j in range(colA):
                for l in range(colB):
                    res[i][l] += A[i][j] * B[j][l]
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
