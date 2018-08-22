#! /usr/local/bin/python3

# https://www.lintcode.com/problem/longest-continuous-increasing-subsequence-ii/description
# Example -- 从山顶滑雪问题， 最长下山路径
# Give you an integer matrix (with row size n, column size m)，find the longest increasing continuous subsequence in this matrix. (The definition of the longest increasing continuous subsequence here can start at any row or column and go up/down/right/left any direction).
#
# Example
# Given a matrix:
#
# [
#   [1 ,2 ,3 ,4 ,5],
#   [16,17,24,23,6],
#   [15,18,25,22,7],
#   [14,19,20,21,8],
#   [13,12,11,10,9]
# ]
# return 25
#
# Challenge
# O(nm) time and memory.

"""
Algo: DP
D.S.:

Solution:

难点：
1. 遍历来自四面，不是顺序遍历
2. dp起点不好找，初始状态不好找
所以传统动归思路，不好做。
可以想到的思路, 时间复杂度非常高，如何利用以求解的小问题

i: 0 -> n
    j:  0 -> n
        dfs(i, j) # 以i，j 结尾的最长自序列
dfs(i, j, A):
    for i in range(4):
        nx, ny = i + dx[i], j + dx[j]
        if A[nx][ny] < A[i][j]:
            continue
    return ans

Solution1: 记忆化搜索方式

Solution2: 
Corner cases:
"""

class Solution2:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longestContinuousIncreasingSubsequence2(self, matrix):
        # write your code here
        if not matrix or not matrix[0]:
            return 0

        row = len(matrix)
        col = len(matrix[0])
        seq = []
        for i in range(row):
            for j in range(col):
                seq.append((matrix[i][j], i, j))
        seq.sort()
        print("check seq: %s" %repr(seq))
        res = 1
        LCIS = {} # key: coor, val: LCIS number
        for ele in seq:
            coor = (ele[1], ele[2])
            LCIS[coor] = 1 # init the LCIS is 1
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x = coor[0] + dx
                y = coor[1] + dy
                if x < 0 or x >= row or y < 0 or y >= col:
                    continue
                else:
                    if (x, y) in LCIS and matrix[x][y] < ele[0]:
                        LCIS[coor] = max(LCIS[coor], LCIS[(x, y)] + 1)
                        res = max(res, LCIS[coor])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
