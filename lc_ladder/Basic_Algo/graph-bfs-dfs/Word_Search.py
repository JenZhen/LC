#! /usr/local/bin/python3

# https://leetcode.com/problems/word-search/
# Example
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

"""
Algo: DFS, Backtracking
D.S.:

Solution:
Time: O(mn * 4 ^ L) L is length of word
Space: O(mn)


Corner cases:
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word: return False
        if not board: return False
        if not board[0]: return False

        row, col = len(board), len(board[0])
        # Visited Matrix
        visited = [[False for j in range(col)] for i in range(row)]

        # DFS
        for i in range(row):
            for j in range(col):
                if self.dfs(board, word, visited, i, j, 0):
                    return True
        return False

    def dfs(self, board, word, visited, i, j, idx):
        if idx == len(word): return True

        row, col = len(board), len(board[0])

        if i < 0 or i >= row or j < 0 or j >= col:
            return False

        if board[i][j] != word[idx]: return False
        if visited[i][j]: return False

        visited[i][j] = True

        # search next 4 directions
        found = False
        found = self.dfs(board, word, visited, i - 1, j, idx + 1) or \
                self.dfs(board, word, visited, i, j - 1, idx + 1) or \
                self.dfs(board, word, visited, i + 1, j, idx + 1) or \
                self.dfs(board, word, visited, i, j + 1, idx + 1)
        # 注意结尾
        # 如果找到 直接返回True 不要把visited[i][j] 标记为 False
        if found:
            return True
        else:
            # 只有在找不到时候才能标记为FALSE ``
            visited[i][j] = False

        return False

# Test Cases
if __name__ == "__main__":
    solution = Solution()


class Solution_FAILED_TLE:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word: return False
        if not board: return False
        if not board[0]: return False

        row, col = len(board), len(board[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if self.dfs(board, word, visited, 0, i, j):
                    return True
        return False

    def dfs(self, board, word, visited, d, i, j):
        row, col = len(board), len(board[0])

        # if out of boundry -> False
        if i < 0 or i >= row or j < 0 or j >= col:
            return False

        # if value doesn't match -> False
        if board[i][j] != word[d]:
            return False

        # if visited:
        if visited[i][j]: return False

        if d == len(word) - 1:
            return True

        found = False
        visited[i][j] = True
        found = self.dfs(board, word, visited, d + 1, i, j + 1) or \
                self.dfs(board, word, visited, d + 1, i + 1, j) or \
                self.dfs(board, word, visited, d + 1, i, j - 1) or \
                self.dfs(board, word, visited, d + 1, i - 1, j)
        if found:
            return True
        else:
            visited[i][j] = False
        return False
