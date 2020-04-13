#!/usr/bin/python

# https://leetcode.com/problems/shortest-word-distance/
# Example
# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""
Algo: Two pointers
D.S.:

Solution:
Time: O(n) -- one pass
Space: O(1) -- two pointers

Corner cases:
"""
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        p1, p2 = None, None
        cur = 0
        res = len(words)
        while cur < len(words):
            if words[cur] == word1:
                p1 = cur
                if p2 != None:
                    res = min(res, abs(p1 - p2))
            if words[cur] == word2:
                p2 = cur
                if p1 != None:
                    res = min(res, abs(p1 - p2))
            cur += 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
