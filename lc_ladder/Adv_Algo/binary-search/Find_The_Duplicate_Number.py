#! /usr/local/bin/python3

# https://lintcode.com/problem/find-the-duplicate-number/description
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
#
# Requiremnet
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated more than once.
# Example

"""
Algo: Binary Search
D.S.:

Solution:
Similar to: Wood_Cut, Copy_Books

1. 找到可行解的范围: 1 - n (只有一个数重复，数的可能范围1 - n, 共 n + 1个数)
2. 猜答案 （二分）: (l + r ) // 2，对可行解范围进行二分
3. 检验条件，来判断答案应该在哪一侧
getCntLT: 遍历数组，数<= target的数有几个。例，target=4, 数到<=4的有<=4个，说明重复的数在4右边，比4大
4. 调整搜索范围
特征：# TODO 不明显

Time：O(nlogn)

Corner cases:
"""

class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        # write your code here
        if not nums:
            return 0
        l, r = 1, len(nums)
        while l + 1 < r:
            mid = (l + r) // 2
            if self.getCntLT(nums, mid) > mid:
                # dup is less than mid
                r = mid
            else:
                l = mid
        # 说明比l小的数里面没有重复的，在l的右边
        if self.getCntLT(nums, l) <= l:
            return r
        else:
            return l

    def getCntLT(self, nums, target):
        res = 0
        for num in nums:
            if num <= target:
                res += 1
        return res

# Test Cases
if __name__ == "__main__":
    s = Solution()
