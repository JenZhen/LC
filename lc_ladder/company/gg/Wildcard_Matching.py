#! /usr/local/bin/python3

# https://leetcode.com/problems/wildcard-matching/solution/
# Example
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:
#
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:
#
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:
#
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
"""
Algo: Matching DP
D.S.:

Solution:
Time: O(mn)
Space: O(mn) --> O(m)

Corner cases:
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s is None or p is None:
            return False

        n, m = len(s), len(p)

        # state
        # p as row, s as col
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # initialization
        # first col should be init, first row -- all false except for 0, 0
        dp[0][0] = True
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and p[i - 1] == '*'

        # function
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[i - 1] == '*':
                    # dp[i][j - 1] 从左边来，* 代替了1或多个字符
                    # dp[i - 1][j] 从上边来，* 代表0个字符
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (p[i - 1] == s[j - 1] or p[i - 1] == '?')

        return dp[-1][-1]
# Test Cases
if __name__ == "__main__":
    solution = Solution()
