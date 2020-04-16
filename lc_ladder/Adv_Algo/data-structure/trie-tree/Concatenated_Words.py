#! /usr/local/bin/python3

# https://leetcode.com/problems/concatenated-words/submissions/
# Example
# Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.
#
# Example:
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
#
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
#  "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Note:
# The number of elements of the given array will not exceed 10,000
# The length sum of elements in the given array will not exceed 600,000.
# All the input string will only include lower case letters.
# The returned elements order does not matter.
"""
Algo: DFS
D.S.: Trie

Solution1:
单纯的DFS 暴力算法

Trie? # TODO:
Corner cases:
"""

class Solution_DFS:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dict = set(words)
        res = []
        for word in words:
            if self.dfs(dict, word, 0):
                res.append(word)
        return res

    def dfs(self, dict, word, level):
        # 注意一定要传入level,
        # 最开始的一层 即level = 0， 如果词在字典，不算，
        # 以后更深的层，算true，是递归出口
        if word in dict and level != 0:
            return True
        for i in range(1, len(word)):
            left = word[:i]
            right = word[i:]
            if left in dict and self.dfs(dict, right, level + 1):
                return True
        return False


# Test Cases
if __name__ == "__main__":
    s = Solution()
