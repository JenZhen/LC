#! /usr/local/bin/python3

# https://www.lintcode.com/problem/one-edit-distance/description
# Example

"""
Algo: DP, array manipulation
D.S.:

Solution:
DP will exceed time limit.

1. swap if necessary to make s shorter than t
"ABC" VS "AbC"
"AB"  VS "AbB"
"AB"  VS "ABC"
"AB"  VS "AB"
Corner cases:
"""

class Solution1:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        m, n = len(s), len(t)
        if abs(m - n) > 1:
            return False

        if m > n:
            # this is a smart way
            return self.isOneEditDistance(t, s)

        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]
        # REMEMBER to finally check this to avoid "AB" VS "AB"
        return m != n

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
        return f[m][n] ==
# Test Cases
if __name__ == "__main__":
    solution = Solution()
