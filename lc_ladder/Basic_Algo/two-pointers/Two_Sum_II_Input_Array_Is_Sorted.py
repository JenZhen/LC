#!/usr/bin/python

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Example, assume there's only 1 exact pair

"""
Algo:
D.S.: 2 pointes narrowing down algo

Solution:
How to use 2 pointers to narrow down range of a sorted array

Time: O(n)
Space: O(1)

Corner cases:
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] > target:
                r = r - 1
            if numbers[l] + numbers[r] < target:
                l = l + 1
        return []

# Test Cases
if __name__ == "__main__":
    solution = Solution()
