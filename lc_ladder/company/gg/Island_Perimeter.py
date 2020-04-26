#! /usr/local/bin/python3

# https://www.lintcode.com/problem/island-perimeter/description?_from=ladder&&fromId=18
# Example
# 给定一张用二维数组表示的网格地图，其中1表示陆地单元格，0表示水域单元格。网格地图中的单元格视为水平/垂直相连（斜向不相连）。这个网格地图四周完全被水域包围着，并且其中有且仅有一个岛（定义为一块或多块相连的陆地单元格）。这个岛不包含湖（定义为不和外围水域相连的水域单元格）。一个地图单元格是边长为1的一个正方形；网格地图是一个矩形，并且它的长和宽不超过100。你要做的是求出这个岛的周长。
#
# 样例
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
#
# 答案：16
# 说明：岛的边界为下图中被标为黄色的边，其周长即为16：

"""
Algo: 2D array count
D.S.:

Solution:
Time: O(n * m) aka size of grid

Corner cases:
"""

class Solution:
    """
    @param grid: a 2D array
    @return: the perimeter of the island
    """
    def islandPerimeter(self, grid):
        # Write your code here
        if not grid or not grid[0]:
            return 0
        res = 0
        nRow = len(grid)
        nCol = len(grid[0])
        for i in range(nRow):
            for j in range(nCol):
                # DO NOT FORGET this condition!!
                if grid[i][j] != 1:
                    continue
                # only count up and left based on the order of traverse
                numNei = self.getNumberOfNeighbors(grid, i, j)
                print(i, j, numNei)
                if numNei == 0:
                    res += 4
                if numNei == 1:
                    res += (4 - 2)
                # if numNei == 2:
                #     res += (4 - 4)
        return res

    def getNumberOfNeighbors(self, grid, i, j):
        res = 0
        dirs = [(-1, 0), (0, -1)] # up and left
        for (di, dj) in dirs:
            newi, newj = i + di, j + dj
            if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]):
                if grid[newi][newj] == 1:
                    res += 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
