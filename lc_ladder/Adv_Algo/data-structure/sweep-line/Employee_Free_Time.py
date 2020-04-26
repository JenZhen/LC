#! /usr/local/bin/python3

# https://leetcode.com/problems/employee-free-time/submissions/
# Example
# We are given a list schedule of employees, which represents the working time for each employee.
#
# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
#
# Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.
#
# (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals,
# not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
#
# Example 1:
#
# Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation: There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
# Example 2:
#
# Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]

"""
Algo: Sweeping line
D.S.:

Solution:
Time: O(nlogn)

Corner cases:
"""


"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        events = []
        for emp in schedule:
            for itv in emp:
                # 注意：在时间点重合时候 要先考虑起点，再终点
                events.append((itv.start, False))
                events.append((itv.end, True))
        events.sort()

        cnt = 0
        prev = None
        res = []
        for e_ts, e_type in events:
            # 重要的判断条件
            if cnt == 0 and prev != None:
                res.append(Interval(prev, e_ts))
            if e_type == False:
                cnt -= 1
            else:
                cnt += 1
            prev = e_ts
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
