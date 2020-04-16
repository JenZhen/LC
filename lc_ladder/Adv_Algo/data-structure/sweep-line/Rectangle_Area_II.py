#! /usr/local/bin/python3

# https://leetcode.com/problems/rectangle-area-ii/submissions/
# Example
# We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] ,
# where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.
#
# Find the total area covered by all rectangles in the plane.  Since the answer may be too large, return it modulo 10^9 + 7.
#
# Example 1:
#
# Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# Output: 6
# Explanation: As illustrated in the picture.
# Example 2:
#
# Input: [[0,0,1000000000,1000000000]]
# Output: 49
# Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
# Note:
#
# 1 <= rectangles.length <= 200
# rectanges[i].length = 4
# 0 <= rectangles[i][j] <= 10^9
# The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.
"""
Algo:
D.S.:

Solution:
Sweep line:
找一个平行于x轴垂直于Y轴，由下向上 平移

Time: O(n * nlogn)
Space: O(n)

Corner cases:
"""

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        OPEN, CLOSE = 0, 1
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2)) # 下底出现，记录宽度
            events.append((y2, CLOSE, x1, x2)) # 上底出现，记录宽度
        events.sort()
        print(events)

        active_x = [] # 记录现在没有完结的所有矩形的宽度 起止点
        cur_y = events[0][0] # 找到最低的lowest y
        res = 0

        for y, type, x1, x2 in events:
            res += self.merge_active_x(active_x) * (y - cur_y)

            # update active x intervals
            if type is OPEN:
                # 加入一个新的矩形宽
                active_x.append((x1, x2))
            else:
                # 一个矩形完结，把它的宽删除
                active_x.remove((x1, x2))

            # update current y level
            cur_y = y

        return res % (10 ** 9 + 7)

    def merge_active_x(self, active_x):
        # 返回当前X轴有多宽 并集
        active_x.sort()
        res = 0
        cur = -1
        for x1, x2 in active_x:
            cur = max(cur, x1)
            res += max(0, x2 - cur)
            cur = max(cur, x2)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
