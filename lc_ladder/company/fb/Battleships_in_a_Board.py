#! /usr/local/bin/python3

# https://leetcode.com/problems/battleships-in-a-board/submissions/
# Example
# Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
# Example:
# X..X
# ...X
# ...X
# In the above board there are 2 battleships.
# Invalid Example:
# ...X
# XXXX
# ...X
# This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
# Follow up:
# Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?
"""
Algo:
D.S.:

Solution:
根据特定条件比较巧的一个题
”只能横着或竖着放”， “没有两个船挨着”
从左到右
从上到下
没找到一个x 如果它上面或下面有X 说明已经算过了
Time: O(mn)
Space: O(1)
Corner cases:
"""

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        row, col = len(board), len(board[0])
        cnt = 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    cnt += 1
                    # check up and left if 'X', if yes, just add a previous counted boat
                    if (i - 1 >= 0 and board[i - 1][j] == 'X') or \
                        (j - 1 >= 0 and board[i][j - 1] == 'X'):
                        cnt -= 1
        return cnt
# Test Cases
if __name__ == "__main__":
    solution = Solution()
