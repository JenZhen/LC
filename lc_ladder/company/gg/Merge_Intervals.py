#! /usr/local/bin/python3

# https://lintcode.com/problem/merge-intervals/description
# Example
# Given a collection of intervals, merge all overlapping intervals.
#
# Example
# Given intervals => merged intervals:
#
# [                     [
#   (1, 3),               (1, 6),
#   (2, 6),      =>       (8, 10),
#   (8, 10),              (15, 18)
#   (15, 18)            ]
# ]
# Challenge
# O(n log n) time and O(1) extra space.

"""
Algo:
D.S.:

Solution:
O(n log n) time and O(1) extra space.
Since space requirement is O(1), cannot seperate start and end point, which will take extra space

Merge as the start point, then try to merge the later one into prev one.

Pay attention to sorting method
Corner cases:
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __repr__(object):
        print("[%s, %s]" %(self.start, self.right)
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if not intervals:
            return intervals

        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            prev = res[-1]
            curSt, curEd = intervals[i].start, intervals[i].end
            prevSt, prevEd = prev.start, prev.end
            if curSt <= prevEd:
                # merge
                prev.end = max(curEd, prevEd)
            else:
                res.append(intervals[i])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
