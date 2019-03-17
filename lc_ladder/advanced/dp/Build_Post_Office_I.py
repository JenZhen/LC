#! /usr/local/bin/python3

# https://www.lintcode.com/problem/build-post-office/
# Example
# 给出一个二维的网格，每一个格子上用 1 表示房子，0 表示空。要求在网格中，找到一个空地建立邮局，
# 使得邮局到所有的房子的距离和最小。返回所有房子到邮局的最小距离和，如果不可能建邮局则返回-1。
#
# 样例
# 给出一个网格
#
# 0 1 0 0
# 1 0 1 1
# 0 1 0 0
# 返回 6 (把邮局设立在(1,1)这个位置时，邮局离所有的房子的距离是最近的)。
#
# 注意事项
# 你可以穿越房子和空地
# 你只能在空地建立邮局。
"""
Algo: DP
D.S.:

Solution:
TODO：

Time:
Space:

Corner cases:
"""

class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # write your code here
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:
            return -1

        sumx, sumy, x, y = [], [], [], []
        import sys
        result = sys.maxsize
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)

        x.sort()
        y.sort()

        print(x)
        print(y)

        total = len(x)

        sumx.append(0)
        sumy.append(0)
        for i in range(1, total + 1):
            sumx.append(sumx[i - 1] + x[i - 1])
            sumy.append(sumy[i - 1] + y[i - 1])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    cost_x = self.get_cost(x, sumx, i, total)
                    cost_y = self.get_cost(y, sumy, j, total)
                    if cost_x + cost_y < result:
                        result = cost_x + cost_y
        return result

    def get_cost(self, x, sumx, pos, total):
        if total == 0:
            return 0
        if x[0] > pos:
            return sumx[total] - pos * total # sumx size of n + 1

        l, r = 0, total - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if x[mid] <= pos:
                l = mid
            else:
                r = mid - 1
        idx = 0
        if x[r] <= pos:
            idx = r
        else:
            idx = l
        return sumx[total] - sumx[idx + 1] - pos * (total - idx - 1) + (idx + 1) * pos - sumx[idx + 1]



# Test Cases
if __name__ == "__main__":
    solution = Solution()
