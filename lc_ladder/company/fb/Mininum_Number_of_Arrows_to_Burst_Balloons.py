#! /usr/local/bin/python3

# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/submissions/
# Example
# There are a number of spherical balloons spread in two-dimensional space.
# For each balloon, provided input is the start and end coordinates of the horizontal diameter.
#
# Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice.
# Start is always smaller than end. There will be at most 104 balloons.
# An arrow can be shot up exactly vertically from different points along the x-axis.
# A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend.
# There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.
# Example:
# Input:
# [[10,16], [2,8], [1,6], [7,12]]
#
# Output:
# 2
# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""
Algo: Merge intervals/Find intersections
D.S.:

Solution1:

Time: O(nlogn) sort all intervals
Space: O(n) -- for intervals

Corner cases:
"""
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key=lambda x: x[0])
        intervals = [points[0]]
        for i in range(1, len(points)):
            s, e = points[i]
            if s > intervals[-1][1]:
                intervals.append([s, e])
            else:
                intervals[-1][0] = max(s, intervals[-1][0])
                intervals[-1][1] = min(e, intervals[-1][1])
        return len(intervals)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
