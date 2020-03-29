#! /usr/local/bin/python3

# https://www.lintcode.com/problem/next-permutation-ii
# Example
# Same with nextPermutation

"""
Algo:
D.S.:

Solution:
Time: O(N)
Space: in-place

Corner cases:
"""

class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        # write your code here
        if not nums:
            return nums

        if len(nums) <= 1:
            return nums

        def swapEle(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        def reverseList(nums, i, j):
            while i < j:
                swapEle(nums, i, j)
                i += 1
                j -= 1

        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        reverseList(nums, i, len(nums) - 1)
        if i == 0:
            return nums
        j = i
        while j < len(nums) and nums[j] <= nums[i - 1]:
            j += 1
        swapEle(nums, i - 1, j)
        return nums

# Test Cases
if __name__ == "__main__":
    solution = Solution()
