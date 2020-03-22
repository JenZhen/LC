#! /usr/local/bin/python3

# https://www.lintcode.com/problem/next-permutation/description
# Find the next permutation in ascending order.
# May have duplicate numbers
# Example
# For [1,3,2,3], the next permutation is [1,3,3,2]
# For [4,3,2,1], the next permutation is [1,2,3,4]

"""
Algo: iteration (understand DFS)
D.S.:

Solution:

[1,3,2,3] -> [1,3,3,2]
[4,3,2,1] -> [1,2,3,4]
前面固定，从后往前找, 如果递减，（2，3，2，1）说明3，2，1已经不能再调整了，3前面有个2 说明下个permutation是把这个3的2调整到后面
找到这个3(idx = i)之后，reverseList [idx, len(nums) - 1],
从左到右[idx, len(nums) - 1]，找到一个大于nums[i - 1]的并swap

Time: O(N)

Corner cases:
"""

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
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
