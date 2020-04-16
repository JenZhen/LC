#!/usr/bin/python

# https://leetcode.com/problems/camelcase-matching/
# Example
# A query word matches a given pattern if we can insert lowercase letters to the pattern word
# so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)
#
# Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.
#
# Example 1:
#
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
# Output: [true,false,true,true,false]
# Explanation:
# "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
# "FootBall" can be generated like this "F" + "oot" + "B" + "all".
# "FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
# Example 2:
#
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
# Output: [true,false,true,false,false]
# Explanation:
# "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
# "FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
# Example 3:
#
# Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
# Output: [false,true,false,false,false]
# Explanation:
# "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
#
# Note:
#
# 1 <= queries.length <= 100
# 1 <= queries[i].length <= 100
# 1 <= pattern.length <= 100
# All strings consists only of lower and upper case English letters.
"""
Algo:
D.S.: Two pointer/Trie

Solution:
1. two pointers
注意Corner cases:
pattern: FoBar
query：
”FoB",
"FoBar",
"FooBar",
"FooBarTest",
"FoatBall",
"FrameBuffer","ForceFeedBack"

2. Trie Tree -- 没有什么特别优势 都是需要每个query和pattern比较
"""

class Solution1:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for query in queries:
            res.append(self._is_match(pattern, query))
        return res

    def _is_match(self, pattern, query):
        i, j = 0, 0
        while i < len(pattern) and j < len(query):
            p, q = pattern[i], query[j]
            if p == q:
                i += 1
                j += 1
            elif q.islower():
                j += 1
            else:
                return False
        return i == len(pattern) and (query[(j + 1):].islower() or query[(j + 1):] == "")

# Test Cases
if __name__ == "__main__":
    solution = Solution()
