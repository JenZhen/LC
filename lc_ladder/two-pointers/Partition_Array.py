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
Solution1.
- cur idx is tracking cur examinig element
- rBoundry idx is cur available position for next >=k element
However, this process losses track of the first >=k idx, need to re-traverse to find.
Corner case, k > all elemnt in array, return len(nums)

Solution2.
- start idx is the left most >=k element, which is the return value of this function
- end idx is the right most <k element
swap start and end
This process use the start idx to cover the corner case for Solution1

Solution3.
Based on solution2, using more l < r condition.
But careful with corner cases
1. [1, 2] k = 2
    l, r
2. [0, 1] k = 2
    l, r

Note, swap may disrupt original order, keep original order see Move Zeroes!
Time: O(N)
Space: O(1)

Corner cases:
[3,2,2,1] k = 4, return 4
"""

# Self solution
class Solution1:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if len(nums) == 0 or k is None:
            return 0

        cur = 0
        rBoundry = len(nums) - 1
        while cur < rBoundry:
            if nums[cur] < k:
                cur += 1
            else:
                nums[cur], nums[rBoundry] = nums[rBoundry], nums[cur]
                rBoundry -= 1

        for i in range(len(nums)):
            if nums[i] >= k:
                return i
        return len(nums)

# Improved solution
class Solution2:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        start, end = 0, len(nums) - 1
        while start <= end:
            while start <= end and nums[start] < k:
                start += 1
            while start <= end and nums[end] >= k:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start

class Solution3:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if len(nums) == 0 or k is None:
            return 0

        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] < k:
                l += 1
            while l < r and nums[r] >= k:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        return l if nums[l] >= k else l + 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
