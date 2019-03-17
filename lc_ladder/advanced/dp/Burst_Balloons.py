#! /usr/local/bin/python3

# https://www.lintcode.com/problem/burst-balloons/description
# 有n个气球，编号为0到n-1，每个气球都有一个分数，存在nums数组中。
# 每次吹气球i可以得到的分数为 nums[left] * nums[i] * nums[right]，
# left和right分别表示i气球相邻的两个气球。当i气球被吹爆后，其左右两气球即为相邻。要求吹爆所有气球，得到最多的分数。
#
# 样例
# 给出 [4, 1, 5, 10]
# 返回 270
#
# nums = [4, 1, 5, 10] burst 1, 得分 4 * 1 * 5 = 20
# nums = [4, 5, 10]    burst 5, 得分 4 * 5 * 10 = 200
# nums = [4, 10]       burst 4, 得分 1 * 4 * 10 = 40
# nums = [10]          burst 10, 得分 1 * 10 * 1 = 10
# 总共的分数为 20 + 200 + 40 + 10 = 270
"""
Algo: 区间动态规划
D.S.:

Solution:
# TODO:
使用算法强化班与动态规划专题班中讲的区间动态规划。
dp[i][j] 代表 burst i+1 ~ j-1 这段时间的所有气球之后，只剩下 i,j 的最大收益。

将原来的数组前面和后面增加两个1，最后结果就是 dp[0][n - 1]（burst 掉所有气球只剩两个1）
Time:
Space:

Corner cases:
"""

class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        # write your code here
        if not nums:
            return 0

        nums = [1, *nums, 1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] +  dp[k][j] + nums[i] * nums[k] * nums[j])

        return dp[0][n - 1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
