#! /usr/local/bin/python3

# https://leetcode.com/problems/isomorphic-strings/
# Example
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# Example 1:
#
# Input: s = "egg", t = "add"
# Output: true
# Example 2:
#
# Input: s = "foo", t = "bar"
# Output: false
# Example 3:
#
# Input: s = "paper", t = "title"
# Output: true
# Note:
You may assume both s and t have the same length.

"""
Algo:
D.S.:

Solution:
注意：一对一关系需要2个map 来实现

Corner cases:
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t = {}
        t_to_s = {}
        for i in range(len(s)):
            src, tgt = s[i], t[i]
            if src not in s_to_t and tgt not in t_to_s:
                s_to_t[src] = tgt
                t_to_s[tgt] = src
            elif src in s_to_t and tgt in t_to_s:
                if s_to_t[src] != tgt or t_to_s[tgt] != src:
                    return False
            else:
                return False
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
