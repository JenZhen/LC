#! /usr/local/bin/python3

# https://www.lintcode.com/problem/backpack-v/description
# Example
# 给出 n 个物品, 以及一个数组, nums[i] 代表第i个物品的大小, 保证大小均为正数, 正整数 target 表示背包的大小, 找到能填满背包的方案数。
# 每一个物品只能使用一次
#
# 样例
# 给出候选物品集合 [1,2,3,3,7] 以及 target 7
#
# 结果的集合为:
# [7]
# [1,3,3]
# 返回 2
"""
Algo: Backpack DP, Rolling
D.S.:

Solution:

solution1: 超时(not sure why)
solution2: AC
解法同backpack_IV, 因为一个元素只能用一次，dp[i][j] = 拿第i个元素 + 不拿第i个元素，其中拿的话要从i - 1行去取值，因为只能那一次
转化为1D空间，要主要因为是从dp矩阵的左上方取值，要么改为2D，要么，要从1D的最后计算
Time: O(n * target)
Space: O(target)

Corner cases:
"""

class Solution1:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        if not nums or not target:
            return 0

        n = len(nums)
        f = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            for j in range(target + 1):
                if j < nums[i - 1]:
                    f[i][j] = f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j] + f[i - 1][j - nums[i - 1]]
        return f[n][target]


class Solution2:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        if not nums or not target:
            return 0

        n = len(nums)
        f = [0 for _ in range(target + 1)]
        f[0] = 1
        for num in nums:
            for j in range(target, num - 1, -1):
                f[j] += f[j - num]
        return f[-1]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
