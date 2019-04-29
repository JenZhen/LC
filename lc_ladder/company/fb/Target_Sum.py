#! /usr/local/bin/python3

# https://www.lintcode.com/problem/target-sum/
# Example
# 给定一个非负整数的列表a1,a2,...an，再给定一个目标S。现在用+和-两种运算，对于每一个整数，选择一个作为它前面的符号。
#
# 找出有多少种方法，使得这些整数的和正好等于S。
#
# 样例
# 例1:
#
# 输入: nums为 [1, 1, 1, 1, 1], S 为 3.
# 输出: 5
# 解释:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 有5种方法让和为3.
# 例2:
#
# 输入: nums 为 [], S 为 3.
# 输出: 0
# 解释:
# 没有方法能让和为3
# 注意事项
# 给定数组的长度是正整数而且不会超过20。
# 所有元素的和不会超过1000。
# 输出结果一定在32位整数范围内。

"""
Algo: DP, DFS, 找可行解的个数
D.S.: array

Solution:
这个题非常好
https://www.youtube.com/watch?v=r6Wz4W1TbuI

DP:
Time: O(n * 2sum) -- n is len of nums, sum is sum of nums
Space： O(n * sum) -- in this solution is n + 1 rows, each row is a dictionary has 2sum + 1 key value pairs

解法非常好，可以参考上面的视频地址
f[i]][j] -- 前i个元素组合成j 值有几种方法 where j 取值范围 -sum -> sum 共 2 * sum + 1 个
f[i][j] = f[i - 1][j - nums[i - 1]] + f[i - 1][j + nums[i - 1]]
where nums[i - 1] 是前i map到数组下标
j - nums[i - 1] 说明 nums[i - 1] 前取 +
j + nums[i - 1] 说明 nums[i - 1] 前取 -

可以滚动数组，只保存2行

DFS:
暴力解法
Time: O(2 ^ n)
Space： O(n)

Corner cases:
"""

class Solution_DP:
    """
    @param nums: the given array
    @param s: the given target
    @return: the number of ways to assign symbols to make sum of integers equal to target S
    """
    def findTargetSumWays(self, nums, s):
        # Write your code here
        if not nums:
            return 0

        n = len(nums)
        sm = sum(nums)
        if not (-sm <= s <= sm):
            return 0

        # sum range from -sum to sum total 2sum + 1
        # init f row: len(nums) + 1, col is map , key sum value, val cont
        f = [{} for _ in range(n + 1)]
        # init value first row only key = 0 cnt 1
        # first col only last row has cnt 1
        for j in range(-sm, sm + 1):
            if j == 0:
                f[0][j] = 1
            else:
                f[0][j] = 0
        for i in range(1, n + 1):
            if i == n:
                f[i][-sm] = 1
            else:
                f[i][-sm] = 0
        # dp process
        for i in range(1, n + 1):
            for j in range(-sm, sm + 1):
                f[i][j] = 0
                if (j - nums[i - 1]) in f[i - 1]:
                    f[i][j] += f[i - 1][j - nums[i - 1]]
                if (j + nums[i - 1]) in f[i - 1]:
                    f[i][j] += f[i - 1][j + nums[i - 1]]

        return f[n][s]


class Solution_DFS:
    """
    @param nums: the given array
    @param s: the given target
    @return: the number of ways to assign symbols to make sum of integers equal to target S
    """
    def findTargetSumWays(self, nums, s):
        # Write your code here
        self.cnt = 0
        self.dfs(0, nums, s)
        return self.cnt

    def dfs(self, idx, nums, target):
        if idx == len(nums):
            if target == 0:
                self.cnt += 1
            return
        self.dfs(idx + 1, nums, target - nums[idx])
        self.dfs(idx + 1, nums, target + nums[idx])

# Test Cases
if __name__ == "__main__":
    solution = Solution()
