#! /usr/local/bin/python3

# https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-with-transaction-fee/description
# Example
# 现在给出一个数组，包含一系列价格，其中第i个元素是一支股票在第i天的价格；一个非负数fee代表了手续费。
#
# 你可以根据需要任意地进行交易，但是每次交易都必须付手续费。每次购买不能超过1股（必须在再次购买的之前卖出股票）。
#
# 返回可以获得的最大利润。
#
# 样例
# 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 最大利润的获得方式为：
# 买入 prices[0] = 1
# 卖出 prices[3] = 8
# 买入 prices[4] = 4
# 卖出 prices[5] = 9
# 总利润为 ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
#
# 注意事项
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.

"""
Algo: DP -- rolling
D.S.:

Solution:
Time: O(n), Space: O(1)

考虑每一天同时维护两种状态：拥有股票(own)状态和已经售出股票(sell)状态。用own和sell分别保留这两种状态到目前为止所拥有的最大利润。
对于sell，用前一天own状态转移，比较卖出持有股是否能得到更多的利润，即sell = max(sell , own + price - fee)，
而对于own , 我们考虑是否买新的股票更能赚钱(换言之，更优惠），own=max( own, sell-price)
初始化我们要把sell设为0表示最初是sell状态且没有profit，把own设为负无穷因为最初不存在该状态，我们不希望从这个状态进行转移
因为我们保存的都是最优状态，所以在买卖股票时候取max能保证最优性不变
最后直接返回sell即可

Corner cases:
"""

class Solution:
    """
    @param prices: a list of integers
    @param fee: a integer
    @return: return a integer
    """
    def maxProfit(self, prices, fee):
        # write your code here
        if not prices:
            return 0

        sell = 0
        buy = -prices[0]
        for i in range(1, len(prices)):
            sell = max(sell, prices[i] + buy - fee)
            print("sell" + str(sell))
            buy = max(buy, sell - prices[i])
            print("buy" + str(buy))
        return sell


# Test Cases
if __name__ == "__main__":
    solution = Solution()
