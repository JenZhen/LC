#! /usr/local/bin/python3

# https://www.lintcode.com/problem/longest-palindromic-substring/description
# Example
# 给出一个字符串（假设长度最长为1000），求出它的最长回文子串，你可以假定只有一个满足条件的最长回文串。
#
# 您在真实的面试中是否遇到过这个题？
# 样例
# 样例 1:
#
# 输入:"abcdzdcab"
# 输出:"cdzdc"
# 样例 2:
#
# 输入:"aba"
# 输出:"aba"
# 挑战
# O(n2) 时间复杂度的算法是可以接受的，如果你能用 O(n) 的算法那自然更好。
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

3. Manacher's_algorithm
Time: O(n)
https://leetcode.com/problems/longest-palindromic-substring/solution/
https://en.wikipedia.org/wiki/Longest_palindromic_substring#Manacher's_algorithm
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
