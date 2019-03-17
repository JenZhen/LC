#! /usr/local/bin/python3

# https://www.lintcode.com/problem/backpack-iv/description
# Example
# 给出 n 个物品, 以及一个数组, nums[i]代表第i个物品的大小, 保证大小均为正数并且没有重复, 正整数 target 表示背包的大小, 找到能填满背包的方案数。
# 每一个物品可以使用无数次
#
# 样例
# 样例1
#
# 输入: nums = [2,3,6,7] 和 target = 7
# 输出: 2
# 解释:
# 方案有:
# [7]
# [2, 2, 3]
# 样例2
#
# 输入: nums = [2,3,4,5] 和 target = 7
# 输出: 2
# 解释:
# 方案有:
# [2, 5]
# [3, 4]

"""
Algo: DP, Backpac, rolling
D.S.:

Solution:
solution1: DFS, 遍历所有可能，会超时
solution2: DP 2D,
dp[i][j] 表示用前i种拼到体积j能有几种方法
初始：第一行全是0，拼到用前0个拼体积0中方法，除了用前0个元素df[0][0] = 1
     第一列全是1，拼到0有1种方法 -- 全不要
dp[i][j] = 拿第i个的方法 + 不拿第i个的方法
dp[i][j] = dp[i - 1][j] + dp[i][j - nums[i - 1]]
note that i 的取值范围用于numsindex 不要越界， 如果可以重复使用，拿第i个的方法来自于dp[i][j - nums[i - 1]]
(区别不可以重复拿，拿第i个的方法来自于dp[i - 1][j - nums[i - 1]])
结果 dp[n][target]
Time: O(n * target) Space O(n * target）
solution3: DP 1D ROLLING
Time: O(n * target) Space O(target）

Corner cases:
"""

class Solution1:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        # write your code here
        if not nums:
            return []

        res = []
        path = []
        idx = 0
        nums = sorted(list(set(nums)))
        print(nums)
        self.dfs(nums, target, path, res, idx)
        return len(res)

    def dfs(self, nums, target, path, res, idx):
        if target == 0:
            res.append(path[:])
            return
        for i in range(idx, len(nums)):
            if nums[i] <= target:
                path.append(nums[i])
                self.dfs(nums, target - nums[i], path, res, i)
                path.pop()


class Solution2:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        # write your code here
        if not nums or not target:
            return 0

        nums = list(set(nums))
        n = len(nums)
        print(nums)
        f = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            for j in range(target + 1):
                if j < nums[i - 1]:
                    f[i][j] = f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j] + f[i][j - nums[i - 1]]
        print(f)
        return f[n][target]

class Solution3:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        # write your code here
        if not nums or not target:
            return 0

        nums = list(set(nums))
        n = len(nums)
        print(nums)
        f = [0 for _ in range(target + 1)]
        f[0] = 1
        for num in nums:
            for j in range(num, target + 1):
                f[j] += f[j - num]
        return f[-1]

# Test Cases
if __name__ == "__main__":
    testcases = [
    {'nums': [2,3,6,7],
     'target': 7},
    ]
    solution1 = Solution1()
    solution2 = Solution2()
    for t in testcases:
        nums = t['nums']
        target = t['target']
        res2 = solution2.backPackIV(nums, target)
        print(res2)
