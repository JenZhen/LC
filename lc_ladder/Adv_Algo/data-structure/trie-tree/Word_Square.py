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

TrieNode设计：
使用start_with list 比 is_end有效
如果使用is_end: 找到prefix之后要 DFS 遍历所有的词
如果是用start_with: 在加入单词的时候就已经准备好了， 所以用空间换时间

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
    s = Solution()
