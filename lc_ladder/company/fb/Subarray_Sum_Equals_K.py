#! /usr/local/bin/python3

# https://www.lintcode.com/problem/subarray-sum-equals-k/description
# Example
# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example
# Example1
#
# Input: nums = [1,1,1] and k = 2
# Output: 2
# Explanation:
# subarray [0,1] and [1,2]
# Example2
#
# Input: nums = [2,1,-1,1,2] and k = 3
# Output: 4
# Explanation:
# subarray [0,1], [1,4], [0,3] and [3,4]

"""
Algo:
D.S.:

Solution:
Space: O(n)
Time: O(n)

Corner cases:
"""

class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        if not nums:
            return 0
        presum = [0] * (len(nums) + 1)
        premap = {}
        # this is important, 0 is pre-set as 1
        premap[0] = 1
        res = 0
        for i in range(len(nums)):
            cursum = presum[i] + nums[i]
            presum[i + 1] = cursum

            if cursum - k in premap:
                res += (premap[cursum - k])

            if cursum not in premap:
                premap[cursum] = 1
            else:
                premap[cursum] += 1

        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
