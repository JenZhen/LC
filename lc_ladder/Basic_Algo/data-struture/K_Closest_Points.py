#!/usr/bin/python

# http://www.lintcode.com/en/problem/k-closest-points/
# Example

"""
Algo:
D.S.:

Solution:

Corner cases:
"""

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

from heapq import heappop, heappush
class Solution:
    """
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """
    from heapq import heappop, heappush

    def kClosest(self, points, origin, k):
        # write your code here
        if points is None or k is None or k == 0:
            return None
        heap = []
        res = []
        for p in points:
            dist = self.getDist(p, origin)
            self.heapPushPoint(heap, p, dist)
        for i in range(k):
            if heap:
                res.append(heappop(heap)[1])
        return res

    def getDist(self, p, origin):
        return (p.x - origin.x)**2 + (p.y - origin.y)**2

    def heapPushPoint(self, heap, p, dist):
        heappush(heap, (dist, p))


# helper printPoints
def printPoints(points):
    print ("Points: [")
    for p in points:
        print ("[%s, %s]" %(p.x, p.y))
    print ("]")

# Test Cases
if __name__ == "__main__":
    points = [
        Point(0, 1),
        Point(1, 0),
        Point(1, 1),
        Point(0.5, 0.5)
    ]

    origin = Point(0, 0)
    solution = Solution()
    res = solution.kClosest(points, origin, 3)
    printPoints(res)

