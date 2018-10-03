#! /usr/local/bin/python3

# https://www.lintcode.com/problem/two-sum-unique-pairs/description?_from=ladder&&fromId=59
# Example
# 给一整数数组, 找到数组中有多少组 不同的元素对 有相同的和, 且和为给出的 target 值, 返回对数.
#
# 样例
# 给一数组 nums = [1,1,2,45,46,46], target = 47, 返回 2
# 1 + 46 = 47
# 2 + 45 = 47

"""
Algo:
D.S.: 2 points 2-end moving towards

Solution:
Time: O(n)

Corner cases:
"""

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        res = 0
        if not nums or target is None:
            return res

        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            ttl = nums[l] + nums[r]
            if ttl == target:
                res += 1
                l += 1
                r -= 1
                while l < len(nums) and nums[l] == nums[l - 1]:
                    l += 1
                while r >= 0 and nums[r] == nums[r + 1]:
                    r -= 1
            elif ttl > target:
                r -= 1
            else:
                l += 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
