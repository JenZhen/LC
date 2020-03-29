#! /usr/local/bin/python3

# https://www.lintcode.com/problem/submatrix-sum/description?_from=ladder&&fromId=4
# Example
# 给定一个整数矩阵，请找出一个子矩阵，使得其数字之和等于0.输出答案时，请返回左上数字和右下数字的坐标。
#
# 样例
# 给定矩阵
#
# [
#   [1 ,5 ,7],
#   [3 ,7 ,-8],
#   [4 ,-8 ,9],
# ]
# 返回 [(1,1), (2,2)]
#
# 挑战
# O(n3) 时间复杂度。

"""
Algo: PreSum 思想
D.S.: 1D扩展到2D

Solution:
o(n ^ 3)

[
  [1 ,5 ,7],
  [3 ,7 ,-8],
  [4 ,-8 ,9],
]
pre-sum array/matrix要补0，一遍方便计算
[
  [0, 0, 0, 0]
  [0, 1, 6, 13],
  [0, 4, 16,15],
  [0, 8, 12,20],
]

Corner cases:
"""

class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrixSum(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return None
        res = []
        m, n = len(matrix), len(matrix[0])
        # First row, col all 0
        # Note do not use [0] * n!!
        sumM = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # Populate inner elements
        for i in range(m):
            for j in range(n):
                sumM[i + 1][j + 1] = sumM[i][j + 1] + sumM[i + 1][j] + matrix[i][j] - sumM[i][j]
        for startRow in range(m):
            for endRow in range(startRow + 1, m + 1):
                dic = {}
                for col in range(n + 1):
                    area = sumM[endRow][col] - sumM[startRow][col]
                    if area not in dic:
                        dic[area] = col
                    else:
                        preCol = dic[area]
                        res.append((startRow, preCol))
                        res.append((endRow - 1, col - 1))
                        return res
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
