#! /usr/local/bin/python3

# https://leetcode.com/problems/minesweeper/
# Example
# Let's play the minesweeper game (Wikipedia, online game)!
#
# You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.
#
# Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:
#
# If a mine ('M') is revealed, then the game is over - change it to 'X'.
# If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
# Return the board when no more squares will be revealed.

"""
Algo: BFS
D.S.:

Solution:
time complexity: O(n) size of board

Corner cases:
"""

class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        w, h = len(board), len(board[0])
        # O(1) -- Check 8 directions
        def countBoard(i, j):
            cnt = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= w or nj < 0 or nj >= h:
                        continue
                    if board[ni][nj] == 'M':
                        cnt += 1
            return str(cnt) if cnt else 'B'
        # click 是入口，记得查入口的countBoard
        cx, cy = click
        if board[cx][cy] == 'M':
            board[cx][cy] = 'X'
            return board
        q = [click]
        board[cx][cy] = countBoard(cx, cy)
        if board[cx][cy] != 'B':
            return board
        while q:
            ti, tj = q.pop(0)
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    ni, nj = ti + di, tj + dj
                    if ni < 0 or ni >= w or nj < 0 or nj >= h:
                        continue
                    if board[ni][nj] == 'E':
                        board[ni][nj] = countBoard(ni, nj)
                        if board[ni][nj] == 'B':
                            q.append((ni, nj))
        return board


# Test Cases
if __name__ == "__main__":
    solution = Solution()
