#! /usr/local/bin/python3

# https://www.lintcode.com/problem/two-sum-less-than-or-equal-to-target/description?_from=ladder&&fromId=62
# Example

# 给定一个整数数组，找出这个数组中有多少对的和是小于或等于目标值。返回对数。
#
# 样例
# 给定数组为 [2,7,11,15]，目标值为 24
# 返回 5。
# 2+7<24
# 2+11<24
# 2+15<24
# 7+11<24
# 7+15<24

"""
Algo: 2 pointers
D.S.:

Solution:
Sort nlogn

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2 or target == None:
            return 0

        length = len(nums)
        res = 0
        nums.sort()
        l, r = 0, length - 1
        while l < r:
            ttl = nums[l] + nums[r]
            if ttl > target:
                r -= 1
            else:
                res += (r - l)
                l += 1
        return res

Corner cases:
"""

# Test Cases
if __name__ == "__main__":
    solution = Solution()
