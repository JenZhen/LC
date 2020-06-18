#! /usr/local/bin/python3

# https://www.lintcode.com/problem/throw-garbage/description?_from=ladder&&fromId=156
# Example
# There are n garbage bags, and the weight of each garbage bag is between [1.01, 3.00] pounds.
# You can take up to 3.00 pounds of garbage one time.
# The problem gives the weight of all garbage bags. Please figure out the minimum number of times that you can throw away all the garbage.
#
# 样例
# Example 1
# input：[1.01,2.21,1.30]
# output：2
# explain：First time throw [1.01,1.30], second time throw[2.21]
# Example 2
# input：[2.50,2.80]
# output：2
# explain：First time throw [2.50], second time throw[2.80]
# 注意事项
# 0 < n < 1000
"""
Algo: Greedy
D.S.:

Solution:


Corner cases:
"""

class Solution:
    """
    @param BagList: the weight of all garbage bags.
    @return: an integer represent the minimum number of times.
    """
    def Count_ThrowTimes(self, BagList):
        BagList.sort()
        res = 0
        l, r = 0, len(BagList) - 1
        while l < r:
            if BagList[l] + BagList[r] <= 3.0:
                res += 1
                l += 1
                r -= 1
            else:
                res += 1
                r -= 1
        if l == r:
            res += 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
