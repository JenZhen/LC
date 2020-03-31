#!/usr/bin/python

# https://leetcode.com/problems/subarray-sum-equals-k/
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


"""
Algo:
D.S.: Linked List/Array

Solution:
Time: O(n)
Space: O(n)

Corner cases:
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums or k is None:
            return 0
        cnt = 0
        presum = 0
        mp = {}
        mp[0] = 1
        for i in range(len(nums)):
            presum += nums[i]
            if presum - k in mp:
                cnt += mp[presum - k]
            if presum not in mp:
                mp[presum] = 1
            else:
                mp[presum] += 1
        return cnt

# Test Cases
if __name__ == "__main__":
	solution = Solution()
