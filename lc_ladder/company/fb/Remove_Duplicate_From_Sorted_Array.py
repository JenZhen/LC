#! /usr/local/bin/python3

# https://www.lintcode.com/problem/remove-duplicates-from-sorted-array/description
# Example
# 给定一个排序数组，在原数组中“删除”重复出现的数字，使得每个元素只出现一次，并且返回“新”的数组的长度。
#
# 不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。
#
# 样例
# 样例 1:
# 	输入:  []
# 	输出: 0
#
#
# 样例 2:
# 	输入:  [1,1,2]
# 	输出: 2
#
# 	解释:
# 	数字只出现一次的数组为: [1,2]

"""
Algo:
D.S.:

Solution:


Corner cases:
"""

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if not nums:
            return 0
        n = len(nums)
        if n == 0 or n == 1:
            return n

        idx = 0
        for i in range(1, n):
            if nums[idx] != nums[i]:
                idx += 1
                nums[idx] = nums[i]
        return idx + 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
