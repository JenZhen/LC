#! /usr/local/bin/python3

# https://leetcode.com/problems/find-and-replace-pattern/c
# Example
# You have a list of words and a pattern, and you want to know which words in words matches the pattern.
#
# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
#
# (Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)
#
# Return a list of the words in words that match the given pattern.
#
# You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
# since a and b map to the same letter.
#
#
# Note:
#
# 1 <= words.length <= 50
# 1 <= pattern.length = words[i].length <= 20
"""
Algo:
D.S.:

Solution:
本质是isomorphic 问题

Corner cases:
"""

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            if self.isIsomorphic(word, pattern):
                res.append(word)
        return res

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
