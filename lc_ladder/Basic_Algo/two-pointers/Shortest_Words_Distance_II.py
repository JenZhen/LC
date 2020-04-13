#!/usr/bin/python

# https://leetcode.com/problems/shortest-word-distance-ii/submissions/
# Example
# Design a class which receives a list of words in the constructor, and implements a method that
# takes two words word1 and word2 and return the shortest distance between these two words in the list.
# Your method will be called repeatedly many times with different parameters.
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

Corner cases:
"""

class WordDistance:

    def __init__(self, words: List[str]):
        self.idx_map = {} #key: word, val: [sorted list of idx]
        for i in range(len(words)):
            word = words[i]
            if word not in self.idx_map:
                self.idx_map[word] = []
            self.idx_map[word].append(i)
        print(self.idx_map)
    def shortest(self, word1: str, word2: str) -> int:
        word1_idx = self.idx_map[word1]
        word2_idx = self.idx_map[word2]
        return self._get_min_distance(word1_idx, word2_idx)

    def _get_min_distance(self, l1, l2):
        cur1 = 0
        cur2 = 0
        res = sys.maxsize
        while cur1 < len(l1) and cur2 < len(l2):
            res = min(res, abs(l1[cur1] - l2[cur2]))
            if res == 0:
                return res
            if l1[cur1] > l2[cur2]:
                cur2 += 1
            else:
                cur1 += 1
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
