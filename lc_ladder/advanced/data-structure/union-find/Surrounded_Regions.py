#! /usr/local/bin/python3

# https://www.lintcode.com/en/old/problem/surrounded-regions/
# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O''s into 'X''s in that surrounded region.
# Example
# X X X X
# X O O X
# X X O X
# X O X X
# After capture all regions surrounded by 'X', the board should be:
# X X X X
# X X X X
# X X X X
# X O X X

"""
Algo:
D.S.: UnionFind/BFS

Solution:
1. UnionFind
Tricky part -- if want certain group points the biggest, need to make sure root points to the largest
Union function needed to be as below

2. BSF # TODO:

Corner cases:
"""
class UnionFind(object):
    def __init__(self, number):
        self.father = [i for i in range(number)]

    def find(self, a):
        if self.father[a] == a:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            # This is important!!
            # To enforce all points to largest number, need to do as below!!
            self.father[min(root_a, root_b)] = max(root_a, root_b)

class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # write your code here
        if not board:
            return None
        row = len(board)
        col = len(board[0])
        total = row * col
        uf = UnionFind(total + 1)
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        # egdge "O" bind with dummy position total (the total-th number)
                        uf.union(i * col + j, total)
                    else:
                        # if internal "O", need to check 4-directions
                        for k in range(4):
                            ni = i + dx[k]
                            nj = j + dy[k]
                            if board[ni][nj] == "O":
                                uf.union(i * col + j, ni * col + nj)
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                if board[i][j] == "O" and uf.find(i * col + j) != total:
                    board[i][j] = "X"
        return board

    def _print(self, board):
        m = len(board)
        n = len(board[0])
        print("[")
        for row in board:
            print("%s" %row)
        print("]")
# Test Cases
if __name__ == "__main__":
    testCases = [
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"]
        ],
    ]
    s = Solution()
    for board in testCases:
        res = s.surroundedRegions(board)
