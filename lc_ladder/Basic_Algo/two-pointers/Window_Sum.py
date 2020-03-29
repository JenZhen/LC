#!/usr/bin/python

# http://lintcode.com/en/problem/window-sum/
# Example
# Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array, find the sum of the element inside the window at each moving.
# For array [1,2,7,8,5], moving window size k = 3.
# 1 + 2 + 7 = 10
# 2 + 7 + 8 = 17
# 7 + 8 + 5 = 20
# return [10,17,20]

"""
Algo: Two pointers
D.S.:

Solution:

Corner cases:
- nums is emtpy, k <= 0 return []
- windwo size larger than array size, return all array elements sum
- k == 1 ie. l == r
"""

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if k <= 0 or not nums:
            return []
        res = []
        ttl = 0
        # init the first k range sum
        for i in range(min(k, len(nums))):
            ttl += nums[i]
        if k > len(nums):
            return [ttl]
        l, r = 0, k - 1
        # append the first k range sum to res
        res.append(ttl)
        while r + 1 < len(nums):
            ttl = ttl - nums[l] + nums[r + 1]
            res.append(ttl)
            l += 1
            r += 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
