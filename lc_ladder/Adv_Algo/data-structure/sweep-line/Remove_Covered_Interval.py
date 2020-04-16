#! /usr/local/bin/python3

# https://leetcode.com/problems/remove-covered-intervals/
# Example
# Given a list of intervals, remove all intervals that are covered by another interval in the list.
# Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
#
# After doing so, return the number of remaining intervals.
#
# Example 1:
#
# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
#
#
# Constraints:
#
# 1 <= intervals.length <= 1000
# 0 <= intervals[i][0] < intervals[i][1] <= 10^5
# intervals[i] != intervals[j] for all i != j

"""
Algo: Sweep Line
D.S.:

Solution:
先按起点升序， 在按终点降序
后面的线段终点一定比前面的大，否则就是在里面
对于相同起点，终点降序排列

Corner cases:
"""

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 起点升序，（起点一样，终点降序）
        intervals.sort(key = lambda x: (x[0], -x[1]))
        pre_end = -1
        res = 0
        for _, end in intervals:
            if end > pre_end:
                res += 1
                pre_end = end
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
