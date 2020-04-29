#! /usr/local/bin/python3

# https://leetcode.com/problems/next-permutation/
# Example
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 1,5,1 → 5,1,1
"""
Algo:
D.S.:

Solution:
从后往前找第一个顺序， 将后面的reverse
顺序数字和reverse后的第一个比他大的调换位置

如果没有顺序，则全部调换位置
Time: O(n) * 3
Time: O(1)

类似的
Prev permutation
Corner cases:
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return nums
        p = len(nums) - 1
        while p - 1 >= 0:
            if nums[p - 1] < nums[p]:
                # reverse
                self.reverse(nums, p, len(nums) - 1)
                print("reverse", nums)
                # swap
                for i in range(p, len(nums)):
                    if nums[i] > nums[p - 1]:
                        nums[i], nums[p - 1] = nums[p - 1], nums[i]
                        print("swap", nums)
                        return
            p -= 1
        self.reverse(nums, 0, len(nums) - 1)
        return

    def reverse(self, nums, i, j):
        l, r = i, j
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
