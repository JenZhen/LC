#!/usr/bin/python

# https://leetcode.com/problems/valid-palindrome-ii/description/
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

"""
Algo: Two pointers
D.S.:

Solution:
- find the break point for origina array
- try remove either of the un-even points of the sub array
- if any of the subarray is palindrome, return True, if both not palindrome, return false

Corner cases:
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                break
        if l >= s:
            return True
        subStr = s[l: r + 1]
        if self.isPalin(subStr[1:]) or self.isPalin(subStr[0:len(subStr) - 1]):
            return True
        else:
            return False

    def isPalin(self, s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
