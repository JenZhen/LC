#! /usr/local/bin/python3

# https://leetcode.com/problems/word-search-ii/
# Example
# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent"
# cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# Example:
#
# Input:
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
#
# Output: ["eat","oath"]
#
#
# Note:
#
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.
"""
Algo: Trie + DFS (Trie 公用prefix 节省时间)
D.S.:

Solution:
详见advanced/data-structure/trie-tree

Corner cases:
"""

########################
# TrieTree + DFS Method
# ######################
class TrieNode:
    def __init__(self, val):
        self.val = val # useless in this contact
        self.children = {} # key "char", val trieNode
        self.endWord = None # init as None, will be a string

class TrieTree:
    def __init__(self):
        self.root = TrieNode("*")

    def add(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        cur.endWord = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board: return []
        if not board[0]: return []
        if not words: return []

        row, col = len(board), len(board[0])
        trie = TrieTree()
        for word in words:
            trie.add(word)

        res = []
        for i in range(row):
            for j in range(col):
                self.dfs(board, i, j, trie.root, res)
        return res


    def dfs(self, board, i, j, node, res):
        row, col = len(board), len(board[0])
        # 先检查是否越界
        if not (0 <= i < row and 0 <= j < col):
            return
        # 再检查值是否相等 是否可以继续
        if board[i][j] not in node.children:
            return

        node = node.children[board[i][j]]
        # 如果找到一个词，（这个词肯定是dictionary里的）看看是不是在结果里
        if node.endWord is not None:
            tmpSet = set(res) # 转换成SET更快计算
            if node.endWord not in tmpSet:
                res.append(node.endWord)

        # 进行下一轮， 不用考虑边界，在每层DFS 最开始考虑边界问题
        tmp = board[i][j]
        board[i][j] = '#' # 标记格子位置访问过
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = i + dx, j + dy
            self.dfs(board, nx, ny, node, res)
        board[i][j] = tmp
        return

# Test Cases
if __name__ == "__main__":
    solution = Solution()
