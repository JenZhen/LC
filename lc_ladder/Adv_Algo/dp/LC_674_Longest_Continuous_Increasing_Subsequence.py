#! /usr/local/bin/python3

# https://www.lintcode.com/problem/longest-continuous-increasing-subsequence/description
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# Example
# Give an integer array，find the longest increasing continuous subsequence in this array.
#
# An increasing continuous subsequence:
# 要求位置连续，数值不一定连续
#
# Can be from right to left or from left to right.
# Indices of the integers in the subsequence should be continuous.
# Example
# For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.
#
# For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.
#
# Challenge
# O(n) time and O(1) extra space.

"""
Algo:
D.S.:

Solution:
Time: O(n), Space: O(1)

DP 分析
1. 状态
asc[i]: 以i为结尾，最大的递增序列
desc[i]: 以i为结尾，最大的递减序列
2. 方程
asc = asc + 1 if A[i] > A[i - 1] else 1
desc = desc + 1 if A[i] < A[i - 1] else 1

3. 初始化
f[0] = 1 # 到台阶0，1种方式
f[1] = 1 # 到台阶1，1种方式
4. 答案
f[n]


Corner cases:
"""

class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        if not A:
            return 0

        asc, desc = 1, 1
        res = 1
        for i in range(1, len(A)):
            asc = asc + 1 if A[i] > A[i - 1] else 1
            desc = desc + 1 if A[i] < A[i - 1] else 1
            res = max(res, max(asc, desc))
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
