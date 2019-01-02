#! /usr/local/bin/python3

# https://www.lintcode.com/problem/convex-polygon/description?_from=ladder&&fromId=18
# Example
# 给定一组点的数组，当一个多边形按顺序连接时，发现这个多边形是凸多边形(凸多边形定义)。
#
# 样例
# 给定 points = [[0, 0], [0, 1], [1, 1], [1, 0]]，返回 True.
# 解释：
# #  A  ---- B
# #  |       |
# #  D ----  C
#
# 给定 points = [[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]], 返回 False.
# 解释：
#  #  A  -------------  B
#  # |                /
#  # |               C
#  # |                 \
#  # E ---------------- D
#
# 注意事项
# 至少有3个，最多10000个点。
# 坐标在- 10000到10000之间。
# 你可以假定由给定的点组成的多边形总是一个简单的多边形(简单的多边形定义)。换而言之，我们确保每个顶点上的两条边相交，而和其他的边不相交。

"""
Algo: 几何数学
D.S.:

Solution:
这道题让我们让我们判断一个多边形是否为凸多边形，我想关于凸多边形的性质 就是所有的顶点角都不大于180度。
那么我们该如何快速验证这一个特点呢，学过计算机图形学或者是图像处理的课应该对计算法线normal并不陌生吧，计算的curve的法向量是非常重要的手段，
一段连续曲线可以离散看成许多离散点组成，而相邻的三个点就是最基本的单位，我们可以算由三个点组成的一小段曲线的法线方向，
而凸多边形的每个三个相邻点的法向量方向都应该相同，要么同正，要么同负。
那么我们只要遍历每个点，然后取出其周围的两个点计算法线方向，然后跟之前的方向对比，如果不一样，直接返回false。
这里我们要特别注意法向量为0的情况，如果某一个点的法向量算出来为0，那么正确的pre就会被覆盖为0，后面再遇到相反的法向就无法检测出来，所以我们对计算出来法向量为0的情况直接跳过即可
Time: O(n)
Space: O(1)
Corner cases:
"""
class Solution:
    """
    @param point: a list of two-tuples
    @return: a boolean, denote whether the polygon is convex
    """
    def isConvex(self, points):
        # write your code here
        size = len(points)
        pre, cur = 0, 0
        for i in range(size):
            p1 = points[i] # or p1 = points[i % size]
            p2 = points[(i + 1) % size]
            p3 = points[(i + 2) % size]
            cur = self.getCP(p1, p2, p3)
            # 注意不要忘了cur == 0
            if cur == 0:
                continue
            if cur * pre < 0:
                return False
            pre = cur
        return True
    def getCP(self, p1, p2, p3):
        x1 = p2[0] - p1[0]
        x2 = p3[0] - p1[0]
        y1 = p2[1] - p1[1]
        y2 = p3[1] - p1[1]
        return x1 * y2  - x2 * y1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
