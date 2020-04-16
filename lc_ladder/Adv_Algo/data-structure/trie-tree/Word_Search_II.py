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
在有很都单词 share prefix 的时候会很有效
t
2. Pure DFS # TODO
O(L * (mn) ^ (4k))

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
    s = Solution()
