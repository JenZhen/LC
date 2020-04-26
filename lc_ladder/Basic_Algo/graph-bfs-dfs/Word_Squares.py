#! /usr/local/bin/python3

# https://leetcode.com/problems/word-squares/submissions/
# Example
# Given a set of words (without duplicates), find all word squares you can build from them.
#
# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
#
# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
#
# b a l l
# a r e a
# l e a d
# l a d y
# Note:
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# Example 1:
#
# Input:
# ["area","lead","wall","lady","ball"]
#
# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]
#
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# Example 2:
#
# Input:
# ["abat","baba","atan","atal"]
#
# Output:
# [
#   [ "baba",
#     "abat",
#     "baba",
#     "atan"
#   ],
#   [ "baba",
#     "abat",
#     "baba",
#     "atal"
#   ]
# ]
#
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
"""
Algo:
D.S.:

Solution:


Corner cases:
"""

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {} #key: val, val: TrieNode of var
        self.start_with = [] #list of words start with prefix ending here

class TrieTree:
    def __init__(self):
        self.root = TrieNode("*")

    def add(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur.children[char].start_with.append(word)
            cur = cur.children[char]
        cur.isEnd = True

    def start_with(self, prefix): # 这里使用start_with list 比 is_end有效
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return []
            cur = cur.children[char]
        return cur.start_with


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        res = []
        trie = TrieTree()
        for word in words:
            trie.add(word)

        for word in words:
            path = [word]
            self.dfs(trie, path, res)
        return res

    def dfs(self, trie, path, res):
        if len(path) == len(path[0]):
            # row count == col count
            res.append(path[:])
            return

        prefix = ""
        n = len(path) # if path has 2 words, then look for 3rd one based on idx = len(path)
        for w in path:
            prefix += w[n]

        options = trie.start_with(prefix)
        for opt in options:
            if len(opt) != len(path[0]): # 注意 不要把过长或过短的单词夹加进来
                continue
            path.append(opt)
            self.dfs(trie, path, res)
            path.pop()

# Test Cases
if __name__ == "__main__":
    solution = Solution()
