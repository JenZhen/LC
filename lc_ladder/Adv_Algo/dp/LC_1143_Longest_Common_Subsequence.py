#! /usr/local/bin/python3

# https://www.lintcode.com/problem/longest-common-subsequence/
# https://leetcode.com/problems/longest-common-subsequence/submissions/
# Example
# 给出两个字符串，找到最长公共子序列(LCS)，返回LCS的长度。
#
# 样例
# 样例 1:
# 	输入:  "ABCD" and "EDCA"
# 	输出:  1
#
# 	解释:
# 	LCS 是 'A' 或  'D' 或 'C'
#
#
# 样例 2:
# 	输入: "ABCD" and "EACB"
# 	输出:  2
#
# 	解释:
# 	LCS 是 "AC"
# 说明
# 最长公共子序列的定义：
#
# 最长公共子序列问题是在一组序列（通常2个）中找到最长公共子序列（注意：不同于子串，LCS不需要是连续的子串）。该问题是典型的计算机科学问题，是文件差异比较程序的基础，在生物信息学中也有所应用。
# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
"""
Algo: Match DP
D.S.:

Solution:
f[i][i] = A first i char and B first j char max matches

Time: O(mn)
Space: O(mn)

Corner cases:
"""

class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        if not A or not B:
            return 0
        m, n = len(A), len(B)
        f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])
        return f[m][n]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
