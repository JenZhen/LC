#! /usr/local/bin/python3

# https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-ii/description
# Example
# 假设有一个数组，它的第i个元素是一个给定的股票在第i天的价格。设计一个算法来找到最大的利润。
# 你可以完成尽可能多的交易(多次买卖股票)。然而,你不能同时参与多个交易(你必须在再次购买前出售股票)。
#
# 样例
# 给出一个数组样例[2,1,2,0,1], 返回 2
"""
Algo:
D.S.:

Solution:
记录所有上升趋势的上升高度.
法一，根据每个趋势判断，持平，上升，或下降，只有上升才计入利润，每种情况都要跟新下一个趋势的起点
法二，找到每个连续上升的序列

Time：O(n), Space: O(1)

Corner cases:
"""

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) == 1:
            return 0

        prof = 0
        low = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > low:
                prof += (prices[i] - low)
            low = prices[i]
        return prof


# Test Cases
if __name__ == "__main__":
    solution = Solution()
