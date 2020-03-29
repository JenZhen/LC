#! /usr/local/bin/python3

# https://lintcode.com/problem/stone-game/description
# Example
# There is a stone game.At the beginning of the game the player picks n piles of stones in a line.

# The goal is to merge the stones in one pile observing the following rules:

# At each step of the game,the player can merge two adjacent piles to a new pile.
# The score is the number of stones in the new pile.
# You are to determine the minimum of the total score.

# Example
# For [4, 1, 1, 4], in the best solution, the total score is 18:

# 1. Merge second and third piles => [4, 2, 4], score +2
# 2. Merge the first two piles => [6, 4]，score +6
# 3. Merge the last two piles => [10], score +10
# Other two examples:
# [1, 1, 1, 1] return 8
# [4, 4, 5, 9] return 43

"""
Algo: 区间类DP
D.S.:

Solution:
Time: O(n^3) Space: O(n^2)
最大的区间
              3，4，3
         /               \
        /                 \
    3, 34                34, 3
      /  \              /   \
    3     4            3     4
最小的区间

大区间指[0, n - 1]
缩小的区间是[0, k][k + 1, n - 1], k 的位置在哪里需要枚举得到，各个枚举的结果中最小的是最优
...
直至初始化区间 f[i][i]

1. 状态
f[i][j]: 合并区间i,j 得到的最小cost
2. 方程
f[i][j] = min(
        # 枚举k 的位置 k [i, j)
        # 取左边子问题：f[i][k]
        # 取右边子问题：f[k + 1][j]
        f[i][k] + f[k + 1][j] + sum[i][j] # sum[i][j] 指从i到j
    )

3. 初始化
因为k 在[i, j) 所以初始化f[i][i] = 0 合并同一位置cost = 0
同事要初始化sum[i][j]
4. 答案
return f[0][n - 1]
Corner cases:
"""

class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        # write your code here
        if not A:
            return 0
        n = len(A)
        f = [[None for _ in range(n)] for _ in range(n)]
        sum = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    sum[i][j] = A[i]
                else:
                    sum[i][j] = sum[i][j - 1] + A[j]
        return self.search(0, n - 1, f, sum, A)

    def search(self, i, j, f, sum, A):
        import sys
        if f[i][j] is not None:
            return f[i][j]
        if i == j:
            f[i][j] = 0
        else:
            f[i][j] = sys.maxsize
            for k in range(i, j):
                f[i][j] = min(f[i][j], self.search(i, k, f, sum, A) + self.search(k + 1, j, f, sum, A) + sum[i][j])
        return f[i][j]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
