#! /usr/local/bin/python3

# https://leetcode.com/problems/continuous-subarray-sum/
# Example
# Given a list of non-negative numbers and a target integer k, write a function to check if
# the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.
#
# Example 1:
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
#
# Example 2:
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
#
# Note:
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

"""
Algo: Presum 数组
D.S.:

Solution1:
presum 数组
遍历所有长度大于等于2的subarray
Time: O(n ^ 2)
Spce: O(n)

Solution2:
presum + map
如果 cursum % 6 = 2 而且之前有 sum 也mod 2 说明相减之后是6的倍数
注意要查前一个的IDX 和当前相比长度是否大于等于2

注意： 单独处理 K = 0的情况
    - 不能求MOD
    - 某个subarray和 等于0

Time: O(n)
Space: O(n) -- build map

Corner cases:
"""

class Solution1:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < 2:
            return False

        pre_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
        print(pre_sum)

        for i in range(len(pre_sum) - 2):
            for j in range(i + 2, len(pre_sum)):
                ttl = pre_sum[j] - pre_sum[i]
                if ttl == k or (k != 0 and ttl % k == 0):
                    print(ttl)
                    return True
        return False

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < 2:
            return False

        if k == 0:
            for i in range(1, len(nums)):
                if nums[i] == nums[i - 1] == 0:
                    return True
            return False

        mod_map = {0: -1} # key: mod, val: idx
        ttl = 0
        for i in range(len(nums)):
            ttl += nums[i]
            mod = ttl % k
            if mod in mod_map and mod_map[mod] < i - 1:
                return True
            if mod not in mod_map:
                mod_map[mod] = i
        return False
# Test Cases
if __name__ == "__main__":
    solution = Solution()
