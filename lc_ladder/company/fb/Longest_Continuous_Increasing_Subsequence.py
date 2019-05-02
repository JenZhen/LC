#! /usr/local/bin/python3

# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# Example
# Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
# Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.
# Example 2:
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length is 1.
# Note: Length of the array will not exceed 10,000.
"""
Algo: 计数，细节，Corner cases
D.S.:

Solution:
很简单的题要注意细节

Corner cases:
"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] <= nums[j - 1]:
                i = j
            res = max(res, j - i + 1)
        return res
        
# Test Cases
if __name__ == "__main__":
    solution = Solution()
