#! /usr/local/bin/python3

# https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iii/description
# Example
# 假设你有一个数组，它的第i个元素是一支给定的股票在第i天的价格。设计一个算法来找到最大的利润。你最多可以完成两笔交易。
#
# 样例
# 给出一个样例数组 [4,4,6,1,1,4,2,5], 返回 6
#
# 注意事项
# 你不可以同时参与多笔交易(你必须在再次购买前出售掉之前的股票)
"""
Algo: DP
D.S.:

Solution:
Solution1: best
Time. O(n), space: O(n)
解法 lint: 最多只有2次，所以在array中遍历分割点k 左到分割点，右到分割点。所以要做两遍DP

Solution2: exceed time limit
Time: O(n ^ 2) Space: O(n ^ 2)

Corner cases:
"""
class Solution_1:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)

        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]

        # from left to right
        minp = prices[0]
        for i in range(1, n):
            minp = min(minp, prices[i])
            left[i] = max(left[i - 1], prices[i] - minp)
        print(left)
        maxp = prices[-1]
        for i in range(n - 2, -1 ,-1):
            maxp = max(maxp, prices[i])
            right[i] = max(right[i + 1], maxp - prices[i])
        print(right)
        res = 0
        for k in range(n):
            res = max(res, left[k] + right[k])
        return res

class Solution_2:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # init dp
        for i in range(n):
            minp, maxp = prices[i], prices[i]
            prof = 0
            for j in range(i + 1, n):
                if prices[j] < minp:
                    minp = prices[j]
                if prices[j] >= maxp:
                    maxp = prices[j]
                    prof = max(prof, maxp - minp)
                dp[i][j] = prof
        print(dp)
        maxprof = 0
        for k in range(0, n):
            if k < n - 1:
                maxprof = max(maxprof, dp[0][k] + dp[k + 1][n - 1], dp[0][k] + dp[k][n - 1])
            else:
                maxprof = max(maxprof, dp[0][k] + dp[k][n - 1])
        return maxprof
# Test Cases
if __name__ == "__main__":
    solution = Solution()
