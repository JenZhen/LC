#! /usr/local/bin/python3

# https://www.lintcode.com/problem/backpack-iii/description
# Example
# 给定n种具有大小 Ai 和价值 Vi 的物品(每个物品可以取用无限次)和一个大小为 m 的一个背包, 你可以放入背包里的最大价值是多少?
#
# 样例
# 给出四个物品, 大小为 [2, 3, 5, 7], 价值为 [1, 5, 2, 4], 和一个大小为 10 的背包. 最大的价值为 15.
#
# 注意事项
# 你不能将物品分成小块, 选择的项目的总大小应 小于或等于 m

"""
Algo: Backpack DP, rolling
D.S.:

Solution:
dp[i][j]: 前i个物体拼成体积j能达到的最大价值
Time: O(n * m)
Space: O(m)

Corner cases:
"""

class Solution1:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        # write your code here
        if not A or not V or len(A) < 1:
            return 0

        n = len(A)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        print(dp)
        # first row 0
        for i in range(1, n + 1):
            for j in range(0, m + 1):
                 # 如果不拿第i个，和只拿前i-1结果一样
                dp[i][j] = dp[i - 1][j]
                if A[i - 1] <= j:
                    #如果拿第i个,可以之前拿过第i个，结果从dp[i]这一行增加
                    dp[i][j] = max(dp[i][j], dp[i][j - A[i - 1]] + V[i - 1])
        print(dp)
        return dp[n][m]

# Test Cases
if __name__ == "__main__":
    testcases = [
        {
            "A": [1],
            "V": [1],
            "bagsize": 10
        },
        {
            "A": [2, 3, 5, 7],
            "V": [1, 5, 2, 4],
            "bagsize": 15
        }
    ]
    s1 = Solution1()
    for t in testcases:
        A = t["A"]
        V = t["V"]
        bagsize = t["bagsize"]
        print(s1.backPackIII(A, V, bagsize))
