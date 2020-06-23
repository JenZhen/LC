#! /usr/local/bin/python3

# https://www.lintcode.com/problem/product-of-array-except-self/description
# Example
# 给定n个整数的数组nums，其中n> 1，返回一个数组输出，使得output [i]等于nums的所有除了nums [i]的元素的乘积。
#
# Example
# 样例1
#
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
# 解释:
# 2*3*4=24
# 1*3*4=12
# 1*2*4=8
# 1*2*3=6
# 样例2
#
# 输入: [2,3,8]
# 输出: [24,16,6]
# 解释:
# 3*8=24
# 2*8=16
# 2*3=6
# Challenge
# 你可以用常数空间复杂度来解决这个问题吗？（注意：出于空间复杂度分析的目的，输出数组不算作额外空间）
#
# Notice
# 在没有除和O(n)时间内解决


"""
Algo: 数组左右各扫一遍
D.S.: Array

Solution:
origin [1,2,3,4]
left   [1,1,2,6]
right  [24,12,4,1]
res
Time：O(n)
Space：O(n)

Solution2:
优化：从右向左 只用一个整数代替整个数组
Time：O(n)
Space：O(1)

Corner cases:
"""

class Solution1:
    """
    @param nums: an array of integers
    @return: the product of all the elements of nums except nums[i].
    """
    def productExceptSelf(self, nums):
        # write your code here
        n = len(nums)
        from_left = [1] * n
        from_right = [1] * n
        res = [1] * n
        for i in range(1, n):
            from_left[i] = nums[i - 1] * from_left[i - 1]
        for i in range(n - 2, -1, -1):
            from_right[i] = nums[i + 1] * from_right[i + 1]
        for i in range(n):
            res[i] = from_left[i] * from_right[i]
        print(from_left)
        print(from_right)
        print(res)
        return res

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # from left
        L = nums[0]
        for i in range(1, len(nums)):
            res[i] = L * res[i]
            L = L * nums[i]
        print(res)
        # from right:
        R = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = R * res[i]
            R = R * nums[i]
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
