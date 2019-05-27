#! /usr/local/bin/python3

# https://leetcode.com/problems/distinct-subsequences/
# Example
# Given a string S and a string T, count the number of distinct subsequences of S which equals T.
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Example 1:
#
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
#
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# Example 2:
#
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
#
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^
"""
Algo: DP, 匹配dp
D.S.:

Solution:
DP
行和列都加padding
行是source 的每个字符， 列是target的每个字符
dp[i][j] source 前i个拼成target前j个的方法
1. 如果s[i - 1] == t[j - 1] source和target对应字符相同
dp[i][j] = dp[i - 1][j - 1] + （把这两个字符都不考虑)
           dp[i - 1][j]       （不考虑source当前的这个字符，看上一行和target字符的匹配个数)
2. 如果不一样
dp[i][j] = dp[i - 1][j]  不考虑source当前的这个字符，看上一行和target字符的匹配个数)

return df[lens][lent]  最后一个元素

S = "babgbag", T = "bag"
   "" b a g
""  1 0 0 0
b   1 1 0 0
a   1 1 1 0
b   1 2 1 0
g   1 2 1 1
b   1 3 1 1
a   1 3 4 1
g   1 3 4 5

Time: O(n ^ 2)
Space: O(n ^ 2) --> O(n) rolling
Corner cases:
"""

# create dp (lens + 1) * (lent + 1)

class Solution_dp1:
    def numDistinct(self, s: str, t: str) -> int:
        lens = len(s)
        lent = len(t)
        # create dp (lens + 1) * (lent + 1)
        # source as row, target as col
        dp = [[0 for _ in range(lent + 1)] for _ in range(lens + 1)]
        # dp[i][j] source 前i个拼成target前j个的方法
        # first col is all 1， first row all 0 dp[0][o] = 1
        for i in range(lens + 1):
            dp[i][0] = 1

        for i in range(1, lens + 1):
            for j in range(1, lent + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[lens][lent]


class Solution_dp2:
    def numDistinct(self, s: str, t: str) -> int:
        lens = len(s)
        lent = len(t)
        # create dp (lens + 1) * (lent + 1)
        # source as row, target as col
        # dp = [[0 for _ in range(lent + 1)] for _ in range(lens + 1)]
        dp = [[0 for _ in range(lent + 1)] for _ in range(2)]

        # dp[i][j] source 前i个拼成target前j个的方法
        # first col is all 1， first row all 0 dp[0][o] = 1
        # for i in range(lens + 1):
        #     dp[i][0] = 1
        dp[0][0] = 1
        dp[1][0] = 1
        for i in range(1, lens + 1):
            for j in range(1, lent + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i%2][j] = dp[(i - 1)%2][j - 1] + dp[(i - 1)%2][j]
                else:
                    dp[i%2][j] = dp[(i - 1)%2][j]
        return dp[lens%2][lent]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
