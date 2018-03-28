#!/usr/bin/python

# http://www.jiuzhang.com/solution/two-sum-less-than-or-equal-to-target/
# Example
# Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pairs.

"""
Algo: two pointers narrow down
D.S.:

Solution:
Two pointer needs 2 features
1) extra map for quick lookup
2) sorted array

In this case, nums.sort() takes O(nlogn)
Time: O(nlogn) + O(n)
Space: O(1)

Corner cases:
Consider duplicate numbers as different pairs
"""

class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum5(self, nums, target):
        # Write your code here
        if len(nums) < 2 or not target:
            return 0

        l, r = 0, len(nums) - 1
        cnt = 0
        nums.sort()
        while l < r:
            total = nums[l] + nums[r]
            if total > target:
                r = r - 1
            else:
                cnt += (r - l)
                l += 1
        return cnt

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    nums = [2,2,1,3,4,5,7]
    target = 5 # result 7
    print(solution.twoSum5(nums, target))
