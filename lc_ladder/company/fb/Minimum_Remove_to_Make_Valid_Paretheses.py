#! /usr/local/bin/python3

# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/submissions/
# Example
# Given a string s of '(' , ')' and lowercase English characters.
#
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
#
# Formally, a parentheses string is valid if and only if:
#
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
#
#
# Example 1:
#
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:
#
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:
#
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
# Example 4:
#
# Input: s = "(a(b(c)d)"
# Output: "a(b(c)d)"
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# s[i] is one of  '(' , ')' and lowercase English letters.
"""
Algo:
D.S.:

Solution:
不合法的重要条件是右括号比左边的多，
左右各来一遍 把不合法的放在一个set中，
再重新组合字符串

Time: O(N)
Space: O(N)
Corner cases:
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s: return s
        arr = [None] * len(s)
        remove_idx_list = set()

        # from left to right
        bal = 0
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                if bal < 0:
                    bal = 1
                else:
                    bal += 1
            if c == ')':
                bal -= 1
                if bal < 0:
                    remove_idx_list.add(i)
        # from right to left
        bal = 0
        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == ')':
                if bal < 0:
                    bal = 1
                else:
                    bal += 1
            if c == '(':
                bal -= 1
                if bal < 0:
                    remove_idx_list.add(i)

        res = ''
        for i in range(len(s)):
            if i in remove_idx_list:
                continue
            else:
                res += s[i]
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
