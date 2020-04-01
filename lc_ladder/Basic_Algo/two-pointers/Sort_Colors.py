#!/usr/bin/python

# https://leetcode.com/problems/sort-colors/description/
# Example
# Given an array with n objects colored red, white or blue, sort them in-place 
# so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#
# Example:
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:
#
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?

"""
Algo: Two pointers
D.S.:

Solution:
Partition 模板
p1 + 1 是下一个0的位置
P2 - 2 是下一个2的位置
cur 以前都是拍好的数，如果P2后面的数换过 CUR 换来一个新数，不要后挪

Corner cases:
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = -1
        p2 = len(nums)
        cur = 0
        while cur < p2:
            if nums[cur] == 0:
                p1 += 1
                nums[cur], nums[p1] = nums[p1], nums[cur]
                cur += 1
            elif nums[cur] == 2:
                p2 -= 1
                nums[cur], nums[p2] = nums[p2], nums[cur]
            else:
                cur += 1


# Test Cases
if __name__ == "__main__":
    solution = Solution()
