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
Algo: DP
D.S.:

Solution:
Time: O(mn)
Space: O(mn * 3) or O(n * 3 * 2) keep 2 rows and use 3 extra types of space

Solution1： regular way; Solution2: 滚动数组
DP 分析
1. 状态
f[i][j]：以i, j 作为正方形右下角可以扩展的最大边长
up[i][j]: 以i, j 作为底，向上0能延长多少（包括[i][j]位置）
left[i][j]: 以i, j 作为最右，向左0能延长多少（包括[i][j]位置）
2. 方程
if matrix[i][j] == 0：
    f[i][j] = 0
    left[i][j] = left[i][j - 1] + 1
    up[i][j] = up[i - 1][j] + 1
else:
    f[i][j] = min(up[i - 1][j], left[i][j - 1], f[i - 1][j - 1]) +  1
    left[i][j] = 0
    up[i][j] = 0

考虑滚动数组 Space O(col)
if matrix[i % 2][j] == 1：
    f[i % 2][j] = min(up[i - 1） % 2][j], left[i % 2][j - 1], f[(i - 1) % 2][j - 1]) + 1
    left[i % 2][j] = left[i % 2][j - 1]
    up[i % 2][j] = up[(i - 1) % 2][j] + 1
else:
    f[i % 2][j] = 0
    left[i% 2][j] = 0
    up[i % 2][j] = 0
当矩阵值为1时，左，上，左上角，的最小值决定f[i][j]的值有关，再加上1

3. 初始化
f[i][0] = matrix[i][0] #第一列
f[0][j] = matrix[0][j] #第一行
考虑滚动数组，只需要init first row
4. 答案
max(f[i][j]) ** 2

Corner cases:
"""
class Solution1:
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


class Solution2:
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
        f = [[0] * col for i in range(2)]
        u = [[0] * col for i in range(2)]
        l = [[0] * col for i in range(2)]

        length = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    f[i % 2][j] = 0
                    u[i % 2][j] = 1 # how many 0 from up (including itself)
                    l[i % 2][j] = 1 # how many 0 from left (including itself)
                    if i > 0:
                        u[i % 2][j] = u[(i - 1) % 2][j] + 1
                    if j > 0:
                        l[i % 2][j] = l[i % 2][j - 1] + 1
                else:
                    u[i % 2][j] = 0
                    l[i % 2][j] = 0
                    if i > 0 and j > 0:
                        f[i % 2][j] = min(f[(i - 1) % 2][j - 1], min(l[i % 2][j - 1], u[(i - 1) % 2][j])) + 1
                    else:
                        f[i % 2][j] = 1
                length = max(length, f[i % 2][j])

        return length ** 2
# Test Cases
if __name__ == "__main__":
    solution = Solution()
