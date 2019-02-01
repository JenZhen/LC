#! /usr/local/bin/python3

# https://www.lintcode.com/problem/shortest-unsorted-continuous-subarray/description?_from=ladder&&fromId=18
# Example
# 给定一个整数数组，你需要找到一个连续子数组，如果你只按升序对这个子数组进行排序，那么整个数组也将按升序排序。
#
# 你需要找到最短的这样的子数组并输出它的长度。
#
# 样例
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你需要对[6, 4, 8, 10, 9]按升序排列从而整个数组也变为升序。
# 注意事项
# 输入的数组长度范围为[1, 10,000]。
# 输入的数组可能会包含重复元素，本题升序的含义为<=。
"""
Algo: sorting
D.S.: array

Solution:
Time: O(n), Space: O(1)

Corner cases:
- equal elements
- all sorted array, careful about init of upper, lower bound

"""

class Solution:
    """
    @param nums: an array
    @return: the shortest subarray's length
    """
    def findUnsortedSubarray(self, nums):
        # Write your code here
        if not nums:
            return 0
        maxval = nums[0]
        minval = nums[-1]
        upper, lower = -1, 0 # init this way for the case of all sorted
        for i in range(len(nums)):
            if nums[i] > maxval:
                maxval = nums[i]
            if nums[i] < maxval:
                upper = i
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < minval:
                minval = nums[i]
            if nums[i] > minval:
                lower = i
        print(upper, lower)
        return upper - lower + 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
