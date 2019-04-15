#! /usr/local/bin/python3

# https://www.lintcode.com/problem/paint-house-ii/description
# Example
# 这里有n个房子在一列直线上，现在我们需要给房屋染色，共有k种颜色。每个房屋染不同的颜色费用也不同，你需要设计一种染色方案使得相邻的房屋颜色不同，并且费用最小。
#
# 费用通过一个nxk 的矩阵给出，比如cost[0][0]表示房屋0染颜色0的费用，cost[1][2]表示房屋1染颜色2的费用。
#
# 样例
# costs = [[14,2,11],[11,14,5],[14,3,10]] return 10
#
# 房屋 0 颜色 1, 房屋 1 颜色 2, 房屋 2 颜色 1， 2 + 5 + 3 = 10
#
# 挑战
# 用O(nk)的时间复杂度解决
#
# 注意事项
# 所有费用都是正整数

"""
Algo: Greedy
D.S.:

Solution:
考虑当前房子涂什么颜色时候， 不需要考察上一层所有的
我们希望能从用上一层最小的，但是如果处于相连位置（index）就可以用第二小的，所以只需要记录最小的和第二小的只和位置
Time: O(nk)
Space: O(k) or O(1) modify on costs

Corner cases:
- 当更新当前最小值的时候， 同时要更新第二小的值
- 当只有一列，即只有一种颜色的情况
"""

class Solution_best:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        if not costs: return 0
        n = len(costs)
        if not n: return 0
        k = len(costs[0])
        if not k: return 0
        if k == 1: return min([i[0] for i in costs])

        import sys
        pre_minval, pre_second_minval = 0, 0
        pre_minidx = -1
        for i in range(n):
            cur_minval, cur_second_minval = sys.maxsize, sys.maxsize
            cur_minidx = -1
            for j in range(k):
                if j == pre_minidx:
                    costs[i][j] = costs[i][j] + pre_second_minval
                else:
                    costs[i][j] = costs[i][j] + pre_minval
                if costs[i][j] < cur_minval:
                    cur_second_minval = cur_minval
                    cur_minval = costs[i][j]
                    cur_minidx = j
                elif costs[i][j] < cur_second_minval:
                    cur_second_minval = costs[i][j]
            pre_minval, pre_second_minval = cur_minval, cur_second_minval
            pre_minidx = cur_minidx
        return pre_minval

class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        if not costs: return 0
        n = len(costs)
        if not n: return 0
        k = len(costs[0])
        if not k: return 0
        if k == 1: return min([i[0] for i in costs])


        #minValue = [(minval, minIdx), (second_minval, second_minidx)]
        minValue = self._getMinValue(costs[0])
        for i in range(1, n):
            colors = [0] * k
            for j in range(k):
                if j != minValue[0][1]:
                    colors[j] = costs[i][j] + minValue[0][0]
                else:
                    colors[j] = costs[i][j] + minValue[1][0]
            minValue = self._getMinValue(colors)
        return minValue[0][0]

    def _getMinValue(self, colors):
        import sys
        minValue = [[sys.maxsize, 0], [sys.maxsize, 0]]
        for j in range(len(colors)):
            if colors[j] < minValue[0][0]:
                minValue[1][0] = minValue[0][0]
                minValue[1][1] = minValue[0][1]
                minValue[0][0] = colors[j]
                minValue[0][1] = j
            elif colors[j] < minValue[1][0]:
                minValue[1][0] = colors[j]
                minValue[1][1] = j
        return minValue
# Test Cases
if __name__ == "__main__":
    solution = Solution()
