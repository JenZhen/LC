#! /usr/local/bin/python3

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/submissions/
# Example
# Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; 
# and a non-negative integer fee representing a transaction fee.
#
# You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
# You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
#
# Return the maximum profit you can make.
#
# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

"""
Algo: DP
D.S.:

Solution:
Time: O(n)
Space: O(1)

注意先更新 SELL 再更新买
Corner cases:
"""

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices or len(prices) < 2:
            return 0
        sell = 0
        buy = -prices[0]
        for i in range(1, len(prices)):
            # sell first, then buy
            # at prices[i] must sell first then buy
            sell = max(sell, prices[i] + buy - fee)
            buy = max(buy, sell - prices[i])
        return sell

# Test Cases
if __name__ == "__main__":
    solution = Solution()
