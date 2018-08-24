#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo: DP
D.S.:

Solution:
1. dp
Time O(n^2)
Space O(n^2)

2. traverse possible centers
Time O(n^2)
Space O(1)

Corner cases:
"""

# DP
class Solution1:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return ""

        f = [[False for i in range(len(s))] for i in range(len(s))]

        maxlen = 1
        maxs = s[0]
        for step in range(len(s)):
            for i in range(len(s)):
                j = i + step
                if j >= len(s):
                    break
                if j == i:
                    f[i][j] = True
                elif j == i + 1:
                    f[i][j] = s[i] == s[j]
                else:
                    f[i][j] = True if s[i] == s[j] and f[i + 1][j - 1] else False
                if f[i][j] and j - i + 1 > maxlen:
                    maxlen = j - i + 1
                    maxs = s[i:j + 1]
        return maxs


class Solution2:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return ""

        maxS = s[0]
        maxLen = 1

        def getPalindrome(s, st, ed):
            if s[st] != s[ed]:
                return ""
            while st >= 0 and ed <= len(s) - 1 and s[st] == s[ed]:
                st -= 1
                ed += 1
            return s[st + 1 : ed]
        for i in range(len(s) - 1):
            # center at i
            tmpStr = getPalindrome(s, i, i)
            if len(tmpStr) > maxLen:
                maxLen = len(tmpStr)
                maxS = tmpStr
            # center at i, i + 1
            tmpStr = getPalindrome(s, i, i + 1)
            if len(tmpStr) > maxLen:
                maxLen = len(tmpStr)
                maxS = tmpStr
        return maxS
# Test Cases
if __name__ == "__main__":
    solution = Solution()
