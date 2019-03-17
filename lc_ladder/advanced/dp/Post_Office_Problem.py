#! /usr/local/bin/python3

# https://www.lintcode.com/problem/post-office-problem/description
# Example
# 在一条线上有 n 个房子，现在给出它们的位置，选择 k 个位置建立邮局使得每个房子到最近邮局距离的总和最小
#
# 样例
# [1,2,3,4,5] k = 2
# 答案为 3
#
# 挑战
# O(n^2)
"""
Algo: DP
D.S.:

Solution:
DP
需要辅助数据 dist
1. 状态
2. 方程
3. 初始化
4. 答案

Time: O(n^2 * k)

Corner cases:
"""

class Solution:
    """
    @param A: an integer array
    @param k: An integer
    @return: an integer
    """
    def postOffice(self, A, k):
        # write your code here
        if not A or not k:
            return 0
        if k >= len(A):
            return 0
        A.sort()

        import sys
        n = len(A)
        dist = self.initDist(A)
        # print(dist)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        # init first col with first row of dist
        for i in range(n + 1):
            dp[i][1] = dist[1][i]

        for j in range(2, k + 1): # [2, k]
            # j: col mean put j post offices
            for i in range(j, n + 1): # [j, n]
                # i iterate at least 2 house for 2 postoffice (house >= post offices)
                dp[i][j] = sys.maxsize
                for l in range(i): # [0, i) here not considering i since dist[l + 1][i] cannot be outofboundry
                    # enumerate possible positions to split
                    if (dp[i][j] == sys.maxsize or dp[i][j] > dp[l][j - 1] + dist[l + 1][i]):
                        dp[i][j] = dp[l][j - 1] + dist[l + 1][i]
        return dp[n][k]


    def initDist(self, A):
        # diag all 0
        n = len(A)
        dist = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):

                mid = (i + j) // 2
                # mid = (A[i - 1] + A[j - 1]) // 2
                for l in range(i, j + 1):
                    dist[i][j] += abs(A[l - 1] - A[mid - 1])
                    # dist[i][j] += abs(A[l - 1] - mid)
        """
        如果 mid 的定义如下：mid = (A[i - 1] + A[j - 1]) // 2
        结果错误，需要和面试官讨论
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                mid = (A[i - 1] + A[j - 1]) // 2
                for l in range(i, j + 1):
                    dist[i][j] += abs(A[l - 1] - mid)
        “”“
        return dist

# Test Cases
if __name__ == "__main__":
    solution = Solution()
