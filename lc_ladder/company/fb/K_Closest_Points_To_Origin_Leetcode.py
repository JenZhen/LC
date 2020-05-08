#! /usr/local/bin/python3

# https://leetcode.com/problems/k-closest-points-to-origin/
# Example
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
#
# (Here, the distance between two points on a plane is the Euclidean distance.)
#
# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
#
#
#
# Example 1:
#
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:
#
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
#
#
# Note:
#
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
"""
Algo: Quick Select, Quick Sort,
D.S.:

Solution:
Time: O(n) - n is number of all points
Space: O(1)

这个题要对比着 Lintcode https://www.lintcode.com/problem/k-closest-points/description 来学习
这个题要求：
前K个最近距离，不需要排序
利用快排序的pivot模板排 这里抄袭quick sort partition 模板就行
选择一个Pivot点，左边都是比他小的，右边都是比他大的，返回这个Pivot点应在的index 和K做比较
最后复杂度是O(n)

lintcode 要求：
前K个最近距离，需要排序
因为要排序所有么有便捷方法，用heap of size k, 最后复杂度
O(n logk) 如果 k 不大，n >> k 结果还是比较理想的
最坏的结果是O(nlogn) where k ~= n

Corner cases:
"""

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points or len(points) == 0 or not K:
            return []
        if len(points) <= K:
            return points
        self.sort(points, 0, len(points) - 1, K - 1)
        return points[:K]

    def sort(self, points, l, r, K):
        if l >= r:
            return
        pos = self.partition(points, l, r)
        if pos == K:
            return
        elif pos < K:
            self.sort(points, pos + 1, r, K)
        else:
            self.sort(points, l, pos - 1, K)

    def partition(self, points, l, r):
        pos = l - 1
        pivot = self.get_distance(points[r])

        for i in range(l, r + 1):
            if self.get_distance(points[i]) <= pivot:
                pos += 1
                points[pos], points[i] = points[i], points[pos]
        return pos

    def get_distance(self, coor):
        return coor[0] ** 2 + coor[1] ** 2

# Test Cases
if __name__ == "__main__":
    solution = Solution()
