#! /usr/local/bin/python3

# https://www.lintcode.com/problem/maximal-rectangle/description
# Given a 2D boolean matrix filled with False and True, find the largest rectangle containing all True and return its area.
# Example
"""
[
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1]
]
Return 6
"""

"""
Algo:
D.S.: Monotonous Stack

Solution1:
Original matrix
[
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1]
]
step1:
hGrid: 纵向到点i, j能有多深 （多加一列初设为0，以后用）
[
  [1, 1, 0, 0, 1，0],
  [0, 2, 0, 0, 2，0],
  [0, 0, 1, 1, 3，0],
  [0, 0, 2, 2, 4，0],
  [0, 0, 0, 0, 5，0] # for exmaple, 5 means at this point, 纵向能有5的高度
]
step2:
用monotonous stack来计算在点i, j位置，固定hGrid[i][j]能有多宽
每个点都要过一遍，但是只能以行为为单位来操作

Time: O(mn)
Space: O(mn)

Solution2:
Optimizaton of Solution1: using less Space
-- realizing that when calculating step1, only use a row before; when calculating getMaxAreaPerRow, only use current row.
We can maintain only 1 row
Time: O(mn)
Space: O(n + 1)

Solution3:
# TODO: DP solution

Corner cases:
"""

class Solution1:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        hGrid = [[0 for j in range(n + 1)] for i in range(m)] # m row n + 1 col

        # populate hGrid using matrix value
        # leave last col as 0
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    hGrid[i][j] = 0
                else:
                    if i == 0:
                        hGrid[i][j] = 1
                    else:
                        hGrid[i][j] = hGrid[i - 1][j] + 1

        for i in range(m):
            res = max(res, self.getMaxAreaPerRow(hGrid[i]))
        return res

    # This is the template from Largest_Rectangle_in_Histogram.py
    def getMaxAreaPerRow(self, row):
        stack = []
        maxAraea = 0
        res = 0
        for i in range(len(row)): # n + 1
            curHeight = row[i]
            while len(stack) and curHeight <= row[stack[-1]]:
                h = row[stack.pop()]
                w = i if (len(stack) == 0) else i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
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
        res = 0
        m, n = len(matrix), len(matrix[0])
        hRow = [0 for j in range(n + 1)] # a row of n + 1 col

        # populate hGrid using matrix value
        # leave last col as 0
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    hRow[j] = 0
                else:
                    if i == 0:
                        hRow[j] = 1
                    else:
                        hRow[j] = hRow[j] + 1
            res = max(res, self.getMaxAreaPerRow(hRow))
        return res

    # This is the template from Largest_Rectangle_in_Histogram.py
    def getMaxAreaPerRow(self, row):
        stack = []
        maxAraea = 0
        res = 0
        for i in range(len(row)): # n + 1
            curHeight = row[i]
            while len(stack) and curHeight <= row[stack[-1]]:
                h = row[stack.pop()]
                w = i if (len(stack) == 0) else i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res

# Test Cases
if __name__ == "__main__":
    testCases = [
        [
          [1, 1, 0, 0, 1],
          [0, 1, 0, 0, 1],
          [0, 0, 1, 1, 1],
          [0, 0, 1, 1, 1],
          [0, 0, 0, 0, 1]
        ],

    ]
    s1 = Solution1()
    s2 = Solution2()
    for matrix in testCases:
        res1 = s1.maximalRectangle(matrix)
        print("res1: %s" %res1)
        res2 = s2.maximalRectangle(matrix)
        print("res2: %s" %res2)
