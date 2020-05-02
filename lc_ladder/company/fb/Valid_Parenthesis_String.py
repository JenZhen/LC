#! /usr/local/bin/python3

# https://leetcode.com/problems/valid-parenthesis-string/solution/
# Example
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
# Example 1:
# Input: "()"
# Output: True
# Example 2:
# Input: "(*)"
# Output: True
# Example 3:
# Input: "(*))"
# Output: True
# Note:
# The string size will be in the range [1, 100].
"""
Algo: 模糊查询括号匹配， DP, Greedy
D.S.:

Solution:

Time: O(N)
Space: O(1)
Corner cases:
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s: return True
        lo = 0  #强制匹配 对应出现的'('
        hi = 0  #可选匹配 对应出现的'(' & '*'
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            if c == ')':
                lo -= 1
                hi -= 1
            if c == '*':
                lo -= 1
                hi += 1
            if hi < 0: return False # 确切出现的)太多了
            lo = max(lo, 0) # lo < 0 可能因为很多* 不清楚
        return lo == 0


# Test Cases
if __name__ == "__main__":
    solution = Solution()
