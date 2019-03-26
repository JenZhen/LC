#! /usr/local/bin/python3

# https://www.lintcode.com/problem/remove-duplicates-from-sorted-array-ii/
# Example
# 给你一个排序数组，删除其中的重复元素，使得每个数字最多出现两次，返回新的数组的长度。
# 如果一个数字出现超过2次，则这个数字最后保留两个。
#
# 样例
# 样例 1:
# 	输入: []
# 	输出: 0
#
#
# 样例 2:
# 	输入:  [1,1,1,2,2,3]
# 	输出: 5
#
# 	样例解释:
# 	长度为 5，  数组为：[1,1,2,2,3]
# 注意事项
# 需要在原数组中操作

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
        n = len(nums)
        if n == 0 or n == 1:
            return n
        idx = 0
        cnt = 1
        for i in range(1, n):
            if nums[idx] == nums[i]:
                if cnt < 2:
                    idx += 1
                    nums[idx] = nums[i]
                    cnt += 1
            else:
                idx += 1
                nums[idx] = nums[i]
                cnt = 1
        print(nums)
        print(idx + 1)
        return idx + 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
