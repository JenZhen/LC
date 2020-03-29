#! /usr/local/bin/python3
# https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-with-cooldown/description
# Example
# 假设你有一个数组，第 i 个元素表示给出股票第 i 天的价格。
#
# 设计一个算法来得到最大的利润。你可以通过以下限制完成任意数量的交易（即买入并多次卖出一股股票）：
#
# 你不能同时进行多笔交易（即，必须在再次购买之前卖出股票）。
# 在你出售股票后，无法在第二天购买股票。 （即冷却1天）
# 样例
# 样例1
#
# 输入： [1, 2, 3, 0, 2]
# 输出： 3
# 解释：
# 交易详情： [buy, sell, cooldown, buy, sell]
# 样例2
#
# 输入： [3,2,6,5,0,3]
# 输出： 7

"""
Algo: DP of 2 states
D.S.:

Solution:
设sell[i] 卖出操作的最大利润。它需要考虑的是，第i天是否卖出。（手上有stock在第i天所能获得的最大利润）

buy[i] 买进操作的最大利润。它需要考虑的是，第i天是否买进。（手上没有stock在第i天所能获得的最大利润）

所以，显然有状态转移方程

buy[i] = max(buy[i-1] , sell[i-2] – prices[i])  // 休息一天在买入，所以是sell[i-2]在状态转移
sell[i] = max(sell[i-1], buy[i-1] + prices[i])
最后显然有sell[n-1] > buy[n-1] 所以我们返回sell[n-1]
Time: O(n)
Space: O(n) rolling space: O(1)

prices [1,  2,  3,  0, 2]
buy    [-1, -1, -1, 1, 1]
sell   [0,  1,   2, 2, 3]


Corner cases:
"""

class Solution:
    """
    @param prices: a list of integers
    @return: return a integer
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        buy = [0] * n
        sell = [0] * n

        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[0] = 0
        sell[1] = max(sell[0], prices[1] - prices[0])

        for i in range(2, n):
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
        print(buy)
        print(sell)
        return sell[n - 1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
