#! /usr/local/bin/python3

# https://www.lintcode.com/problem/palindromic-substrings/description
# Example
# 给定一个字符串，你的任务是数出有多少个回文子串在这个字符串内。
# 一个子串不同于其他的子串，当且仅当开始和结束位置不同。
#
# Example
# 样例1
#
# 输入: "abc"
# 输出: 3
# 解释:
# 3个回文字符串: "a", "b", "c".
# 样例2
#
# 输入: "aba"
# 输出: 4
# 解释:
# 4个回文字符串: "a", "b", "a", "aba".
# Notice
# 输入的字符串长度不会超过1,000


"""
Algo:
D.S.:

Solution:


Corner cases:
"""
class Solution1:
    """
    @param str: s string
    @return: return an integer, denote the number of the palindromic substrings
    """
    def countPalindromicSubstrings(self, s):
        # write your code here
        if not s:
            return 0

        n = len(s)
        cnt = 0
        for i in range(n):
            cnt += self.span(s, i, i)
            cnt += self.span(s, i, i + 1)
        return cnt

    def span(self, s, l, r):
        cnt = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            cnt += 1
            l -= 1
            r += 1
        return cnt

class Solution2:
    """
    @param str: s string
    @return: return an integer, denote the number of the palindromic substrings
    """
    def countPalindromicSubstrings(self, s):
        # write your code here
        if not s:
            return 0

        n = len(s)
        f = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            f[i][i] = True

        for j in range(1, n):
            for i in range(j):
                if i + 1 == j:
                    f[i][j] = s[i] == s[j]
                else:
                    f[i][j] = (s[i] == s[j]) and (f[i + 1][j - 1] == 1)

        res = 0
        for i in range(n):
            for j in range(i, n):
                res += 1 if f[i][j] else 0
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
