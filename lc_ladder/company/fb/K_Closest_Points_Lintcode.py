#! /usr/local/bin/python3

# https://www.lintcode.com/problem/k-closest-points/description
# Example
# 给定一些 points 和一个 origin，从 points 中找到 k 个离 origin 最近的点。按照距离由小到大返回。如果两个点有相同距离，则按照x值来排序；若x值也相同，就再按照y值排序。
#
# 样例
# 例1:
#
# 输入: points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
# 输出: [[1,1],[2,5],[4,4]]
# 例2:
#
# 输入: points = [[0,0],[0,9]], origin = [3, 1], k = 1
# 输出: [[0,0]]

"""
Algo: sort, top k,
D.S.: heap

Solution:
Time: O(n log k)
Space: O(k)

这个题要结合着Leetcode的来看 https://leetcode.com/problems/k-closest-points-to-origin/

因为要排序所有么有便捷方法，用heap of size k, 最后复杂度
O(n logk) 如果 k 不大，n >> k 结果还是比较理想的
最坏的结果是O(nlogn) where k ~= n， 这个和把所有的都排序的暴力解法是一样的复杂度

一些细节
- 这里使用的是Max heap, python heapq default是min heap 如何转换，注意细节！！
- heap 的sort方法有多重条件， 1） 先按距离，2）再按x值 3）再按y值
要记住再heapq中，直接这样使用就可以
heappush(heap, (-dist, -p.x, -p.y))

Corner cases:
"""


"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        if not points:
            return []

        from heapq import heappush, heappop
        heap = []
        res = []

        def get_dist(a, b):
            return (a.x - b.x) ** 2 + (a.y - b.y) ** 2

        for p in points:
            dist = get_dist(p, origin)
            heappush(heap, (-dist, -p.x, -p.y))
            if len(heap) > k:
                heappop(heap)
        while heap:
            minele = heappop(heap)
            x, y = -minele[1], -minele[2]
            res.append([x, y])
        return res[::-1]


# Test Cases
if __name__ == "__main__":
    solution = Solution()
