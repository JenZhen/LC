#! /usr/local/bin/python3

# https://www.lintcode.com/problem/contiguous-array/description
# Example
# 给一个二进制数组，找到 0 和 1 数量相等的子数组的最大长度
#
# 样例
# 样例 1:
#
# 输入: [0,1]
# 输出: 2
# 解释: [0, 1] 是具有相等数量的 0 和 1 的最长子数组。
# 样例 2:
#
# 输入: [0,1,0]
# 输出: 2
# 解释: [0, 1] (或者 [1, 0]) 是具有相等数量 0 和 1 的最长子数组。
# 注意事项
# 给出的二进制数组的长度不会超过 50,000。

"""
Algo: presum array + hashmap to find subarray sum
D.S.:

Solution:
Time: O(n)
Space: O(n)

Corner cases:
"""
class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        # Write your code here
        if not nums or len(nums) < 2:
            return 0
        cnt0, cnt1 = 0, 0
        diffMap = {}
        diffMap[0] = -1
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt0 += 1
            else:
                cnt1 += 1a
            diff = cnt0 - cnt1
            if diff not in diffMap:
                diffMap[diff] = i
            else:
                res = max(res, i - diffMap[diff])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
