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
D.S.: UnionFind/BFS/DFS

Solution:
1. UnionFind
Tricky part -- if want certain group points the biggest, need to make sure root points to the largest
Union function needed to be as below
    # 棋盘共mn个点，UF 创建 mn + 1 个点-- 从0到mn
    # 遍历棋盘
        # 如果是边界上的‘O’ 都链接上特殊点 mn
        # 如果是内部的‘O’， 和他四个方向的’O‘ union
    # 最后过一遍棋盘，如果是’O‘而且root 不是特殊点mn, 说明没有联通边界， 变为’X'，否则保持‘O’
2. BSF:
    # BFS
    # 从边界的’o' 开始bfs
    # 把‘O’都变成’#‘， 并且用’#‘ 来记录是否访问过
    # BFS 所有的position， 能和边界联通的标记’#‘
    # 最后再过一遍所有board，之前标记’#‘ 变回’O‘，之前’O‘的是不能联通边界，所以被包围，改为’X'

3. DFS
    # 从边界的'O' 向内部的‘O’遍历
    # 分别从上下左右四个边界开始找’O'，也就是可能的入口
    # 进入DFS，-- 更新值，能到边界变为‘#’， 也用’#‘标记是否访问过
    # 如果越界，或是‘X’ 或是’#’ 访问过就不要在进入dfs 直接return
    # 如果是内部’O‘ 进入他四面元素的dfs

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

class SolutionB_BFS:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    # BFS
    # 从边界的’o' 开始bfs
    # 把‘O’都变成’#‘， 并且用’#‘ 来记录是否访问过
    # BFS 所有的position， 能和边界联通的标记’#‘
    # 最后再过一遍所有board，之前标记’#‘ 变回’O‘，之前’O‘的是不能联通边界，所以被包围，改为’X'

    def surroundedRegions(self, board):
        # write your code here
        if not board or not board[0]:
            return board
        from collections import deque
        q = deque()
        m, n = len(board), len(board[0])
        for i in [0, m - 1]:
            for j in range(n):
                # iterate first and last row
                if board[i][j] == 'O':
                    board[i][j] = '#'
                    q.append((i, j))
        for j in [0, n -  1]:
            for i in range(m):
                # iterate first and last col
                if board[i][j] == 'O':
                    board[i][j] = '#'
                    q.append((i, j))
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while q:
            (curx, cury) = q.popleft()
            for (dx, dy) in dirs:
                newx, newy = curx + dx, cury + dy
                if not (0 <= newx <= m - 1 and 0 <= newy <= n - 1):
                    continue
                if board[newx][newy] == 'O':
                    board[newx][newy] = '#'
                    q.append((newx, newy))

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return board


class Solution_DFS:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # write your code here
        if not board or not board[0]:
            return board
        m, n = len(board), len(board[0])
        for i in range(m):
            if board[i][0] == 'O':
                self.dfs(board, m, n, i, 0)
            if board[i][n - 1] == 'O':
                self.dfs(board, m, n, i, n - 1)
        for j in range(n):
            if board[0][j] == 'O':
                self.dfs(board, m, n, 0, j)
            if board[m - 1][j] == 'O':
                self.dfs(board, m, n, m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return board

    def dfs(self, board, m, n, i, j):
        # if out of boundry return
        if not (0 <= i <= m - 1 and 0 <= j <= n - 1):
            return
        # if 'x' or '#' -- visited not going further dfs
        if board[i][j] == 'X' or board[i][j] == '#':
            return
        board[i][j] = '#'
        self.dfs(board, m, n, i + 1, j)
        self.dfs(board, m, n, i, j + 1)
        self.dfs(board, m, n, i - 1, j)
        self.dfs(board, m, n, i, j - 1)

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
