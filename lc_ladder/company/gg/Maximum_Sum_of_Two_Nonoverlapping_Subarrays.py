#! /usr/local/bin/python3

# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
# Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays,
# which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)
#
# Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:
# 0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
# 0 <= j < j + M - 1 < i < i + L - 1 < A.length.
#
# Example 1:
# Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
# Example 2:
# Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
# Example 3:
# Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
#
# Note:
# L >= 1
# M >= 1
# L + M <= A.length <= 1000
# 0 <= A[i] <= 1000

"""
Algo: Sliding widow, prefix sum
D.S.:

Solution:
Time: O(n)
Space: O(n)
[3,8,1,3,2,1,8,9,0]
L = 3
M = 2
       0,  1,  2,  3,  4,  5,  6,  7,  8
A     [3,  8,  1,  3,  2,  1,  8,  9,  0]
L_sum [0,  0,  12, 12, 6,  6,  11, 18, 17]
L_max [0,  0,  12, 12, 12, 12, 12, 18, 18]
L_max [18, 18, 18, 18, 18, 18, 18, 18, 17]
M_max [0,  11, 9,  4,  5,  3,  9,  17,  9]
Corner cases:
"""

import sys
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if not A or len(A) < L + M:
            return 0
        n = len(A)
        L_sum = [0] * n
        L_left_max = [0] * n
        L_right_max = [0] * n
        M_sum = [0] * n

        for i in range(L - 1, n):
            if i == L - 1:
                L_sum[i] = sum(A[:L])
            else:
                L_sum[i] = L_sum[i - 1] + A[i] - A[i - L]
        for i in range(n):
            if i == 0:
                L_left_max[i] = L_sum[i]
            else:
                L_left_max[i] = max(L_sum[i], L_left_max[i - 1])
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                L_right_max[i] = L_sum[i]
            else:
                L_right_max[i] = max(L_sum[i], L_right_max[i + 1])
        for i in range(M - 1, n):
            if i == M - 1:
                M_sum[i] = sum(A[:M])
            else:
                M_sum[i] = M_sum[i - 1] + A[i] - A[i - M]

        res = -sys.maxsize
        for i in range(n):
            if i - M >= 0:
                res = max(res, M_sum[i] + L_left_max[i - M])
            if i + L < n:
                res = max(res, M_sum[i] + L_right_max[i + L])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
