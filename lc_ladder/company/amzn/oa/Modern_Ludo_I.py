#! /usr/local/bin/python3

# https://www.lintcode.com/problem/modern-ludo-i/description
# Example
# 有一个一维的棋盘，起点在棋盘的最左侧，终点在棋盘的最右侧，棋盘上有几个位置是跟其他的位置相连的，即如果A与B相连，则当棋子落在位置A时, 你可以选择是否移动棋子从A到B。并且这个连接是单向的，即不能从B移动到A，现在你有一个六面的骰子，最少需要丢几次才能到达终点。
#
# 样例
# input:
# length = 10
# connections = [[2, 10]], 只能从2->10, 不能从2->8
# output:
# 1
# 注意事项
# the index starts from 1.
# length > 1
# The starting point is not connected to any other location
# connections[i][0] < connections[i][1]

"""
Algo: DP
D.S.: arrau

Solution:


Corner cases:
"""

class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modernLudo(self, length, connections):
        # Write your code here
        if not length:
            return 0

        if length <= 7:
            return 1
        # no need to sort on connections
        # connections = sorted(connections, key=lambda x: x[0])
        print("sorted con: %s" %connections)
        map = {}
        for c in connections:
            map[c[0]] = c[1]
        import sys
        dp = [sys.maxsize] * (length + 1)
        for i in range(2, len(dp)):
            dp[i] = min((i - 2) // 6 + 1, dp[i])
            if i > 7:
                # if came from prev steps
                for step in range(1, 7):
                    dp[i] = min(dp[i], dp[i - step] + 1)
            if i in map:
                dp[map[i]] = min(dp[map[i]], dp[i])
        print('dp: %s' %dp)
        return dp[length]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
