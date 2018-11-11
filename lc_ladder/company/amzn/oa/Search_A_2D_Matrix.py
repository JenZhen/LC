#! /usr/local/bin/python3

# Requirement
# Example
# 写出一个高效的算法来搜索 m × n矩阵中的值。
#
# 这个矩阵具有以下特性：
#
# 每行中的整数从左到右是排序的。
# 每行的第一个数大于上一行的最后一个整数。
# 样例
# 考虑下列矩阵：
#
# [
#   [1, 3, 5, 7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# 给出 target = 3，返回 true
#
# 挑战
# O(log(n) + log(m)) 时间复杂度

"""
Algo: Binary Search
D.S.:

Solution:
Time: O(log(n) + log(m))


Corner cases:
"""

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0] or target is None:
            return False
        m, n = len(matrix), len(matrix[0])
        # search which row target is
        l, r = 0, m - 1
        row, col = -1, -1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        if matrix[l][0] <= target <= matrix[l][n - 1]:
            row = l
        if matrix[r][0] <= target <= matrix[r][n - 1]:
            row = r
        if row == -1:
            return False
        # serach which col target is
        l, r = 0, n - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        if matrix[row][l] == target or matrix[row][r] == target:
            return True
        return False

# Test Cases
if __name__ == "__main__":
    solution = Solution()
