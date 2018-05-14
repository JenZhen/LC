#! /usr/local/bin/python3

# https://lintcode.com/en/old/problem/word-squares/
# Given a set of words without duplicates, find all word squares you can build from them.

# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
# Notice
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# Example
# Given a set ["area","lead","wall","lady","ball"]
# return [["wall","area","lead","lady"],["ball","area","lead","lady"]]
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

# Given a set ["abat","baba","atan","atal"]
# return [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

"""
Algo:
D.S.: TireTree + DFS

Solution:
# TODO: Not completed yett

Corner cases:
"""
class TrieNode(object):
    def __init__(self, char=""):
        self.cahr = char # uesless here
        self.children = {}
        self.startWith = []

class TrieTree(object):
    def __init__(self):
        self.root = TrieNode("*")

    def addWord(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.char = char # uselsess here
                cur.children[char] = TrieNode(char)
            cur.children[char].startWith.append(word)
            cur = cur.children[char]

    def getAllStartWith(self, prefix):
        res = []
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return res
            res.extend(cur.startWith)
            cur = cur.children[char]
        res = res.extend(cur.startWith)
        return res

class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        # write your code here
         # write your code here
        if not words:
            return [[]]

        trie = TrieTree()
        for word in words:
            trie.addWord(word)

        res = []
        for word in words:
            builder = []
            builder.append(word)
            self.dfs(trie, res, builder)
            builder.pop() # remove the last element
        return res

    def dfs(self, trie, res, builder):
        if len(builder) == len(builder[0]): # builder is a square already
            res.append(builder)
            return

        idx = len(builder)
        prefix = ""
        for word in builder:
            prefix += word[idx]
        print("prefix: %s" %prefix)
        wordsWithPrefix = trie.getAllStartWith(prefix)
        print("list: %s" %wordsWithPrefix)
        for word in wordsWithPrefix:
            builder.appen(word)
            self.dfs(trie, res, builder)
            builder.pop()

# Test Cases
if __name__ == "__main__":
    s = Solution()
