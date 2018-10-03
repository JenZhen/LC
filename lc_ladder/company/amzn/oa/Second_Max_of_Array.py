#! /usr/local/bin/python3

# https://www.lintcode.com/problem/second-max-of-array/description?_from=ladder&&fromId=59
# Example
# 在数组中找到第二大的数
#
# 样例
# 给出 [1, 3, 2, 4], 返回 3.
#
# 给出 [1, 2], 返回 1.
#
# 注意事项
# 你可以假定至少有两个数字
"""
Algo:
D.S.:

Solution:


Corner cases:
"""
class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        # write your code here
        if len(nums) == 2:
            return min(nums)
        from heapq import heappush, heappop, heapify
        h = []
        for e in nums:
            if len(h) < 2:
                heappush(h, e)
            else:
                if e > h[0]:
                    heappop(h)
                    heappush(h, e)
        return h[0]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
