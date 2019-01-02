#! /usr/local/bin/python3

# https://www.lintcode.com/problem/regular-expression-matching/description?_from=ladder&&fromId=18
# Example
# 实现支持'.'和'*'的正则表达式匹配。
#
# '.'匹配任意一个字母。
#
# '*'匹配零个或者多个前面的元素。
#
# 匹配应该覆盖整个输入字符串，而不仅仅是一部分。
#
# 需要实现的函数是：bool isMatch(string s, string p)
#
# 样例
# isMatch("aa","a") → false
#
# isMatch("aa","aa") → true
#
# isMatch("aaa","aa") → false
#
# isMatch("aa", "a*") → true
#
# isMatch("aa", ".*") → true
#
# isMatch("ab", ".*") → true
#
# isMatch("aab", "c*a*b") → true # note, c* could be no c at all


"""
Algo: DP(string matching type), Recursion
D.S.:

Solution:
1. DP
Time: O(n^2), Space: O(n^2)

p.charAt(j) == s.charAt(i) : dp[i][j] = dp[i-1][j-1]
If p.charAt(j) == ‘.’ : dp[i][j] = dp[i-1][j-1];
If p.charAt(j) == ‘*’:
here are two sub conditions:
if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2] //in this case, a* only counts as empty
if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == ‘.’:
dp[i][j] = dp[i-1][j] //in this case, a* counts as multiple a
dp[i][j] = dp[i][j-1] // in this case, a* counts as single a
dp[i][j] = dp[i][j-2] // in this case, a* counts as empty

2. Recursion


Corner cases:
"""

class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        if s is None or p is None:
            return False

        # s as row, p as col
        dp = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        # init first col, only first is True,
        dp[0][0] = True
        # init first row, only * can match ""
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        # dp
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    if s[i - 1] != p[j - 2] and p[j - 2] != ".":
                        # p 往前挪2位
                        dp[i][j] = dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i][j - 2]
        print(dp)
        return dp[len(s)][len(p)]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
