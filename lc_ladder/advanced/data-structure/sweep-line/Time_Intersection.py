#! /usr/local/bin/python3

# https://www.lintcode.com/problem/time-intersection/description
# Example

# 目前有两个用户的有序在线时间序列，每一个区间记录了该用户的登录时间点x和离线时间点y，请找出这两个用户同时在线的时间段，输出的时间段请从小到大排序。
#
# 样例
# 给出 seqA = [(1,2),(5,100)], seqB = [(1,6)], 返回 [(1,2),(5,6)]。
#
# 解释：
# 在(1,2),(5,6) 这两个时间段内，两个用户同时在线。
# 给出 seqA = [(1,2),(10,15)], seqB = [(3,5),(7,9)]，返回 []。
#
# 解释：
# 不存在任何时间段，两个用户同时在线。
# 注意事项
# 我们保证在线时间序列的长度 1 <= len <= 1e6。
# 我们保证在线时间序列是合法的，即对于某一个用户的在线时间序列，它的任意两个区间不相交。

"""
Algo:
D.S.:

Solution:
O(nlogn) -- n = max(lenA, lenB)

Corner cases:
"""

"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """
    def timeIntersection(self, seqA, seqB):
        # Write your code here
        points = []
        for interval in seqA + seqB:
            print("interval: %s" %repr(interval.start))
            points.append((interval.start, True))
            points.append((interval.end, False))

        online = 0
        intervals = []
        points = sorted(points, key=lambda x: (x[0], x[1]))
        print("points: %s" %repr(points))
        for timestamp, delta in points:
            if delta:
                online += 1
                if online == 2:
                    intervals.append([timestamp, None])
            else:
                online -= 1
                if online == 1:
                    intervals[-1][1] = timestamp
        return intervals

# Test Cases
if __name__ == "__main__":
    def buildSeq(originSeq):
        seq = []
        for s in originSeq:
            newIntv = Interval(s[0], s[1])
            seq.append(newIntv)
        return seq

    testCases = [
        {
            "seqA": [(1,2),(5,100)],
            "seqB": [(1,6)]
        }
    ]
    solution = Solution()
    for t in testCases:
        seqA = buildSeq(t["seqA"])
        seqB = buildSeq(t["seqB"])
        res = solution.timeIntersection(seqA, seqB)
        print("res: %s" %repr(res))
