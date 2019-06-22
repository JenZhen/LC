#! /usr/local/bin/python3

# no permission
# LC 253 High freq
# Example
# Given a list of meeting room intervals consisting start and end time [[s1,e1], [s2,e2] ... ]
# si < ei, find the mininum number of conference room needed
# 给定一系列的会议时间间隔intervals，包括起始和结束时间[[s1,e1],[s2,e2],...] (si < ei)，找到所需的最小的会议室数量。
# Example:
# [
#     [0, 30], [5, 10], [15, 20]
# ]
# return 2

"""
Algo: sweepline
D.S.:

Solution:


Corner cases:
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        ts = []
        for int in intervals:
            ts.append((int[0], 1))
            ts.append((int[1], 0))
        sorted_ts = sorted(ts, key = lambda x: (x[0], x[1]))
        print(sorted_ts)
        max_room = 0
        res = 0
        for ts in sorted_ts:
            if ts[1] == 1:
                res += 1
            else:
                res -= 1
            max_room = max(max_room, res)
        return max_room

# Test Cases
if __name__ == "__main__":
    testCases = [
        [[0, 30],[5, 10],[15, 20]],
        [[0, 30],[5, 10],[10, 20]],
        [[0, 30],[5, 10],[9, 20]]
    ]
    solution = Solution()
    for t in testCases:
        res = solution.minMeetingRooms(t)
        print(res)
