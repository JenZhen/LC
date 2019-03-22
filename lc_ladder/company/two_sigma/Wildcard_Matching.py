#! /usr/local/bin/python3

# https://www.lintcode.com/problem/wildcard-matching/description
# Example
# 判断两个可能包含通配符“？”和“*”的字符串是否匹配。匹配规则如下：
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个串完全匹配才算匹配成功。
#
#
# 函数接口如下:
#
# bool isMatch(const char *s, const char *p)
#
# 样例
# 一些例子：
#
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false

"""
Algo: DP with rolling, DFS (# TODO: )
D.S.:

Solution:
注意：
1. *可以是包含空串在内的任意字符串，不一定是某个串的N次重复
2. ？只能表示一个字符，且不是一个空字符

Corner cases:
"""

class SolutionDP:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        if not s and not p:
            return True

        m, n = len(p), len(s)
        f = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][0] = True
        # init first row
        # for j in range(1, n + 1):
        #     f[0][j] = False
        # init first col
        for i in range(1, m + 1):
            if p[i - 1] == "*":
                f[i][0] = f[i - 1][0]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[i - 1] == "*":
                    f[i][j] = f[i - 1][j] or f[i][j - 1] or f[i - 1][j - 1]
                elif p[i - 1] == "?":
                    f[i][j] =  f[i - 1][j - 1]
                else:
                    if p[i - 1] == s[j - 1]:
                        f[i][j] = f[i - 1][j - 1]
        print(f)
        return f[m][n]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
