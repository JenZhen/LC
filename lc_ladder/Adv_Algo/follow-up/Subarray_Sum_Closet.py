#! /usr/local/bin/python3

# https://lintcode.com/problem/subarray-sum-closest/description
# Example
# Given an integer array, find a subarray with sum closest to zero. Return the indexes of the first number and last number.

# Example
# Given [-3, 1, 1, -3, 5], return [0, 2], [1, 3], [1, 1], [2, 2] or [0, 4].

# Challenge
# O(nlogn) time

"""
Algo: Presum
D.S.: Continuous subarray

Solution:
idx   -1,  0, 1,  2,  3,  4
nums      -3, 1,  1, -3,  5
presum 0, -3, -2, -1, -4, 1
sorted with idx (-4, 3), (-3, 0), (-2, 1), (-1, 2), (0, -1), (1, 4)

Since the presum is sorted, neighbors should be the closest distance. Iterate thru each neighbor to find the min dist.
The closest scenario is equal, meaning distance is 0.
When find min dist, there are 2 indice, order them. Since sum[i:j] = presum[j] - presum[i - 1], we need to add smaller idx by 1.

Follow up. To find all possible solutions.
Corner cases:
"""

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        res = []
        if not nums:
            return res
        presum = [(0, -1)]
        for i in range(len(nums)):
            presum.append((presum[-1][0] + nums[i], i))

        presum.sort()
        import sys
        dist = sys.maxsize
        for i in range(len(nums)):
            if presum[i + 1][0] - presum[i][0] < dist:
                dist = presum[i + 1][0] - presum[i][0]
                res = [presum[i + 1][1], presum[i][1]]
                res.sort()
                res[0] += 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
