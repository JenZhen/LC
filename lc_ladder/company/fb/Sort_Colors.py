#! /usr/local/bin/python3

# https://www.lintcode.com/problem/sort-colors/description
# Example
# 给定一个包含红，白，蓝且长度为 n 的数组，将数组元素进行分类使相同颜色的元素相邻，并按照红、白、蓝的顺序进行排序。
#
# 我们可以使用整数 0，1 和 2 分别代表红，白，蓝。
#
# 样例
# 给你数组 [1, 0, 1, 2], 需要将该数组原地排序为 [0, 1, 1, 2]。
#
# 挑战
# 一个相当直接的解决方案是使用计数排序扫描2遍的算法。
#
# 首先，迭代数组计算 0,1,2 出现的次数，然后依次用 0,1,2 出现的次数去覆盖数组。
#
# 你否能想出一个仅使用常数级额外空间复杂度且只扫描遍历一遍数组的算法？
#
# 注意事项
# 不能使用代码库中的排序函数来解决这个问题。
# 排序需要在原数组中进行。

"""
Algo: partition, swap
D.S.:

Solution:
重点是找到边界
Time: O(n)
Space: O(1)

Corner cases:
"""

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if not nums or len(nums) < 2:
            return nums

        n = len(nums)
        # i next 0's position from left to right
        # i's left all 0 (not including i)
        # j next 2's position from right to left
        # j's right all 0 (not including j)
        i, j = 0, n - 1
        cursor = 0
        while cursor <= j: # note should include ==, since j's next 2 not yet
            if nums[cursor] == 0:
                nums[i], nums[cursor] = nums[cursor], nums[i]
                i += 1
                cursor += 1
            elif nums[cursor] == 2:
                nums[j], nums[cursor] = nums[cursor], nums[j]
                j -= 1
            else:
                cursor += 1
        return nums

# Test Cases
if __name__ == "__main__":
    solution = Solution()
