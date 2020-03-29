#! /usr/local/bin/python3

# https://www.lintcode.com/problem/backpack-ii/
# Example
# 给出n个物品的体积A[i]和其价值V[i]，将他们装入一个大小为m的背包，最多能装入的总价值有多大？
#
# 样例
# 对于物品体积[2, 3, 5, 7]和对应的价值[1, 5, 2, 4], 假设背包大小为10的话，最大能够装入的价值为9。
#
# 挑战
# O(n x m) memory is acceptable, can you do it in O(m) memory?
#
# 注意事项
# A[i], V[i], n, m均为整数。你不能将物品进行切分。你所挑选的物品总体积需要小于等于给定的m。

"""
Algo: Rolling DP
D.S.:

Solution:
Time: O(n*s)  Space: O(s) 滚动数组
where n is number of items, s is size of backpack

DP 分析
1. 状态
f[i][j]：表示i个物品中选一些物品组成体积为j的最大价值
2. 方程
f[i][j] = max(f[i - 1][j], f[i - 1][j - A[i - 1]] + value[i - 1])
倒着考虑有2种拿法：
f[i - 1][j] -- 就不用拿第i个了
f[i - 1][j - A[i - 1]] + value[i - 1] -- 拿了第i个物品正好有体积j, 再加上物品i-1的价值
    前提是j - A[i - 1] >= 0， 应为物品没有根据大小来排序

考虑滚动数组 Space O(size_of_backpack)

3. 初始化
f[0][0] = 0
4. 答案
f[n][s]

Corner cases:
"""

class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        if not m or not A or not V or len(A) < 2 or len(V) < 2:
            return 0
        n = len(A)
        dp = [[0 for _ in range(m + 1)] for _ in range(2)]
        # first row and col are 0s
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # not take i-th item
                dp[i % 2][j] = dp[(i - 1) % 2][j]
                if A[i - 1] <= j:
                    # if j is big enough for i-th item to be taken
                    dp[i % 2][j] = max(dp[i % 2][j], # not take i-th item
                                       dp[(i - 1) % 2][j - A[i - 1]] + V[i - 1] # take i-th item
                                       )
        return dp[n % 2][m]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
