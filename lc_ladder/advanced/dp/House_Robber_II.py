#! /usr/local/bin/python3

# https://www.lintcode.com/problem/house-robber-ii/description
# Example
# After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# nums = [3,6,4], return 6
"""
Algo: DP, 环状dp 滚动数组
D.S.:

Solution:
Time: O(n) Space: O(1）

解决环状dp的方式
1. 分裂，[3, 6, 4] -> [6, 4] && [3, 6] 拆成2个非换装
2. 重复，
3. 取反

DP分析 （和之前的简单版本一样）
1. 状态
f[i]: 前i个房子中，偷到的最大值
2. 方程
f[i] = max(f[i - 1], f[i - 2] + A[i - 1])
前i个最大值 = 1）前i-1的最大值，2）前i-2（偷i-2）的最大值加上A[i-1] （注意是A[i-1]而不是A[i] 因为有padding)
3. 初始化
f[0] = 0 # 前0个，ie 0
f[1] = A[0] # 前1个， ie A[0]
4. 答案
f[n]

Corner cases:
"""

class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        # write your code here
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums, 0, len(nums) - 2),
                   self.helper(nums, 1, len(nums) - 1))

    def helper(self, nums, start, end):
        # start and end are inclusive
        if start == end:
            return nums[start]
        f = [0, 0]
        """
        IMPORTANT that init f with f[start % 2] and f[(start + 1) % 2]
        """
        f[start % 2] = nums[start]
        f[(start + 1) % 2] = max(nums[start], nums[start + 1])
        for i in range(start + 2, end + 1):
            f[i % 2] = max(f[(i - 1) % 2],
                           f[(i - 2) % 2] + nums[i])
        return f[end % 2]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
