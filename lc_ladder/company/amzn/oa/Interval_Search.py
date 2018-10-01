#! /usr/local/bin/python3

# https://www.lintcode.com/problem/interval-search/description?_from=ladder&&fromId=62
# Example
# 给定一个 List ，其中元素是 区间, 区间的长度是 1000, 例如 [500,1500], [2100,3100].给定一个 number 计算并确认是否在这些区间内.返回 True 或 False.
#
# 样例
# 给定:
#
# List = [[100,1100],[1000,2000],[5500,6500]]
# number = 6000
# 返回: True

"""
Algo:
D.S.:

Solution:

class Solution:
    """
    @param intervalList:
    @param number:
    @return: return True or False
    """
    def isInterval(self, intervalList, number):
        # Write your code here
        if not intervalList or number is None:
            return "False"
        for itv in intervalList:
            if itv[0] <= number <= itv[1]:
                return "True"
        return "False"


Corner cases:
"""

# Test Cases
if __name__ == "__main__":
    solution = Solution()
