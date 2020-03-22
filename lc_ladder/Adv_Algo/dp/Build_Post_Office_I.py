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
Solution1: 二分
Solution2: DP?
Time: O(mn) ~ O(mm) ~ O(nn)
Space:

0 1 0 0
1 0 1 1
0 1 0 0

x: (行) 1， 3， 1 （行0 1个，行1 3个，行2 1个）
y:（列) 1, 2, 1, 1 （列0 1个，列1 2个， 列2 1个，列3 1个）

x 轴上
x = 0, 到各个房子的x 距离为 1*(0-0) + 3*(1-0) + 1*(2-0) = 5
x = 1, 到各个房子的x 距离为 1*|0-1| + 3*(1-1) + 1*(2-1) = 2
x = 2, 到各个房子的x 距离为 1*|0-2| + 3*|1-2| + 1*(2-2) = 5
x_sum = [5,2,5]

y轴上
y = 0, 到各个房子y 距离为 1*(0-0) + 2*(1-0) + 1*(2-0) + 1*(3-0) = 7
y = 1, 到各个房子y 距离为 1*|0-1| + 2*(1-1) + 1*(2-1) + 1*(3-1) = 4
y = 2, 到各个房子y 距离为 1*|0-2| + 2*|1-2| + 1*(2-2) + 1*(3-2) = 5
y = 3, 到各个房子y 距离为 1*|0-3| + 2*|1-3| + 1*|2-3| + 1*(3-3) = 8

y_sum = [7,4,5,8]

x = 1, y = 1 satisfying grid[i][j] == 0 and x_sum + y_sum 最小

Corner cases:
"""

class Solution1:
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

class Solution2:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        import sys
        # write your code here
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:
            return -1

        x_cnt = [0] * m
        y_cnt = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x_cnt[i] += 1
                    y_cnt[j] += 1
        x_sum = [0] * m
        y_sum = [0] * n
        for i in range(m):
            sum = 0
            for k in range(m):
                sum += x_cnt[k] * abs(i - k)
            x_sum[i] = sum
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += y_cnt[k] * abs(j - k)
            y_sum[j] = sum
        print('x_sum: %s' %repr(x_sum))
        print('y_sum: %s' %repr(y_sum))

        res = sys.maxsize
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    # if it is an empty Space
                    res = min(res, x_sum[i] + y_sum[j])
        return res

# Test Cases
if __name__ == "__main__":
    testCases = [
        [
            [0, 1, 0, 0],
            [1, 0, 1, 1],
            [0, 1, 0, 0]
        ],#6
        [
            [0, 1, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0]
        ], #8
        [
            [0, 1, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 0]
        ], #12
        [
            [1, 1, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 1, 0]
        ], #12
    ]
    solution1 = Solution1()
    solution2 = Solution2()

    for t in testCases:
        res1 = solution1.shortestDistance(t)
        res2 = solution2.shortestDistance(t)
        print("res1: %s" %res1)
        print("res2: %s" %res2)
