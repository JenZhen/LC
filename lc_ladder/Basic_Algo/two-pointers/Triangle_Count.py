#!/usr/bin/python

# https://leetcode.com/problems/valid-triangle-number/description/
# Example
# Given an array consists of non-negative integers, your task is to count the number of 
# triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
# Example 1:
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# Note:
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].

"""
Algo:
D.S.:

Solution:
直白的想法是三重循环，i, j, k, 只要满足S[i] + S[j] > S[k]，或者S[i] + S[j] > S[k], 或者S[j] + S[k] > S[i]，该组合就计入总数。 不过显然，这种算法复杂度较高，为O(n^3)。

可以对问题进行转化：
-对数组排序，按照O(nlogn)计
-对数组下标循环，则内部转化为一个two sum II问题，即寻找 S[j] + S[k] > S[i]有多少组，因为数组已排序，则可以使用two pointers的方法
-对于每一个i，初始化left = 0, right = i - 1，如果有一个满足S[left] + S[right] > S[i], 那么对于left ~ right - 1 同样也满足，因此计入right-left到最终count中
- 固定一个S[i]： 从sorted S的最右边最大的数开始
- 如何便利left -> right 的所有组合？
    - 固定right从 S[i]左第一个开始
    - then narrow down range of left right
最终算法复杂度为O(n^2 + nlogn)
Corner cases:
"""

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        cnt = 0
        m = length - 1
        while m >= 2:
            # i marks the largest number
            i, j = m - 1, m - 2
            while j >= 0 and nums[i] + nums[j] > nums[m]:
                j -= 1

            j += 1
            while j < i:
                cnt += (i - j)
                i -= 1
                # narrow down i (nums[i] gets smaller)
                # j moves right to satisfy validity
                # note there condition is "INVALIDITY", then j move further right
                while j < i and nums[i] + nums[j] <= nums[m]:
                    j += 1
            m -= 1
        return cnt

# Test Cases
if __name__ == "__main__":
    solution = Solution()
