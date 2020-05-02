#! /usr/local/bin/python3

# https://leetcode.com/problems/sudoku-solver/
# Example

"""
Algo: DFS Backtracking
D.S.:

Solution:

Time: O(1)
Time complexity is constant here since the board size is fixed and there is no N-parameter to measure.
Though let's discuss the number of operations needed : (9!)^9

Space: O()
Corner cases:
"""

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                for k in range(1, 10):
                    if self.valid(board, i, j, str(k)):
                        board[i][j] = str(k)
                        if self.solve(board):
                            return True
                        board[i][j] = '.'
                return False
        return True

    def valid(self, board, x, y, k):
        for i in range(9):
            # 固定y列，扫描9行
            if board[i][y] == k:
                return False

        for j in range(9):
            # 固定x行，扫描9列
            if board[x][j] == k:
                return False

        for i in range(3):
            for j in range(3):
                a = (x // 3) * 3 + i
                b = (y // 3) * 3 + j
                if board[a][b] == k:
                    return False
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
