#! /usr/local/bin/python3

# https://www.lintcode.com/problem/maximum-average-subarray-i/description
# Example

"""
Algo: Similar to Maximum_Average_Subarray II but not binary search required
D.S.: Sliding Window

Solution:
Time O(n)
Corner cases:
"""

class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """
    def findMaxAverage(self, nums, k):
        # Write your code here
        if not nums or not k:
            return 0
        ttl = sum(nums[:k])
        res = ttl
        for i in range(k, len(nums)):
            ttl += (nums[i] - nums[i - k])
            res = max(res, ttl)
        return res / k

# Test Cases
if __name__ == "__main__":
    s = Solution()
