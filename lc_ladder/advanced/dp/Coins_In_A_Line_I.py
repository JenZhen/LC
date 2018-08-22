#! /usr/local/bin/python3

# https://www.lintcode.com/problem/coins-in-a-line/description
# Example
# There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more coins left. The player who take the last coin wins.
#
# Could you please decide the first play will win or lose?
#
# Example
# n = 1, return true.
#
# n = 2, return true.
#
# n = 3, return false.
#
# n = 4, return true.
#
# n = 5, return true.
#
# Challenge
# O(n) time and O(1) memory

"""
Algo: DP 滚动数组
D.S.:

Solution1 & 2 （针对当前选手）:
1. Time O(n) Space O(n)
2. Time O(n) Space O(1)

Solution3: 针对先手一个player来分析状态
1. 状态
f[i]: 先手A，面对有i个剩余硬币时的输赢状态
2. 方程
f[i] = (f[i - 2] && f[i - 3])||(f[i - 3] && f[i - 4])
3. 初始化
f[0] = F
f[1] = T
f[2] = T
f[3] = F
4. 答案
f[n]

Corner cases:
"""

class Solution1:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if not n:
            return False

        if n == 1:
            return True
        if n == 2:
            return True

        f = [False for i in range(n + 1)]
        f[0] = False
        f[1] = True
        f[2] = True
        for i in range(3, n + 1):
            f[i] = (not f[i - 1]) or (not f[i - 2])
        return f[n]

class Solution2:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        if not n:
            return False

        if n == 1:
            return True
        if n == 2:
            return True

        f = [False for i in range(n + 1)]
        f[0] = False
        f[1] = True
        f[2] = True
        for i in range(3, n + 1):
            f[i % 3] = (not f[(i - 1) % 3]) or (not f[(i - 2) % 3])
        return f[n % 3]
# Test Cases
if __name__ == "__main__":
    solution = Solution()
