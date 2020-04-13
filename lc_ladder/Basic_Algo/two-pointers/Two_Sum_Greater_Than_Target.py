#!/usr/bin/python

# http://www.jiuzhang.com/solution/two-sum-greater-than-target/
# Example
# Given an array of integers, find how many pairs in the array such that
# their sum is bigger than a specific target number. Please return the number of pairs.

"""
Algo: Sort, two pointers
D.S.:

Solution:
Same as Two Sum - Less than or equal to
Using sort method
Time O(nlogn)
Space O(1)

Corner cases:
"""
class Solution:
    # @param nums, an array of integer
    # @param target, an integer
    # @return an integert

    def twoSum2_1(self, nums, target):
        # Write your code here
        if len(nums) < 2 or target is None:
            return 0
        cnt = 0
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total <= target:
                l += 1
            else:
                cnt += (r - l)
                r -= 1
        return cnt

# Test Cases
if __name__ == "__main__":
    solution = Solution()
