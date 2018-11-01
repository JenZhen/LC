#! /usr/local/bin/python3

# /Users/zhenzhen/Documents/src/LC/lc_ladder/advanced/follow-up/Zigzag_Iterator_II.py
# Example
# Given an array of n * m matrix, and a moving matrix window (size k * k), move the window from top left to botton right at each iteration, find the maximum sum inside the window at each moving.
# Return 0 if the answer does not exist.
#
# Example
# For matrix
#
# [
#   [1, 5, 3],
#   [3, 2, 1],
#   [4, 1, 9],
# ]
# The moving window size k = 2.
# return 13.
#
# At first the window is at the start of the array like this
#
# [
#   [|1, 5|, 3],
#   [|3, 2|, 1],
#   [4, 1, 9],
# ]
# ,get the sum 11;
# then the window move one step forward.
#
# [
#   [1, |5, 3|],
#   [3, |2, 1|],
#   [4, 1, 9],
# ]
# ,get the sum 11;
# then the window move one step forward again.
#
# [
#   [1, 5, 3],
#   [|3, 2|, 1],
#   [|4, 1|, 9],
# ]
# ,get the sum 10;
# then the window move one step forward again.
#
# [
#   [1, 5, 3],
#   [3, |2, 1|],
#   [4, |1, 9|],
# ]
# ,get the sum 13;
# SO finally, get the maximum from all the sum which is 13.
#
# Challenge
# O(n^2) time.

"""
Algo:
D.S.:

Solution:
Time O(n^2)
presum 矩阵构建方法 方法和 submatrix-sum 完全一样
因为K的长度的确定的，所以减少了一维复杂度

Corner cases:
k 大于matrix的长或宽
"""

class Solution:
    """
    @param matrix: an integer array of n * m matrix
    @param k: An integer
    @return: the maximum number
    """
    def maxSlidingMatrix(self, matrix, k):
        # write your code here
        if not matrix or not matrix[0] or not k:
            return 0
        import sys
        res = -sys.maxsize
        m = len(matrix)
        n = len(matrix[0])
        if k > m or k > n:
            return 0
        # build presumMatrix of size m + 1 * n + 1
        sumM = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # populate presumMatrix value
        for i in range(m):
            for j in range(n):
                sumM[i + 1][j + 1] = sumM[i][j + 1] + sumM[i + 1][j] + matrix[i][j] - sumM[i][j]
        # Build iterate sumM
        # stRow = 0 # endRow = stRow + k
        # stCol = 0 # endCol = endCol + k
        for endRow in range(k, m + 1):
            for endCol in range(k, n + 1):
                stRow = endRow - k
                stCol = endCol - k
                ttl = sumM[endRow][endCol] - sumM[stRow][endCol] - sumM[endRow][stCol] + sumM[stRow][stCol]
                if ttl > res:
                    res = ttl
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
