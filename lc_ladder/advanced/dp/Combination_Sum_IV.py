#! /usr/local/bin/python3

# https://www.lintcode.com/problem/combination-sum-iv/description
# Example
# 给出一个都是正整数的数组 nums，其中没有重复的数。从中找出所有的和为 target 的组合个数。
#
# 样例
# 样例1
#
# 输入: nums = [1, 2, 4] 和 target = 4
# 输出: 6
# 解释:
# 可能的所有组合有：
# [1, 1, 1, 1]
# [1, 1, 2]
# [1, 2, 1]
# [2, 1, 1]
# [2, 2]
# [4]
# 样例2
#
# 输入: nums = [1, 2] 和 target = 4
# 输出: 5
# 解释:
# 可能的所有组合有：
# [1, 1, 1, 1]
# [1, 1, 2]
# [1, 2, 1]
# [2, 1, 1]
# [2, 2]
# 注意事项
# 一个数可以在组合中出现多次。
# 数的顺序不同则会被认为是不同的组合。

"""
Algo: DP
D.S.:

Solution:

Corner cases:
"""

class Solution2:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackVI(self, nums, target):
        # write your code here
        if not nums or not target:
            return 0

        n = len(nums)
        f = [0] * (target + 1)
        f[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                print("num: " + str(num))
                if i >= num:
                    f[i] += f[i - num]
        return f[-1]

# Test Cases
if __name__ == "__main__":
    testcases = [
    {
        "nums": [1,2,4],
        "target": 4
    },
    ]
    solution2 = Solution2()
    for t in testcases:
        nums = t["nums"]
        target = t["target"]
        print(solution2.backPackVI(nums, target))
