#! /usr/local/bin/python3

# https://www.lintcode.com/problem/minimum-adjustment-cost/description?_from=ladder&&fromId=4
# Example
# 给一个整数数组，调整每个数的大小，使得相邻的两个数的差不大于一个给定的整数target，调整每个数的代价为调整前后的差的绝对值，求调整代价之和最小是多少。
#
# 样例
# 样例 1:
# 	输入:  [1,4,2,3], target=1
#   输出:  2
#
# 样例 2:
# 	输入:  [3,5,4,7], target=2
# 	输出:  1
#
# 注意事项
# 你可以假设数组中每个整数都是正整数，且小于等于100。
"""
Algo: DP 背包
D.S.:

Solution:
f[i][k] 表示第i个数变成k时，前i个数调整的代价和最小值。
枚举第i-1个数调整成的数字j，再枚举第i个数调整成k.做转移。

Corner cases:
"""


class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        import sys
        n = len(A)
        f = [[ sys.maxsize for j in range(101)] for i in range(n + 1)]
        # init first row as all 0
        # f[0][j] modify first 0 item to value j, total adjust cost is f[0][j]
        for j in range(101):
            f[0][j] = 0

        for i in range(1, n + 1):
            for j in range(101):
                for k in range(101):
                    if abs(j - k) <= target:
                        f[i][k] = min(f[i][k], f[i - 1][j] + abs(A[i - 1] - k))
        return min(f[n])


# Test Cases
if __name__ == "__main__":
    solution = Solution()
