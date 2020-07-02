#! /usr/local/bin/python3

# https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock/description
# Example
# 假设有一个数组，它的第i个元素是一支给定的股票在第i天的价格。如果你最多只允许完成一次交易(例如,一次买卖股票),设计一个算法来找出最大利润。
#
# 样例
# 给出一个数组样例 [3,2,3,1,2], 返回 1
"""
Algo:
D.S.: Array

Solution:
find all upwards trends and update min and max price, update max profit
only price greater than current max price or less than current min price matters.
it doesn't matter if equal or between.

Time：O(n), Space: O(1)
arr       3  2  3  1  2
maxsell   0  -1 1  -1 1
   buy   -3  -2 -3 -1 -2
maxbuy   -3  -2 -2 -1 -1

Corner cases:
no element or one element

"""
class Solution_Suggested:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 1:
            return 0
        maxsell = 0
        maxbuy = -prices[0]

        for i in range(1, len(prices)):
            maxsell = max(maxsell, maxbuy + prices[i])
            maxbuy = max(-prices[i], maxbuy)
        return maxsell

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if not prices or len(prices) == 1:
            return 0

        maxp, minp = prices[0], prices[0]
        prof = 0
        for i in range(1, len(prices)):
            if prices[i] > maxp:
                maxp = prices[i]
                prof = max(maxp - minp, prof)
            if prices[i] < minp:
                minp, maxp = prices[i], prices[i]
        return prof

# Test Cases
if __name__ == "__main__":
    solution = Solution()
