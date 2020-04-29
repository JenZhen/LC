#! /usr/local/bin/python3

# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays
# Example
# In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
#
# Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
#
# Return the result as a list of indices representing the starting position of each interval
# (0-indexed). If there are multiple answers, return the lexicographically smallest one.
#
# Example:
#
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
#
# Note:
#
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).
"""
Algo: DP, pre_sum
D.S.:

Solution:
1. 构建presum 数组，
优化为 presum[i] 是以i结尾 长度为k的subarray和
2. 固定中间一段subarray， 左边 右边分别能有多大的subarray
- 构建左， 会有一段buffer， list of （start_idx, sum) 更好的记录
- 构建右 同理
3. 遍历一遍找到最大的和，记录 3段 区间的起点

Time: O(n) * 4
Space: O(n)

Corner cases:
"""

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) < k * 3:
            return []

        # prepare presum array
        presum = [0] * len(nums)
        presum[0] = nums[0]
        for i in range(1, len(nums)):
            presum[i] = presum[i - 1] + nums[i]
            if i >= k:
                presum[i] = presum[i] - nums[i - k]
        print(presum)

        # prepare left (start_idx, sum)
        left = [(-1, 0)] * len(nums)
        for i in range(2 * k - 1, len(nums)):
            prev_sum = presum[i - k]
            prev_start_idx = i - 2 * k  + 1
            if prev_sum > left[i - 1][1]:
                left[i] = (prev_start_idx, prev_sum)
            else:
                left[i] = left[i - 1]
        print(left)
        # prepare right (start_idx, sum)
        right = [(-1, 0)] * len(nums)
        for i in range(len(nums) - 1 - k, -1, -1):
            prev_sum = presum[i + k]
            prev_start_idx = i + 1 # (i + k - (k - 1))
            if prev_sum >= right[i + 1][1]:
                right[i] = (prev_start_idx, prev_sum)
            else:
                right[i] = right[i + 1]
        print(right)

        max_sum = 0
        res = [0, 0, 0]
        for i in range(len(nums)):
            if left[i][0] == -1 or right[i][0] == -1:
                continue
            cur_sum = presum[i] + left[i][1] + right[i][1]
            print(cur_sum)
            if cur_sum > max_sum:
                max_sum = cur_sum
                res = [left[i][0], i - k + 1, right[i][0]]
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
