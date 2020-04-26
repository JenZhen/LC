#! /usr/local/bin/python3

# https://leetcode.com/problems/remove-interval/
# Example
# Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b]
# represents the set of real numbers x such that a <= x < b.
#
# We remove the intersections between any interval in intervals and the interval toBeRemoved.
#
# Return a sorted list of intervals after all such removals.
#
# Example 1:
#
# Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
# Output: [[0,1],[6,7]]
# Example 2:
#
# Input: intervals = [[0,5]], toBeRemoved = [2,3]
# Output: [[0,2],[3,5]]
#
#
# Constraints:
#
# 1 <= intervals.length <= 10^4
# -10^9 <= intervals[i][0] < intervals[i][1] <= 10^9

"""
Algo: Sweep Line
D.S.:

Solution:
注意
1. 找交集和找不相交 部分的方法
    2段相交可以找到1个段
    2段不相交可以找到之多2个段（左右端点）
2. 根据题目定义 如何处理边界

Corner cases:
"""

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        # intervals are sorted, compare with toBeRemoved one by one
        res = []
        rm_st, rm_end = toBeRemoved[0], toBeRemoved[1]
        for itv in intervals:
            st, end = itv[0], itv[1]
            left, right = [], []
            if st < rm_st:
                left = [st, min(end, rm_st)]
                res.append(left[:])

            if end > rm_end:
                right = [max(rm_end, st), end]
                res.append(right[:])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
