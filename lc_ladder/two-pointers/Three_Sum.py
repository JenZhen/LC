#!/usr/bin/python

# Requirement
# https://leetcode.com/problems/3sum/description/

"""
Algo: Sort and two pointers
D.S.:

Solution:
- 3 element pair, if brutal-force it would take O(n^3)
fix one element then using 2Sum for the other 2 element can take advantage of O(n),
making O(n^2) in total
- Sort the array if original ids is not required. Sorting takes O(nlogn) < O(n^2)

In total: time O(n^2) space O(n)

Corner cases:
Duplicate element, same value not count as twice
if it makes 2 [-1, 0, 1] need to check with interviewer to decide if appear in res twice
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 3:
            return []

        nums.sort()
        res = []
        for i in range(length - 2):
            # note if fixing point need to check dup
            # note that this is an "if" not "while"
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * (-1)
            l, r = i + 1, length - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # this is to remove duplicate
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,1,2,-1,-4,-1]
    print(solution.threeSum(nums))

