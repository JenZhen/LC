#! /usr/local/bin/python3

# https://lintcode.com/problem/word-search-ii/
# Given a matrix of lower alphabets and a dictionary.
# Find all words in the dictionary that can be found in the matrix.
# A word can start from any position in the matrix and go left/right/up/down to the adjacent position.
# Example
# Given a matrix:
# doaf
# agai
# dcan
# and a dictionary
# {"dog", "dad", "dgdg", "can", "again"}
# return {"dog", "dad", "can", "again"}

"""
Algo: Pure DFS
D.S.: TrieTree + DFS

Solution:
1. TrieTree + DFS
Time Complexity: Worst O(L * (mn) ^ (4k)), where m * n is size of borad, k is length of word, run it L times, meaining L words in dictionary
if there are many shared prefix, more efficient

2. Pure DFS # TODO
O(L * (mn) ^ (4k))

Corner cases:
"""

########################
# TrieTree + DFS Method
# ######################
class TrieNode(object):
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.endWord = None # When need to mark what the whole word is using a string to note end of word, not a boolean

class TrieTree(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        if not word:
            return
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endWord = word
        return

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if not board or not board[0] or not words:
            return []

        trie = TrieTree()
        for word in words:
            trie.addWord(word)
        res = []
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                self.dfs(i, j, trie.root, board, res)
        return res

    def dfs(self, i, j, trieNode, board, res):
        if board[i][j] not in trieNode.children:
            return
        node = trieNode.children[board[i][j]]
        if node.endWord is not None:
            tempSet = set(res)
            if node.endWord not in tempSet:
                res.append(node.endWord)
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        row, col = len(board), len(board[0])
        temp = board[i][j]
        board[i][j] = "#"
        for k in range(4):
            ni, nj = i + dx[k], j + dy[k]
            if ni < 0 or ni >= row or nj < 0 or nj >= col:
                continue
            self.dfs(ni, nj, node, board, res)
        board[i][j] = temp

# Test Cases
if __name__ == "__main__":
    s = Solution()
