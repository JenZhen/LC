#! /usr/local/bin/python3

# https://www.lintcode.com/problem/previous-permutation/description
# Example
# 给定一个整数数组来表示排列，找出其上一个排列。
#
# 样例
# 例1:
#
# 输入:[1]
# 输出:[1]
# 例2:
#
# 输入:[1,3,2,3]
# 输出:[1,2,3,3]
# 例3:
#
# 输入:[1,2,3,4]
# 输出:[4,3,2,1]
#
# 注意事项
# 排列中可能包含重复的整数
"""
Algo:
D.S.:

Solution:

Time: O(N)
Space: O(1)
Corner cases:
"""

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        # write your code here
        if not nums: return nums
        p = len(nums) - 1
        while p - 1 >= 0:
            if nums[p - 1] > nums[p]:
                self.reverse(nums, p, len(nums) - 1)
                for i in range(p, len(nums)):
                    if nums[i] < nums[p - 1]:
                        nums[i], nums[p - 1] = nums[p - 1], nums[i]
                        return nums
            p -= 1
        self.reverse(nums, 0, len(nums) - 1)
        print(nums)
        return nums

    def reverse(self, nums, lower, upper):
        l, r = lower, upper
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
# Test Cases
if __name__ == "__main__":
    solution = Solution()
