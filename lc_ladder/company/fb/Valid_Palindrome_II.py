#! /usr/local/bin/python3

# https://www.lintcode.com/problem/valid-palindrome-ii/description
# Example
# 给一个非空字符串 s，你最多可以删除一个字符。判断是否可以把它变成回文串。
#
# Example
# 样例 1:
#
# 输入: s = "aba"
# 输出: true
# 解释: 原本就是回文串
# 样例 2:
#
# 输入: s = "abca"
# 输出: true
# 解释: 删除 'b' 或 'c'
# 样例 3:
#
# 输入: s = "abc"
# 输出: false
# 解释: 删除任何一个字符都不能使之变成回文串
# Notice
# 给定的字符串只包含小写字母
# 字符串的长度最大为 50000

"""
Algo: two-pointers
D.S.: array

Solution:
Time: O(n)

Corner cases:
"""


class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code here
        if not s or len(s) <= 2:
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                break
        return self._is_palindrome(s[l : r]) or self._is_palindrome(s[l + 1: r + 1])

    def _is_palindrome(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        
# Test Cases
if __name__ == "__main__":
    solution = Solution()
