#! /usr/local/bin/python3

# https://www.lintcode.com/problem/insert-interval/description?_from=ladder&&fromId=18
# Example
# Given a non-overlapping interval list which is sorted by start point.
#
# Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).
#
# 样例
# Insert (2, 5) into [(1,2), (5,9)], we get [(1,9)].
#
# Insert (3, 4) into [(1,2), (5,9)], we get [(1,2), (3,4), (5,9)].
"""
Algo:
D.S.:

Solution:
难点： 讨论各种可能的情况，注意边界在同一个点的情况
比较好的方式
1. 考虑完全不相交的情况，只有2个情况； 其他的就是有相交
2. 不建议在元数据上改，重新写一个result比较清晰，也比较容易构建新的after-merged interval

Corner cases:
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        res = []
        pos = 0
        for intv in intervals:
            if intv.end < newInterval.start:
                res.append(intv)
                pos += 1
            elif newInterval.end < intv.start:
                res.append(intv)
            else:
                newInterval.start = min(newInterval.start, intv.start)
                newInterval.end = max(newInterval.end, intv.end)
        res.insert(pos, newInterval)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
