#! /usr/local/bin/python3

# https://www.lintcode.com/problem/non-decreasing-array/description?_from=ladder&&fromId=18
# Example
# 给定一个包含 n 个整数的数组，你的任务是检测在改变至多一个元素的情况下，它是否可以变成不下降的。
#
# 我们定义一个数组是不下降的，如果 array[i] <= array[i + 1] 对于每一个 i (1 <= i < n) 都成立。
#
# 样例
# 样例1:
#
# 输入: [4,2,3]
# 输出: True
# 解释: 你可以把第一个4修改为1从而得到一个不下降数组。
# 样例2:
#
# 输入: [4,2,1]
# 输出: False
# 解释: 你无法得到一个不下降数组，在修改至多一个元素的情况下。
# 注意事项
# n 属于 [1, 10,000].

"""
Algo: compare element
D.S.: array

Solution:
Time: O(n), Space: O(1)
重点在考虑Corner cases
Corner cases:
1. 不需要改动的： cnt == 0
2. 需要改第一个： 4，2，3，lowIdx == 1
3. 需要改最后一个：2，3，1. lowIdx = len(nums) - 1
4. 需要改中间的，山形状： 2，5，3. nums[lowIdx - 2] <= nums[lowIdx]
5. 需要改中间的，脊形状： 2，1，4. nums[lowIdx - 1] <= nums[lowIdx + 1]

"""
class Solution:
    """
    @param nums: an array
    @return: if it could become non-decreasing by modifying at most 1 element
    """
    def checkPossibility(self, nums):
        # Write your code here
        cntDesc = 0
        lowIdx = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                cntDesc += 1
                lowIdx = i
        if cntDesc == 0:
            return True
        if cntDesc > 1:
            return False

        return lowIdx == 1 or \
                lowIdx == len(nums) - 1 or \
                nums[lowIdx - 2] <= nums[lowIdx] or \
                nums[lowIdx - 1] <= nums[lowIdx + 1]
# Test Cases
if __name__ == "__main__":
    solution = Solution()
