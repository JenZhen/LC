#!/usr/bin/python

# http://lintcode.com/en/problem/partition-array/
# Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:
# All elements < k are moved to the left
# All elements >= k are moved to the right
# Return the partitioning index, i.e the first index i nums[i] >= k.
#
# If nums = [3,2,2,1] and k=2, a valid answer is 1.

"""
Algo: two pointers, swap
D.S.:

Solution:
partition 模板

Note, swap may disrupt original order, keep original order see Move Zeroes!
Time: O(N)
Space: O(1)

Corner cases:
"""
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        p = -1
        for i in range(len(nums)):
            if nums[i] < k:
                p += 1
                nums[i], nums[p] = nums[p], nums[i]

        return p + 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
