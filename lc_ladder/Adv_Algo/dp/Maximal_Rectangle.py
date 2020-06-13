#! /usr/local/bin/python3

# https://www.lintcode.com/problem/maximal-rectangle/description
# Example
# Given a 2D boolean matrix filled with False and True,
# find the largest rectangle containing all True and return its area.
#
# Example
# Given a matrix:
#
# [
#   [1, 1, 0, 0, 1],
#   [0, 1, 0, 0, 1],
#   [0, 0, 1, 1, 1],
#   [0, 0, 1, 1, 1],
#   [0, 0, 0, 0, 1]
# ]
# return 6.
"""
Algo:
D.S.:

Solution:


Corner cases:
"""

class Solution1:
    # TODO:
    # 不知道为什么不用初始化第一行 也不会越界
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        h = [[0] * col for i in range(row)]
        l = [[0] * col for i in range(row)]
        r = [[col - 1] * col for i in range(row)]

        res = 0
        for i in range(row):
            curLeft = 0
            curRight = col - 1
            for j in range(col):
                if matrix[i][j] == True:
                    h[i][j] = h[i - 1][j] + 1
                    l[i][j] = max(curLeft, l[i - 1][j])
                else:
                    h[i][j] = 0
                    l[i][j] = 0
                    curLeft = j + 1 #j is False, first left True is j + 1 position
            for j in range(col - 1, -1, -1):
                if matrix[i][j] == True:
                    r[i][j] = min(curRight, r[i - 1][j])
                else:
                    r[i][j] = col - 1
                    curRight = j - 1
            for j in range(col):
                res = max(res, (r[i][j] - l[i][j] + 1) * h[i][j])
        return res

class Solution_with_init:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        h = [[0 for _ in range(col)] for _ in range(row)]
        l = [[0 for _ in range(col)] for _ in range(row)]
        r = [[col - 1 for _ in range(col)] for _ in range(row)]

        res = 0
        # init first row
        curLeft = 0
        curRight = col - 1
        for j in range(col):
            if matrix[0][j] == '1':
                h[0][j] = 1
                l[0][j] = curLeft
            else:
                h[0][j] = 0
                l[0][j] = 0
                curLeft = j + 1
        for j in range(col - 1, -1, -1):
            if matrix[0][j] == '1':
                r[0][j] = curRight
            else:
                r[0][j] = col - 1
                curRight = j - 1
        for j in range(col):
            res = max(res, (r[0][j] - l[0][j] + 1) * h[0][j])

        for i in range(1, row):
            curLeft = 0
            curRight = col - 1
            for j in range(col):
                if matrix[i][j] == '1':
                    h[i][j] = h[i - 1][j] + 1
                    l[i][j] = max(curLeft, l[i - 1][j])
                else:
                    h[i][j] = 0
                    l[i][j] = 0
                    curLeft = j + 1 #j is False, first left True is j + 1 position
            for j in range(col - 1, -1, -1):
                if matrix[i][j] == '1':
                    r[i][j] = min(curRight, r[i - 1][j])
                else:
                    r[i][j] = col - 1
                    curRight = j - 1
            for j in range(col):
                res = max(res, (r[i][j] - l[i][j] + 1) * h[i][j])
        print(h)
        print(l)
        print(r)
        return res

class Solution2:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0

        row = len(matrix)
        col = len(matrix[0])

        h = [0] * col
        l = [0] * col
        r = [col - 1] * col

        res = 0
        for i in range(row):
            curLeft = 0
            curRight = col - 1
            for j in range(col):
                if matrix[i][j] == True:
                    h[j] += 1
                    l[j] = max(curLeft, l[j])
                else:
                    h[j] = 0
                    l[j] = 0
                    curLeft = j + 1 #j is False, first left True is j + 1 position
            for j in range(col - 1, -1, -1):
                if matrix[i][j] == True:
                    r[j] = min(curRight, r[j])
                else:
                    r[j] = col - 1
                    curRight = j - 1
            for j in range(col):
                res = max(res, (r[j] - l[j] + 1) * h[j])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
