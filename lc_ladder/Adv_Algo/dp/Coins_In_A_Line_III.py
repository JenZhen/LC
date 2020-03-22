#! /usr/local/bin/python3

# https://lintcode.com/problem/coins-in-a-line-iii/description
# Example
# # There are n coins in a line. Two players take turns to take a coin from one of the ends of the line until there are no more coins left. The player with the larger amount of money wins.

# Could you please decide the first player will win or lose?

# Example
# Given array A = [3,2,2], return true.

# Given array A = [1,2,4], return true.

# Given array A = [1,20,4], return false.

# Challenge
# Follow Up Question:

# If n is even. Is there any hacky algorithm that can decide whether first player will win or lose in O(1) memory and O(n) time?

"""
Algo: 博弈类，记忆搜索，区间DP 从大区间想小区间搜
D.S.:

Solution:
Time: O(n^2), Space: O(n^2)

Solution1: 针对先手一个player来分析状态 -- 先手
                [0,2]
A(first-hand)  （3，2，4）
        take 3 /        \ take 4
              /          \
B         （2，4）      （3, 2)
    take 2 / \take 4   3 /  \ take 2
          /   \         /    \
A       4      2       2      3
    [2,2]     [1,1]   [1,1]   [0,0]

大区间指[0, n - 1]
缩小的区间是[1, n - 1] & [0, n - 2]
...
直至初始化区间 f[i][i], f[i][i+1]

1. 状态
f[i][j]: 先手A，面对区间[i, j]时的输赢状态
2. 方程
f[i] = max(
        # 取左边，i - 2 是先后手都从左边取，右端点j不变，i + 1 是先手取左，后手去右，最后加上values[i] 先手第一次从左边去的值
        min(f(i - 2, j), f(i + 1, j - 1)) + values[i]
        # 取左边，j - 2 是先后手都从右边取，左端点i不变，i + 1 是先手取右，后手去左，最后加上values[j] 先手第一次从右边去的值
        min(f(i， j - 2), f(i + 1, j - 1)) + values[j]
    )

3. 初始化
因为有i-2，j-2，所以要i从2开始循环，初始化i,j 为0，1时候
f[i][j] = values[i]
f[i][i+1] = max(values[i], values[i + 1]）
4. 答案
return f[0][n - 1] > sum(value) / 2

Corner cases:
"""

class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # write your code here
        if not values:
            return False
        n = len(values)
        f = [[None for _ in range(n)] for _ in range(n)]

        return sum(values) < 2 * self.search(0, n - 1, f, values)

    def search(self, i, j, f, values):
        if f[i][j] is not None:
            return f[i][j]
        if i == j:
            f[i][j] = values[i]
        elif i + 1 == j:
            f[i][j] = max(values[i], values[j])
        else:
            pick_left = min(self.search(i + 2, j, f, values), self.search(i + 1, j - 1, f, values)) + values[i]
            pick_right = min(self.search(i, j - 2, f, values), self.search(i + 1, j - 1, f, values)) + values[j]
            f[i][j] = max(pick_right, pick_left)
        return f[i][j]
# Test Cases
if __name__ == "__main__":
    solution = Solution()
