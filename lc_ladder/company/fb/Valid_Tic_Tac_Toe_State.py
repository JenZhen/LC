#! /usr/local/bin/python3

# https://leetcode.com/problems/valid-tic-tac-toe-state/
# Example
# A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.
#
# The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.
#
# Here are the rules of Tic-Tac-Toe:
#
# Players take turns placing characters into empty squares (" ").
# The first player always places "X" characters, while the second player always places "O" characters.
# "X" and "O" characters are always placed into empty squares, never filled ones.
# The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Example 1:
# Input: board = ["O  ", "   ", "   "]
# Output: false
# Explanation: The first player always plays "X".
#
# Example 2:
# Input: board = ["XOX", " X ", "   "]
# Output: false
# Explanation: Players take turns making moves.
#
# Example 3:
# Input: board = ["XXX", "   ", "OOO"]
# Output: false
#
# Example 4:
# Input: board = ["XOX", "O O", "XOX"]
# Output: true
# Note:
#
# board is a length-3 array of strings, where each string board[i] has length 3.
# Each board[i][j] is a character in the set {" ", "X", "O"}.
"""
Algo:
D.S.:

Solution:
考察逻辑

列举 不合法的例子，其余的情况就可以返回TRUE
- x数 应于 O数相同，或大一个， 反之不行
- 如果X 赢， X 数比O数打一个
- 如果O 赢，X 数和O 数相同

Time: O(MN) size of board
Space: O(1)
Corner cases:
"""

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        if not board or not board[0]:
            return False
        # X should be one more than O or equal
        cnt_x, cnt_o = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    cnt_x += 1
                if board[i][j] == 'O':
                    cnt_o += 1
        if not (cnt_x == cnt_o or cnt_x == cnt_o + 1):
            return False

        # there's a win
        # if X wins, must have cnt_o + 1 == cnt_x
        if self.win(board, 'X') and cnt_o + 1 != cnt_x: return False

        # if O wins, must have cnt_o == cnt_x
        if self.win(board, 'O') and cnt_o != cnt_x: return False
        return True

    def win(self, board, char):
        # check row:
        for i in range(3):
            if char == board[i][0] and char == board[i][1] and char == board[i][2]:
                return True
        # check col:
        for j in range(3):
            if char == board[0][j] and char == board[1][j] and char == board[2][j]:
                return True
        # check diagonal
        if char == board[0][0] and char == board[1][1] and char == board[2][2]:
            return True
        if char == board[0][2] and char == board[1][1] and char == board[2][0]:
            return True
        return False

# Test Cases
if __name__ == "__main__":
    solution = Solution()
