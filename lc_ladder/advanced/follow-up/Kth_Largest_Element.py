#! /usr/local/bin/python3

# https://www.lintcode.com/problem/kth-largest-element/description
# Example
# 在数组中找到第k大的元素
#
# 样例
# 给出数组 [9,3,2,4,8]，第三大的元素是 4
#
# 给出数组 [1,2,3,4,5]，第一大的元素是 5，第二大的元素是 4，第三大的元素是 3，以此类推
#
# 挑战
# 要求时间复杂度为O(n)，空间复杂度为O(1)
#
# 注意事项
# 你可以交换数组中的元素的位置

"""
Algo: Quick Select for 第几大/小问题
D.S.:

Solution:
背诵quick select 模版

Corner cases:
"""

class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not n or not nums or n > len(nums):
            return None

        return self.findKSmallest(nums, 0, len(nums) - 1, len(nums) - n)

    def findKSmallest(self, nums, start, end, k):
        # k is the idx not the kth
        # if find 2nd smallest, k = 1
        if start >= end:
            return nums[k]
        l, r = start, end
        pivot = nums[(start + end) // 2]
        while l <= r:
            while l <= r and nums[l] < pivot:
                l += 1
            while l <= r and nums[r] > pivot:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        if k <= r:
            return self.findKSmallest(nums, start, r, k)
        if k >= l:
            return self.findKSmallest(nums, l, end, k)
        return nums[k]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
