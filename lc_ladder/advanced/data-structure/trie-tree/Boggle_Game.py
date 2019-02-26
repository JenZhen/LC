#! /usr/local/bin/python3

# https://www.lintcode.com/problem/boggle-game/description?_from=ladder&&fromId=4
# Example
# 给定一个2D矩阵包括 a-z 和字典 dict，找到矩阵上最大的单词集合，这些单词不能在相同的位置重叠。返回最大集合的 大小。
#
# 字典中的单词不重复
# 可以重复使用字典中的单词
# 您在真实的面试中是否遇到过这个题？
# 样例
# 给一个如下的矩阵
#
# [['a', 'b', 'c'],
# ['d', 'e', 'f'],
# ['g', 'h', 'i']]
# dict = ["abc", "cfi", "beh", "defi", "gh"] 返回 3 //
# 我们可以得到最大的集合 ["abc", "defi", "gh"]


"""
Algo:
D.S.: Trie + DFS

Solution:

首先将字典单词插入trie树，然后从(0,0)开始搜索，一个辅助函数getNextWords(i,j)表示从当前位置能获取到的下一个单词，显然可能有多条路径，我们用一个list存下来，然后一个主函数findWords(x,y)表示从(x,y)开始能得到的单词。
大概的流程就是
1.以(x,y)开始搜索，先用getNextWords(x,y)获取到从(x,y)开始能得到的单词，并记录下来路径。
2.枚举获取到的每一个单词word[i]，将word[i]的路径标记一下，更新一下ans,然后继续findWords(next_x,next_y)，回溯的时侯将之前标记的word[i]的路径标记取消掉。
3.最后答案就是ans的最大值。

Corner cases:
"""

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {} #key char, val: TrieNode
        self.isWord = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode("*")

    def addWord(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        cur.isWord = True

    # def isWord(self, word):
    #     cur = self.root
    #     for char in word:
    #         if char not in cur.children:
    #             return False
    #         cur = cur.children[char]
    #     return cur.isWord

class Solution:
    """
    @param: board: a list of lists of character
    @param: words: a list of string
    @return: an integer
    """
    def boggleGame(self, board, words):
        # write your code here
        if not words:
            return 0

        self.trie = TrieTree()
        for w in words:
            self.trie.addWord(w)

        self.row = len(board)
        self.col = len(board[0])
        self.board = board
        self.results = [] #最终最多的结果
        self.temp = [] #动态记录result可能的值，并不断更新self.results
        self.visited = [[False for _ in range(self.col)] for _ in range(self.row)]
        # start from 0, 0
        self.dfs(0, 0, self.trie.root)
        return len(self.results)

    def dfs(self, i, j, node):
        for i in range(i, self.row):
            for j in range(j, self.col):
                paths = []
                temp = []
                self.getPossibleWords(i, j, paths, temp, node)
                for path in paths:
                    word = ''
                    for px, py in path:
                        word += self.board[px][py]
                        self.visited[px][py] = True
                    self.temp.append(word)

                    if len(self.temp) > len(self.results):
                        self.results = self.temp[:]

                    self.dfs(i, j, node)
                    self.temp.pop()
                    for px, py in path:
                        self.visited[px][py] = False
            j = 0

    def getPossibleWords(self, i, j, path, temp, node):
        '''
        start from location (i, j), look for words in dict
        temp: is dynamic coordinate list
        path: is a determined coordinate list
        path you chongdie, danshi meici zhi shiyong yige
        '''
        if i < 0 or i >= self.row or j < 0 or j >= self.col or \
            self.board[i][j] not in node.children or \
            self.visited[i][j] == True:
            return

        node = node.children[self.board[i][j]]
        if node.isWord:
            temp.append((i,j))
            path.append(temp[:])
            temp.pop()
            return

        self.visited[i][j] = True
        deltas = [(0,1), (0,-1), (1,0), (-1, 0)]
        temp.append((i,j))
        for dx, dy in deltas:
            newx = i + dx
            newy = j + dy
            self.getPossibleWords(newx, newy, path, temp, node)
        temp.pop()
        self.visited[i][j] = False
# Test Cases
if __name__ == "__main__":
    s = Solution()
