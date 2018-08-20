#! /usr/local/bin/python3

# https://www.lintcode.com/problem/house-robber-ii/description
# Example
# After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# nums = [3,6,4], return 6
"""
Algo: DP, 环状dp
D.S.:

Solution:
解决环状dp的方式


Corner cases:
"""

class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        # write your code here
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums, 0, len(nums) - 2),
                   self.helper(nums, 1, len(nums) - 1))

    def helper(self, nums, start, end):
        # start and end are inclusive
        if start == end:
            return nums[start]
        f = [0, 0]
        """
        IMPORTANT that init f with f[start % 2] and f[(start + 1) % 2]
        """
        f[start % 2] = nums[start]
        f[(start + 1) % 2] = max(nums[start], nums[start + 1])
        for i in range(start + 2, end + 1):
            f[i % 2] = max(f[(i - 1) % 2],
                           f[(i - 2) % 2] + nums[i])
        return f[end % 2]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
