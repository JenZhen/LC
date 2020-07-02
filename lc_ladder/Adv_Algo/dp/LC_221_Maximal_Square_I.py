#! /usr/local/bin/python3

# https://www.lintcode.com/problem/maximal-square/my-submissions
# https://leetcode.com/problems/maximal-square/
# Example
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.
#
# Example
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 4.

"""
Algo: DP 滚动数组
D.S.:
小技巧：以matrix[i][j]为右下角

Time: O(mn), Space: O(col)

Solution1 & Solution2: 滚动数组 2行J列

DP 分析
1. 状态
f[i][j]：以i, j 作为正方形右下角可以扩展的最大边长
2. 方程
if matrix[i][j] == 1：
    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) +  1
else:
    f[i][j] = 0

考虑滚动数组 Space O(col)
if matrix[i % 2][j] == 1：
    f[i % 2][j] = min(f[（i - 1） % 2][j], f[i % 2][j - 1], f[(i - 1) % 2][j - 1]) + 1
else:
    f[i % 2][j] = 0
当矩阵值为1时，左，上，左上角，的最小值决定f[i][j]的值有关，再加上1

3. 初始化
f[i][0] = matrix[i][0] #第一列
f[0][j] = matrix[0][j] #第一行
考虑滚动数组，只需要init first row
4. 答案
max(f[i][j]) ** 2

Solution3: 利用up, left 数组来找向上，向左最多能延伸多长 （方法和maximal_square_II.py, maximal_rectangle.py一样）

DP 分析
1. 状态
f[i][j]：以i, j 作为正方形右下角可以扩展的最大边长
up[i][j]: 以i, j 作为底，向上1能延长多少（包括[i][j]位置）
left[i][j]: 以i, j 作为最右，向左1能延长多少（包括[i][j]位置）
2. 方程
if matrix[i][j] == 1：
    f[i][j] = min(up[i - 1][j], left[i][j - 1], f[i - 1][j - 1]) +  1
    left[i][j] = left[i][j - 1] + 1
    up[i][j] = up[i - 1][j] + 1
else:
    f[i][j] = 0
    left[i][j] = 0
    up[i][j] = 0

考虑滚动数组 Space O(col)
if matrix[i % 2][j] == 1：
    f[i % 2][j] = min(up[i - 1） % 2][j], left[i % 2][j - 1], f[(i - 1) % 2][j - 1]) + 1
    left[i % 2][j] = left[i % 2][j - 1] + 1
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
Only one row or one column
[[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]] -> 1
"""

class Solution1:
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



class Solution2:
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
        # f keeps only 2 rows
        f = [[0] * col, [0] * col]
        # init only first row
        for j in range(col):
            f[0][j] = matrix[0][j]
        res = max(f[0])
        for i in range(1, row):
            # default first row
            f[i % 2][0] = matrix[i][0]
            for j in range(1, col):
                if matrix[i][j] == 1:
                    f[i % 2][j] = min(f[(i - 1) % 2][j], f[i % 2][j - 1], f[(i - 1) % 2][j - 1]) + 1
                else:
                    f[i % 2][j] = 0
                res = max(res, f[i % 2][j])
        return res ** 2

# Test Cases
if __name__ == "__main__":
    solution = Solution()
