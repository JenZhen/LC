#! /usr/local/bin/python3

# https://leetcode.com/problems/stone-game/
# Example
# LT;DR:
# A, B两人轮流取石碓
# 每人每次可以从最左或最右拿一堆
# 最后总和数最大的人赢
# 求 先手 能不能赢

# Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row,
# and each pile has a positive integer number of stones piles[i].
#
# The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.
# Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.
# This continues until there are no more piles left, at which point the person with the most stones wins.
#
# Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.
#
# Example 1:
#
# Input: [5,3,4,5]
# Output: true
# Explanation:
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
#
# Note:
#
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles) is odd.
"""
Algo: DP
D.S.:

Solution:
相对数目：
A 拿5个，B拿 4个
A相对于B 赢 5 - 4 = 1 个
B相对于A 赢 4 - 5 = -1 个

推演：
如果只有1堆：[4] A 全拿 赢 4个
如果有2堆:  [4, 5] A 拿较多的那个 赢1个

最佳决策：
score(piles, l, r) = max(
    piles[l] - score(piles, l + 1, r),   # A 拿最左端，B 从剩下的 ie 区间[l + 1, r] 选最优解
    piles[r] - score(piles, l, r - 1),   # A 拿最右端，B 从剩下的 ie 区间[l , r + 1] 选最优解
)

Solution1:
DFS
Time: O(2 ^ n)
Space: O(n) n: 层深
递归深度N， 每层分出2支， 共2 ^ N
很多重复子问题， A 面对区间[l, r] 和 B面对区间[l, r] 是一样的决择， 所以需要MEMO

Solution2:
DP -- 记忆化 重复子问题
改进， 用memo 记住子区间的大小
if memo[l][r] 求结过，直接返回memo[l][r]
if memo[l][r] 没结果，求解 （公式如上），记住，直接返回memo[l][r]

Time: O(n ^ 2)
Space: O(n ^ 2)

Corner cases:
"""


class Solution1(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return self.dfs(piles, 0, len(piles) - 1)

    def dfs(self, piles, l, r):
        if l == r:
            return piles[l]
        return max(piles[l] - self.dfs(piles, l + 1, r), piles[r] - self.dfs(piles, l, r - 1))


class Solution2:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        self.memo = [[None for _ in range(n)] for _ in range(n)]
        return self.dfs(piles, 0, n - 1)

    def dfs(self, piles, l, r):
        if l == r:
            self.memo[l][r] = piles[l]
            return piles[l]
        if self.memo[l][r] == None:
            self.memo[l][r] = max(piles[l] - self.dfs(piles, l + 1, r), piles[r] - self.dfs(piles, l, r - 1))
        return self.memo[l][r]
# Test Cases
if __name__ == "__main__":
    solution = Solution()
