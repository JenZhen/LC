#! /usr/local/bin/python3

# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/submissions/
# Example
# Given an array of integers arr and an integer target.
# You have to find two non-overlapping sub-arrays of arr each with sum equal target.
# There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.
#
# Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.
#
# Example 1:
# Input: arr = [3,2,2,4,3], target = 3
# Output: 2
# Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
#
# Example 2:
# Input: arr = [7,3,4,7], target = 7
# Output: 2
# Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]),
# but we will choose the first and third sub-arrays as the sum of their lengths is 2.
#
# Example 3:
# Input: arr = [4,3,2,6,2,3,4], target = 6
# Output: -1
# Explanation: We have only one sub-array of sum = 6.
#
# Example 4:
# Input: arr = [5,5,4,4,5], target = 3
# Output: -1
# Explanation: We cannot find a sub-array of sum = 3.
#
# Example 5:
# Input: arr = [3,1,1,1,5,1,2,1], target = 3
# Output: 3
# Explanation: Note that sub-arrays [1,2] and [2,1] cannot be an answer because they overlap.
#
# Constraints:
# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 1000
# 1 <= target <= 10^8
"""
Algo: presum
D.S.:

Solution:
2个presum 从左向右，从右向左，找 以 arr[i] 为左右端点 sub array 最小长度记录一下
Time: O(n)
Space: O(n)

Solution2:
Sliding Window
Time: O(n)
Space: O(n)

Corner cases:
"""

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        if not arr:
            return -1

        mp_left = {}
        mp_left[0] = [-1]
        len_left = [len(arr)] * len(arr)
        presum_left = 0
        for i in range(len(arr)):
            presum_left += arr[i]
            if presum_left - target in mp_left:
                for k in mp_left[presum_left - target]:
                    len_left[i] = min(len_left[i], i - k)
            if presum_left not in mp_left:
                mp_left[presum_left] = []
            mp_left[presum_left].append(i)

        mp_right = {}
        mp_right[0] = [len(arr)]
        len_right = [len(arr)] * len(arr)
        presum_right = 0
        for i in range(len(arr) - 1, -1, -1):
            presum_right += arr[i]
            if presum_right - target in mp_right:
                for k in mp_right[presum_right - target]:
                    len_right[i] = min(len_right[i], k - i)
            if presum_right not in mp_right:
                mp_right[presum_right] = []
            mp_right[presum_right].append(i)

        # print(len_left)
        # print(len_right)

        i, j = 0, len(arr) - 1
        res = len(arr) + 1
        while i < j:
            if len_left[i] == len(arr):
                i += 1
            elif len_right[j] == len(arr):
                j -= 1
            else:
                res = min(res, len_left[i] + len_right[j])
                if len_left[i] <= len_right[j]:
                    j -= 1
                else:
                    i += 1
        return -1 if res == len(arr) + 1 else res



class Solution2:
    """
    @param boxes: number of pens for each box
    @param target: the target number
    @return: the minimum boxes
    """
    def minimumBoxes(self, boxes, target):
        # write your code here
        n = len(boxes)
        dp = [n for _ in range(n)]
        right, left, sum = n - 1, n - 1, 0
        while left >= 0:
            sum += boxes[left]
            while sum > target:
                sum -= boxes[right]
                right -= 1
            while right > left and boxes[right] == 0:
                right -= 1
            if sum == target:
                dp[left] = right - left + 1
            if left + 1 < n:
                dp[left] = min(dp[left], dp[left + 1])
            left -= 1
        left, right, sum = 0, 0, 0
        ans = n + 1
        while right < n:
            sum += boxes[right]
            while sum > target:
                sum -= boxes[left]
                left += 1
            while left < right and boxes[left] == 0:
                left += 1
            if sum == target and right + 1 < n:
                print(left, right)
                ans = min(ans, right - left + 1 + dp[right + 1])
            right += 1
        if ans > n:
            return -1
        return ans

# Test Cases
if __name__ == "__main__":
    solution = Solution()
