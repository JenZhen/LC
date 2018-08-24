#! /usr/local/bin/python3

# https://www.lintcode.com/problem/unique-paths/description
# Example
# A robot is located at the top-left corner of a m x n grid.
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
#
# How many possible unique paths are there?
#
# Example
# Given m = 3 and n = 3, return 6.
# Given m = 4 and n = 5, return 35.
#
# Notice
# m and n will be at most 100.

"""
Algo: DP - 二维滚动数组
D.S.:

DP 分析
1. 状态
f[i]: 到位置i， 有几种方式
2. 方程
f[i] = f[i - 1] + f[i] #可以%2
f[i]为来自上一行，f[i-1]为来自左边

3. 初始化
第一行，第一列都是1 到每个位置都只有1个方法
4. 答案
f[col - 1]

Solution:
Time O(mn) Space O(m)

Corner cases:
"""

class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        if not m or not n:
            return 0

        f = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                f[j] = f[j - 1] + f[j]
        return f[n - 1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
