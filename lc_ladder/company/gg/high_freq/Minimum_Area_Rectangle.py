#! /usr/local/bin/python3

# https://leetcode.com/problems/minimum-area-rectangle/
# Example
# Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.
#
# If there isn't any rectangle, return 0.

# Example 1:
#
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# Example 2:
#
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
#
#
# Note:
#
# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.

"""
Algo:
D.S.:

Solution:
遍历2个点可以构成对角线 -- 2个点的x y 不一样
这时候可以推算出另外两个点
如何快速找到另外两个点是否存在 -- 建立map，在最初，建立x - y 的map，
Time: O(n ^ 2)

Corner cases:
"""

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        xmap = {} # key x, val set of y
        for p in points:
            if p[0] not in xmap:
                xmap[p[0]] = set()
            xmap[p[0]].add(p[1])
        import sys
        res = sys.maxsize
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                if x1 == x2 or y1 == y2: continue # if not a diagnal continue
                x3, y3 = x1, y2
                x4, y4 = x2, y1
                if y2 not in xmap[x1] or y1 not in xmap[x2]: continue
                res = min(res, abs(x1 - x2) * abs(y1 - y2))
        return res if res != sys.maxsize else 0

# Test Cases
if __name__ == "__main__":
    solution = Solution()
