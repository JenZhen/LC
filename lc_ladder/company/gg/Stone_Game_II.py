#! /usr/local/bin/python3

# https://leetcode.com/problems/stone-game-ii/
# LT;DR:
# A, B两人轮流取石碓
# 每人每次可以从 x 堆， 1 <= x <= 2M, M从1开始
# 目标 最后总和数最大
# 求 先手 最多能拿多少
#
# Example
# Alex and Lee continue their games with piles of stones.
# There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
# The objective of the game is to end with the most stones.
#
# Alex and Lee take turns, with Alex starting first.  Initially, M = 1.
# On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).
# The game continues until all the stones have been taken.
# Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.
#
# Example 1:
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, then Alex takes 2 piles again.
# Alex can get 2 + 4 + 4 = 10 piles in total. If Alex takes two piles at the beginning, then Lee can take all three piles left. In this case,
# Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger.
#
# Constraints:
#
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 10 ^ 4

"""
Algo: DP
D.S.:

Solution:
类似于stone game I
相对数目：
A 拿5个，B拿 4个
A相对于B 赢 5 - 4 = 1 个
B相对于A 赢 4 - 5 = -1 个

a + b = total --> sum(piles)
a - b = diff  --> A 最后赢的数目
a = (total + diff) // 2 --> 题目转化为 求diff

最佳决策：
相比于stone game I, 只有2种决策方式，最左或最右
这个题，要遍历k种方式，1 <= k <= 2*M (同时不能超过pile size)
memo[l][r] = max(
    memo[l][r], sum[l][k] - memo[k+1][r])
)
Time: O(n ^ 3) mn * k
Space: O(n ^ 2)
Corner cases:
"""

import sys
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # i, j means 从i 开始 给定M 最多能赢多少
        # i [0, n - 1], j [1, n] 最少拿1个，最多全拿 n个
        self.memo = [[None for _ in range(n)] for _ in range(n)]
        total = sum(piles)
        diff = self.dfs(0, 1, piles)
        # print(total, diff)
        # print(self.memo)
        return (total + diff) // 2

    def dfs(self, start_idx, M, piles):
        if start_idx >= len(piles):
            return 0
        # M 最多有n 个
        M = min(len(piles), M)

        if self.memo[start_idx][M] != None:
            return self.memo[start_idx][M]
        # 在当前start_idx， 给定M, 最远可以全部拿走的话，取得全部拿走的和
        if start_idx + 2 * M >= len(piles):
            self.memo[start_idx][M] = sum(piles[start_idx:])
            return self.memo[start_idx][M]

        # 遍历可以拿走的所有情况 k [1, 2M]
        best = -sys.maxsize
        cur = 0
        for k in range(1, 2 * M + 1):
            # from start_idx 拿k个，有多少分
            cur += piles[start_idx + k - 1
                    # 当前拿k个的分 - 剩下的给对方做决定拿多少分
            best = max(best, cur - self.dfs(start_idx + k, max(k, M), piles))
        self.memo[start_idx][M] = best
        return self.memo[start_idx][M]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
