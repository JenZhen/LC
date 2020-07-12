#! /usr/local/bin/python3

# https://leetcode.com/problems/minimum-area-rectangle-ii
# Example
# Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points,
# with sides not necessarily parallel to the x and y axes.
#
# If there isn't any rectangle, return 0.
#
# Input: [[1,2],[2,1],[1,0],[0,1]]
# Output: 2.00000
# Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
#
# Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
# Output: 1.00000
# Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
#
# Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
# Output: 0
# Explanation: There is no possible rectangle to form from these points.
"""
Algo:
D.S.:

Solution1:
构成矩形条件，对角线中点在一起，对角线长度一样
若是要求正方形，还需要 对角线垂直

遍历所有的边：
建立map:
# mp = {
#     (mid_x, mid_y): {
#         length: [(p1, p2), (p3, p4)]
#     }
# }
中点坐标:
    边长：[(p1, p2), (p3, p4)] 这样 p1,p2,p3,p4 可以构成一个矩形

Solution2:
Time: O(n^3)
1. 遍历3个点可以构成一个三角形
2. 通过求点积算是这个3个点是否构成一个直角三角形 (math)
3. 如果构成直角三角形，可以推算出第四个点 (math)
4. 第四格点是否存在？在初始化时建立x->y 的map, 需要判断x是否在map，y是否在map

这时候可以推算出另外两个点
如何快速找到另外两个点是否存在 -- 建立map，在最初，建立x - y 的map，

Corner cases:
"""

class Solution1:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        if not points:
            return 0

        # mp = {
        #     (mid_x, mid_y): {
        #         length: [(p1, p2), (p3, p4)]
        #     }
        # }
        mp = {}
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                p1, p2 = points[i], points[j]
                midx, midy = (p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0
                dist = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                if (midx, midy) not in mp:
                    mp[(midx, midy)] = {}
                if dist not in mp[(midx, midy)]:
                    mp[(midx, midy)][dist] = []
                mp[(midx, midy)][dist].append((p1, p2))

        res = sys.maxsize
        for key, val in mp.items():
            for length, pair_list in val.items():
                n = len(pair_list) # number of edges
                for i in range(n):
                    for j in range(i + 1, n):
                        p1, p2 = pair_list[i][0], pair_list[i][1]
                        p3, p4 = pair_list[j][0], pair_list[j][1]
                        e1 = ((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2) ** 0.5
                        e2 = ((p1[0] - p4[0]) ** 2 + (p1[1] - p4[1]) ** 2) ** 0.5
                        area = e1 * e2
                        res = min(res, area)
        return res if res != sys.maxsize else 0

class Solution2:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
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
            for j in range(len(points)):
                if j == i: continue
                for k in range(len(points)):
                    if k == i or k == j: continue
                    p1 = points[i]
                    p2 = points[j]
                    p3 = points[k]
                    dot_product = (p2[0] - p1[0]) * (p3[0] - p1[0]) + (p2[1] - p1[1]) * (p3[1] - p1[1])
                    if dot_product != 0: # not chui zhi
                        continue
                    p4_x = p2[0] + p3[0] - p1[0];
                    p4_y = p2[1] + p3[1] - p1[1];
                    print(p4_x, p4_y)
                    if p4_x not in xmap: continue
                    if p4_y not in xmap[p4_x]: continue
                    a = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
                    b = (p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2
                    res = min(res, a * b)
        return res ** 0.5 if res != sys.maxsize else 0
# Test Cases
if __name__ == "__main__":
    solution = Solution()
