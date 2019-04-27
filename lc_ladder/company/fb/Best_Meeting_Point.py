#! /usr/local/bin/python3

# https://www.lintcode.com/problem/best-meeting-point/description
# Example
# 有一群住在不同地方的朋友（两个或以上）想要在某地见面，要求他们去往目的地的路程和最短。
# 现在给一个0、1组成的二维数组，1表示此地有一个人居住。使用曼哈顿距离作为计算总距离，公式为：(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|
#
# 样例
# 样例 1:
#
# 输入:
# [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# 输出:
# 6
#
# 解释:
# 点(0, 2)是最佳见面地点，最小的路程总和为2+2+2=6，返回6。
# 样例 2:
#
# 输入:
# [[1,1,0,0,1],[1,0,1,0,0],[0,0,1,0,1]]
# 输出:
# 14

"""
Algo: 2D array
D.S.:

Solution:
注意： 这个题求的是总距离，不是那个最优的地点
这个题不考虑中间有障碍物

曼哈顿距离，行列的最佳点分开求，组合起来就是最佳点。
二维->一维。求中位数。

细节：拿到坐标的list后一定要记得排序

Corner cases:
"""
class Solution:
    """
    @param grid: a 2D grid
    @return: the minimize travel distance
    """
    def minTotalDistance(self, grid):
        # Write your code here

        m = len(grid)
        n = len(grid[0])
        x_list = []
        y_list = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x_list.append(i)
                    y_list.append(j)
        return self.getAvgDist(x_list) + self.getAvgDist(y_list)

    def getAvgDist(self, cor_list):
        cor_list.sort()
        res = 0
        l, r = 0, len(cor_list) - 1
        while l < r:
            res += (cor_list[r] - cor_list[l])
            l += 1
            r -= 1
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
