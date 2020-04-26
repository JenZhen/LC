#! /usr/local/bin/python3

# https://www.lintcode.com/problem/find-all-numbers-disappeared-in-an-array/description?_from=ladder&&fromId=18
# Example
# 给定一个整数数组，其中1 ≤ a[i] ≤ n (n =数组的大小)，一些元素出现两次，其他元素出现一次。
#
# 找到 [1,n] 中所有没有出现在此数组中的元素。
#
# 你可以在没有额外空间和O(n)运行时的情况下完成吗？ 您可以认为返回的列表不计为额外空间。
#
# 样例
# 输入:
# [4,3,2,7,8,2,3,1]
#
# 输出:
# [5,6]

"""
Algo: array
D.S.:

Solution:

Time: O(n) Space O(1)
容易想到新开一个数组来记录某个位置是否访问过。
如果不额外使用空间，就需要在原数组的基础上修改。
如果在原数组记录是否被访问过？ 如果没被访问过，原数值【1， n】如果被访问过，无论是第几次都是【-1， -n】
最后过一遍数组还是positive value的位置就是没有被访问过的

注意index和value的转换不要越界
Corner cases:
"""

class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def findDisappearedNumbers(self, nums):
        # write your code here
        if not nums:
            return []

        ans = []
        for idx in range(len(nums)):
            newIdx = abs(nums[idx]) - 1
            nums[newIdx] = -abs(nums[newIdx])
        for idx in range(len(nums)):
            if nums[idx] > 0:
                ans.append(idx + 1)
        return ans

# Test Cases
if __name__ == "__main__":
    solution = Solution()
