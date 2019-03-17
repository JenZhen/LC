#! /usr/local/bin/python3

# https://www.lintcode.com/problem/k-sum/description?_from=ladder&&fromId=4
# Example
# 给定 n 个不同的正整数，整数 k（k <= n）以及一个目标数字 target。　
# 在这 n 个数里面找出 k 个数，使得这 k 个数的和等于目标数字，求问有多少种方案？
#
# 样例
# 给出 [1,2,3,4]，k=2， target=5，[1,4] 和 [2,3] 是 2 个符合要求的方案，返回 2。

"""
Algo: Rolling DP, high-dimensional
D.S.:

Solution: # TODO:
dp[i][j][s]
前 i 个数里挑出 j 个数，和为 s

Corner cases:
"""

class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # write your code here
        n = len(A)
        dp = [
            [[0] * (target + 1) for _ in range(k + 1)],
            [[0] * (target + 1) for _ in range(k + 1)],
        ]

        # dp[i][j][s]
        # 前 i 个数里挑出 j 个数，和为 s
        dp[0][0][0] = 1
        for i in range(1, n + 1):
            dp[i % 2][0][0] = 1
            for j in range(1, min(k + 1, i + 1)):
                for s in range(1, target + 1):
                    dp[i % 2][j][s] = dp[(i - 1) % 2][j][s]
                    if s >= A[i - 1]:
                        dp[i % 2][j][s] += dp[(i - 1) % 2][j - 1][s - A[i - 1]]

        return dp[n % 2][k][target]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
