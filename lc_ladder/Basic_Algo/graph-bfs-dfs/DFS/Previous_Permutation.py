#! /usr/local/bin/python3

# https://www.lintcode.com/problem/previous-permutation/description
# Example
# Given a list of integers, which denote a permutation.
# Find the previous permutation in ascending order.
# Example
# For [1,3,2,3], the previous permutation is [1,2,3,3]
# For [1,2,3,4], the previous permutation is [4,3,2,1]

"""
Algo:
D.S.:

Solution:
The opposite solution of Next_Permutaion:
1. from rightmost, find the place i, where nums[i] < nums[i - 1]
2. reverse nums [i, len(nums) - 1]
3. from i to right, find the first j where nums[j] < nums[i - 1]
Corner cases:
"""

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        # write your code here
        if nums is None or len(nums) <= 0:
            return nums

        def swapElement(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        def reverseList(nums, i, j):
            while i < j:
                swapElement(nums, i, j)
                i += 1
                j -= 1

        i = len(nums) - 1
        while i > 0 and nums[i] >= nums[i - 1]:
            i -= 1
        reverseList(nums, i, len(nums) - 1)
        if i == 0:
            return nums
        j = i
        while j < len(nums) and nums[j] >= nums[i - 1]:
            j += 1
        swapElement(nums, i - 1, j)
        return nums

# Test Cases
if __name__ == "__main__":
    solution = Solution()
