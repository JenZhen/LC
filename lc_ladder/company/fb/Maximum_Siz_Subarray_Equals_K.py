#! /usr/local/bin/python3

# https://www.lintcode.com/problem/maximum-size-subarray-sum-equals-k/description
# Example
# 给一个数组nums和目标值k，找到数组中最长的子数组，使其中的元素和为k。如果没有，则返回0。
#
# 样例
# 样例1
#
# 输入: nums = [1, -1, 5, -2, 3], k = 3
# 输出: 4
# 解释:
# 子数组[1, -1, 5, -2]的和为3，且长度最大
# 样例2
#
# 输入: nums = [-2, -1, 2, 1], k = 1
# 输出: 2
# 解释:
# 子数组[-1, 2]的和为1，且长度最大
# 挑战
# 能否用O(n)的时间复杂度完成？
#
# 注意事项
# 数组之和保证在32位有符号整型数的范围内

"""
Algo: presum array + hash to quick find subarray sum
D.S.:

Solution:
Time: O(n)
Space: O(n)

presun[j] - presum[i] = sum[i + 1 : j]

presum array 0: -1 idx
careful about index between nums and presums

Corner cases:
"""

class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        if not nums:
            return 0
        res = 0
        presum = [0] * (len(nums) + 1)
        preMap = {}
        preMap[0] = -1
        for i in range(len(nums)):
            presum[i + 1] = presum[i] + nums[i]
            if presum[i + 1] not in preMap:
                preMap[presum[i + 1]] = i
            if presum[i + 1] - k in preMap:
                res = max(res, i - preMap[presum[i + 1] - k])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
