#! /usr/local/bin/python3

# https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iv/
# 假设你有一个数组，它的第i个元素是一支给定的股票在第i天的价格。
#
# 设计一个算法来找到最大的利润。你最多可以完成 k 笔交易。
#
# 样例
# 给定价格 = [4,4,6,1,1,4,2,5], 且 k = 2, 返回 6.
#
# 挑战
# O(nk) 时间序列。
#
# 注意事项
# 你不可以同时参与多笔交易(你必须在再次购买前出售掉之前的股票)

"""
Algo: DP, Rolling-DP
D.S.:

Solution:

dp,设dp[i][j]为第J天进行第i次交易能获取的最大值。

当k >=n/2时候，相当于第122题。Best Time to Buy and Sell Stock II
Original thought:
dp[i][j] = max {1. no transaction at time j: dp[i][j - 1],
                2. enumerate breaking point k [0, j) such as max prices[j] - prices[k] + dp[i - 1][k]
               }
Improvement:
dp[i][j]= max(dp[i][j-1],prices[j] + maxpre)  我们能获取的最大利润，当我们在第j天进行抛售时。由于maxpre已经算了买进时的价格，所以直接加上即可。
maxpre 可以理解为在j时间之前买入获得的最大利润
maxpre = max(maxpre,dp[i-1][j-1] – prices[j])  可以理解为已获得的最大利润，即如果买进第j天的，那么用之前一轮的买卖，前一天的的利润即（dp[i-1][j-1]）减去prices[j]
在时间j时maxpre 可以是1. 没有买入 也就是之前的maxpre， 2. 有买入，也就是dp[i - 1][j - 1] 在j-1时候交易i-1次的最大收入除去在时间j的买入付出，aka dp[i - 1][j - 1] - prices[j]

solution1:
Time: O(K * n * n) -- enumerate takes O(n) Too slow cannot AC
Space: O(K * n)
solution2:
Time; O(K * n) -- skip enumerate instead keep track of maxpre, (see definition above)
Space: O(K * n)
solution3:
Time: O(K * n) Space: O(n) -- rolling matrix only 2 rows

Corner cases:
"""


class Solution_1:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        # write your code here
        if not prices or len(prices) <= 1:
            return 0
        n = len(prices)
        if K >= n // 2:
            # transaction unlimited times, K is too large
            res = 0
            for i in range(1, n):
                res += (prices[i] - prices[i - 1]) if prices[i] - prices[i - 1] > 0 else 0
            return res

        dp = [[0 for _ in range(n)] for _ in range(K + 1)]
        # init first row and first col as 0
        for i in range(1, K + 1):
            for j in range(1, n):
                prof = 0
                for k in range(j):
                    prof = max(prof, prices[j] - prices[k] + dp[i - 1][k])
                prof = max(prof, dp[i][j - 1])
                dp[i][j] = prof
        print(dp)
        return dp[K][n - 1]


class Solution_2:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        # write your code here
        if not prices or len(prices) <= 1:
            return 0
        n = len(prices)
        if K >= n // 2:
            # transaction unlimited times, K is too large
            res = 0
            for i in range(1, n):
                res += (prices[i] - prices[i - 1]) if prices[i] - prices[i - 1] > 0 else 0
            return res

        dp = [[0 for _ in range(n)] for _ in range(K + 1)]
        # init first row and first col as 0
        for i in range(1, K + 1):
            maxpre = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + maxpre)
                maxpre = max(maxpre, dp[i - 1][j] - prices[j])
        print(dp)
        return dp[K][n - 1]


class Solution_3:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        # write your code here
        if not prices or len(prices) <= 1:
            return 0
        n = len(prices)
        if K >= n // 2:
            # transaction unlimited times, K is too large
            res = 0
            for i in range(1, n):
                res += (prices[i] - prices[i - 1]) if prices[i] - prices[i - 1] > 0 else 0
            return res

        dp = [[0 for _ in range(n)] for _ in range(2)]
        # init first row and first col as 0
        for i in range(1, K + 1):
            maxpre = -prices[0]
            for j in range(1, n):
                dp[i % 2][j] = max(dp[i % 2][j - 1], prices[j] + maxpre)
                maxpre = max(maxpre, dp[(i - 1) % 2][j - 1] - prices[j])
        print(dp)
        return dp[K % 2][n - 1]
# Test Cases
if __name__ == "__main__":
    solution = Solution()
