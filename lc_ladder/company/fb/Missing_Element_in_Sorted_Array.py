#! /usr/local/bin/python3

# https://leetcode.com/problems/missing-element-in-sorted-array/submissions/
# Example
# Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.
#
# Example 1:
# Input: A = [4,7,9,10], K = 1
# Output: 5
# Explanation:
# The first missing number is 5.
#
# Example 2:
# Input: A = [4,7,9,10], K = 3
# Output: 8
# Explanation:
# The missing numbers are [5,6,8,...], hence the third missing number is 8.
#
# Example 3:
# Input: A = [1,2,4], K = 3
# Output: 6
# Explanation:
# The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
#
# Note:
# 1 <= A.length <= 50000
# 1 <= A[i] <= 1e7
# 1 <= K <= 1e8
"""
Algo: 计数题
D.S.:

Solution:

Time: O(n) -- length of nums
Space: O(1)
Corner cases:
"""

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if not nums or not k: return None
        if len(nums) == 1:
            return nums[0] + k
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1] - 1 # 中间缺几个数
            if diff >= k:
                return nums[i - 1] + k
            else:
                k -= diff
        if k > 0:
            return nums[-1] + k

# Test Cases
if __name__ == "__main__":
    solution = Solution()
