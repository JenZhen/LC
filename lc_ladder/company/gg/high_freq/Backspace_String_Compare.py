#! /usr/local/bin/python3

# https://leetcode.com/problems/backspace-string-compare/
# Example
# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:
#
# Can you solve it in O(N) time and O(1) space?
"""
Algo:
D.S.:stack

Solution:
1. using stack
Time: O(n)
Space: O(n)

2. TODO
count from back to from and compare
use Space O(1)

Corner cases:
"""

class Solution1:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack = self.populate_stack(S)
        t_stack = self.populate_stack(T)
        if ''.join(s_stack) == ''.join(t_stack):
            return True
        return False

    def populate_stack(self, str):
        res = []
        for s in str:
            if 'a' <= s <= 'z':
                res.append(s)
            if s == '#':
                if len(res) > 0:
                    res.pop()
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
