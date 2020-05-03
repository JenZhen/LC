#! /usr/local/bin/python3

# https://www.lintcode.com/problem/one-edit-distance/description
# Example
# Given two strings s and t, determine if they are both one edit distance apart.
#
# Note:
#
# There are 3 possiblities to satisify one edit distance apart:
#
# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t
# Example 1:
#
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.
# Example 2:
#
# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.
# Example 3:
#
# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.
"""
Algo: DP, array manipulation
D.S.:

Solution1:
Time: O(N)
Space: O(1)

Solution2_DP:
DP will exceed time limit.

1. swap if necessary to make s shorter than t
"ABC" VS "AbC"
"AB"  VS "AbB"
"AB"  VS "ABC"
"AB"  VS "AB"
Corner cases:
"""

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m > n:
            return self.isOneEditDistance(t, s)
        # make sure t比s长 or 一样长
        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    # replace
                    return s[i+1:] == t[i+1:]
                else:
                    # 减去这个不一样的
                    return s[i:] == t[i+1:]
        #最后要检查 长度 考虑 一下情形：‘ab' vs 'abc'
        return m + 1 == n

class SolutionDP:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        m, n = len(s), len(t)
        f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for j in range(n + 1):
            f[0][j] = j
        for i in range(m + 1):
            f[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
        return f[m][n] == 1
# Test Cases
if __name__ == "__main__":
    solution = Solution()
