#! /usr/local/bin/python3

# https://leetcode.com/problems/single-element-in-a-sorted-array/submissions/
# Example
# You are given a sorted array consisting of only integers where every element appears exactly twice,
# except for one element which appears exactly once. Find this single element that appears only once.
# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
"""
Algo: bit operation
D.S.:

Solution:
XOR  异或算法 ^
Time: O(n)
Space: O(1)
Corner cases:
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if not nums: return None
        res = nums[0]
        for i in range(1, len(nums)):
            res = res ^ nums[i]
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
