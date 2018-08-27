#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo:
D.S.:

Solution:
Time: O(n*s) Space: O(s) 滚动数组
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

# Test Cases
if __name__ == "__main__":
    solution = Solution()
