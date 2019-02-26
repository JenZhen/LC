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

# 给出一系列 不重复的单词，找出所有用这些单词能构成的 单词矩阵。
# 一个有效的单词矩阵是指, 如果从第 k 行读出来的单词和第 k 列读出来的单词相同(0 <= k < max(numRows, numColumns))，那么就是一个单词矩阵.
# 例如，单词序列为 ["ball","area","lead","lady"] ,构成一个单词矩阵。因为对于每一行和每一列，读出来的单词都是相同的。
#
# b a l l
# a r e a
# l e a d
# l a d y
# 现在至少有一个单词并且不多于1000个单词
# 所有的单词都有相同的长度
# 单词的长度最短为 1 最长为 5
# 每一个单词均由小写字母组成
#
# 样例
# 给出单词序列 ["area","lead","wall","lady","ball"]
# 返回 [["wall","area","lead","lady"],["ball","area","lead","lady"]]
# 输出包含 两个单词矩阵，这两个矩阵的输出的顺序没有影响(只要求矩阵内部有序)。
#
# 给出单词序列 ["abat","baba","atan","atal"]
# 返回 [["baba","abat","baba","atan"],["baba","abat","baba","atal"]]
# 输出包含 两个单词矩阵，这两个矩阵的输出的顺序没有影响(只要求矩阵内部有序)。

"""
Algo:
D.S.: TireTree + DFS

Solution:
Time Complexity:

题中说明是无重复单词，所以不用查重

Corner cases:
"""
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {} # key: "char", val: TrieNode
        self.startWith = []

class TrieTree:
    def __init__(self):
        self.root = TrieNode("*")

    def addWord(self, word):
        cur = self.root
        for w in word:
            if not w in cur.children:
                cur.children[w] = TrieNode(w)
            cur.children[w].startWith.append(word)
            cur = cur.children[w]

    def getStartWith(self, prefix):
        cur = self.root
        res = []
        for w in prefix:
            if w not in cur.children:
                return res
            cur = cur.children[w]
        res.extend(cur.startWith)
        return res

class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        # write your code here
        if not words:
            return []

        trie = TrieTree()
        for word in words:
            trie.addWord(word)

        res = []
        for word in words:
            build = [word]
            self.dfs(res, build, trie)
            build.pop()
        return res

    def dfs(self, res, build, trie):
        if len(build) == len(build[0]):
            res.append(build[:])
            return
        prefix = ""
        for word in build:
            prefix += word[len(build)]
        # print("prefix: " + prefix)
        options = trie.getStartWith(prefix)
        # print("options: %s" %repr(options))
        for opt in options:
            build.append(opt)
            self.dfs(res, build, trie)
            build.pop()

# Test Cases
if __name__ == "__main__":
    s = Solution()
