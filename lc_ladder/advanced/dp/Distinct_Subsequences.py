#! /usr/local/bin/python3

# https://www.lintcode.com/problem/distinct-subsequences/description
# Example
# 给出字符串S和字符串T，计算S的不同的子序列中T出现的个数。
#
# 子序列字符串是原始字符串通过删除一些(或零个)产生的一个新的字符串，并且对剩下的字符的相对位置没有影响。(比如，“ACE”是“ABCDE”的子序列字符串,而“AEC”不是)。
#
# 样例
# 给出S = "rabbbit", T = "rabbit"
#
# 返回 3
#
# 挑战
# 尝试挑战时间复杂度为O(n2)，空间复杂度为O(n)的算法。
#
# 如果不知道如何优化空间复杂度的话空间复杂度O(n2)也是可接受的。

"""
Algo: Match DP rolling
D.S.:

Solution:
f[i][j]

Corner cases:
"""
class Solution:
    """
    @param S: A string
    @param T: A string
    @return: Count the number of distinct subsequences
    """
    def numDistinct(self, S, T):
        # write your code here
        m, n = len(S), len(T)
        f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # init first col as 1
        for i in range(m + 1):
            f[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if S[i - 1] == T[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j]

        return f[m][n]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
