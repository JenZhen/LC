#! /usr/local/bin/python3

# https://leetcode.com/problems/minimum-area-rectangle-ii
# Example

"""
Algo:
D.S.:

Solution:
Time: O(n^3)
1. 遍历3个点可以构成一个三角形
2. 通过求点积算是这个3个点是否构成一个直角三角形 (math)
3. 如果构成直角三角形，可以推算出第四个点 (math)
4. 第四格点是否存在？在初始化时建立x->y 的map, 需要判断x是否在map，y是否在map

这时候可以推算出另外两个点
如何快速找到另外两个点是否存在 -- 建立map，在最初，建立x - y 的map，

Corner cases:
"""

class Solution:
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
