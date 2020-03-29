#! /usr/local/bin/python3

# https://lintcode.com/en/old/problem/word-search/
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# Example
# Given board:
# [
#   "ABCE",
#   "SFCS",
#   "ADEE"
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

"""
Algo: DFS
D.S.:

Solution:
1. Pure DFS
Time Complexity: O((mn) * (4k)), where m * n is size of borad, k is length of word
Another word:
for i in range(m):
    for j in range(n):
        dfs --> worst case O(mn)
Total: O(mn * mn)
# TODO

- worst case: all board elements can be the start of the word
- need to dfs the depth of word, ie k, from 4 directions, ie. 4 * k

Corner cases:
"""

class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        if not board or not word:
            return False

        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if self._find(i, j, 0, board, word):
                        return True
        return False

    def _find(self, i, j, depth, board, word):
        if depth == len(word):
            # The only True condition -- reach to the end of the word(all digit found)
            return True

        row = len(board)
        col = len(board[0])
        if i < 0 or i >= row or j < 0 or j >= col:
            # Out of board boundry
            return False
        if board[i][j] != word[depth]:
            # char on board doesn't match with word
            return False

        # Before goes to next step, mark this [i][j] on board "visited"
        #  -- some char not in [a -z] so that it will bot be revisited
        board[i][j] = "#"
        res = self._find(i + 1, j, depth + 1, board, word) or \
            self._find(i, j + 1, depth + 1, board, word) or \
            self._find(i - 1, j, depth + 1, board, word) or \
            self._find(i, j - 1, depth + 1, board, word)
        # After traced back to this level, reset [i][j] from visited to original value
        board[i][j] = word[depth]
        return res


# Test Cases
if __name__ == "__main__":
    testCases = [
        {
            "board":
                [
                  ["A","B","C","E"],
                  ["S","F","C","S"],
                  ["A","D","E","E"]
                ],
            "words":
                [
                    "ABCCED", #-> returns true,
                    "SEE", #-> returns true,
                    "ABCB" # -> returns false.
                ]
        },
    ]
    s = Solution()
    for t in testCases:
        board = t["board"]
        words = t["words"]
        for w in words:
            res = s.exist(board, w)
            print("res %s" %res)
