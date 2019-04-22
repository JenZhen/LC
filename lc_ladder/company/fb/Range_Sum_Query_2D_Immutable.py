#! /usr/local/bin/python3

# https://www.lintcode.com/problem/range-sum-query-2d-immutable/description
# Example
# 给一 二维矩阵,计算由左上角 (row1, col1) 和右下角 (row2, col2) 划定的矩形内元素和.
#
# Example
# 样例1
#
# 输入：
# [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
# sumRegion(2, 1, 4, 3)
# sumRegion(1, 1, 2, 2)
# sumRegion(1, 2, 2, 4)
# 输出：
# 8
# 11
# 12
# 解释：
# 给出矩阵
# [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
# sumRegion(2, 1, 4, 3) = 2 + 0 + 1 + 1 + 0 + 1 + 0 + 3 + 0 = 8
# sumRegion(1, 1, 2, 2) = 6 + 3 + 2 + 0 = 11
# sumRegion(1, 2, 2, 4) = 3 + 2 + 1 + 0 + 1 + 5 = 12
# 样例2
#
# 输入：
# [[3,0],[5,6]]
# sumRegion(0, 0, 0, 1)
# sumRegion(0, 0, 1, 1)
# 输出：
# 3
# 14
# 解释：
# 给出矩阵
# [
#   [3, 0],
#   [5, 6]
# ]
# sumRegion(0, 0, 0, 1) = 3 + 0 = 3
# sumRegion(0, 0, 1, 1) = 3 + 0 + 5 + 6 = 14
# Notice
# 你可以假设矩阵不变
# 对函数 sumRegion 的调用次数有很多次
# 你可以假设 row1 ≤ row2 并且 col1 ≤ col2

"""
Algo:
D.S.:

Solution:


Corner cases:
"""

class NumMatrix:
    """
    @param: matrix: a 2D matrix
    """
    def __init__(self, matrix):
        # do intialization if necessary
        m = len(matrix)
        n = len(matrix[0])
        self.sum = [[0 for _ in range(n)] for _ in range(m)]
        self.sum[0][0] = matrix[0][0]
        for i in range(1, m):
            self.sum[i][0] = self.sum[i - 1][0] + matrix[i][0]
        for j in range(1, n):
            self.sum[0][j] = self.sum[0][j - 1] + matrix[0][j]
        print(self.sum)
        for i in range(1, m):
            for j in range(1, n):
                self.sum[i][j] = matrix[i][j] + self.sum[i - 1][j] + self.sum[i][j - 1] - self.sum[i - 1][j - 1]
        print(self.sum)
    """
    @param: row1: An integer
    @param: col1: An integer
    @param: row2: An integer
    @param: col2: An integer
    @return: An integer
    """
    def sumRegion(self, row1, col1, row2, col2):
        # write your code here
        width = row2 - row1 + 1
        height = col2 - col1 + 1
        top_sum, left_sum, top_left_sum = 0, 0, 0
        # NOTE when row1 == 0 col2 == 0,
        # top_sum, left_sum, top_left_sum = 0, 0, 0
        if row1 == 0 and col1 > 0:
            # only left_sum no top_left_sum, no top_sum
            left_sum = self.sum[row2][col1 - 1]
        elif row1 > 0 and col1 == 0:
            # only top_sum, no top_left_sum, no left_sum
            top_sum = self.sum[row1 - 1][col2]
        elif row1 > 0 and col1 > 0:
            # both greater than 0
            top_left_sum = self.sum[row1 - 1][col1 - 1]
            top_sum = self.sum[row1 - 1][col2]
            left_sum = self.sum[row2][col1 - 1]

        return self.sum[row2][col2] - left_sum - top_sum + top_left_sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
