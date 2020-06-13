#! /usr/local/bin/python3

# https://leetcode.com/problems/longest-string-chain/
# Example
# Given a list of words, each word consists of English lowercase letters.
# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.
# For example, "abc" is a predecessor of "abac".
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1,
# where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.
#
# Return the longest possible length of a word chain with words chosen from the given list of words.
#
# Example 1:
# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
#
# Note:
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.

"""
Algo: map
D.S.:

Solution:
Time: O(n * len(word))
Space: O(n)

Corner cases:
"""

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        if not words: return 0
        words.sort(key=lambda x: len(x))
        res = 1 # init as 1 not 0
        mp = {} #key: word, val: order
        for w in words:
            mp[w] = 1
        for w in words:
            preds = self.get_pred(w)
            for p in preds:
                if p in mp:
                    mp[w] = max(mp[w], mp[p] + 1)
                    res = max(res, mp[w])
        return res

    def get_pred(self, w):
        res = []
        for i in range(len(w)):
            res.append(w[0:i] + w[i+1::])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
