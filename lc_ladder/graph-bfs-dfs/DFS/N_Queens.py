#! /usr/local/bin/python3

# https://www.lintcode.com/problem/n-queens/description
# n皇后问题是将n个皇后放置在n*n的棋盘上，皇后彼此之间不能相互攻击。
# 给定一个整数n，返回所有不同的n皇后问题的解决方案。
# 每个解决方案包含一个明确的n皇后放置布局，其中“Q”和“.”分别表示一个女王和一个空位置。
#
# 样例
# 对于4皇后问题存在两种解决的方案：
#
# [
#     [".Q..", // Solution 1
#      "...Q",
#      "Q...",
#      "..Q."],
#     ["..Q.", // Solution 2
#      "Q...",
#      "...Q",
#      ".Q.."]
# ]
# 挑战
# 你能否不使用递归完成

"""
Algo: DFS Permutaion Backtracking
D.S.:

Solution:
Permutation 变形
难点： Permute 的条件变得更严格了
1. 不能出现在同一列(类似之前visited的功能)
2. 不能和之前的在同一对角线

Corner cases:
"""

class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        if not n:
            return []
        ans = []
        colPerm = []
        self.dfs(n, colPerm, ans)
        return self.draw(ans)

    def dfs(self, n, colPerm, ans):
        rowCnt = len(colPerm)
        # 递归出口，找到一组解，或是全扫过了没有解
        # 放入ans中
        if n == len(colPerm):
            ans.append(colPerm[:])
            return
        for i in range(n):
            # rowCnt, i refers to row, col to be added,
            # check if it's valid position
            # permutation 的条件，每个题主要差异在这里
            if not self.isValid(colPerm, rowCnt, i):
                continue
            colPerm.append(i)
            self.dfs(n, colPerm, ans)
            colPerm.pop()

    def isValid(self, colPerm, row, col):
        for r, c in enumerate(colPerm):
            # replacement of visited functionality
            if c == col:
                return False
            if r - c == row - col or r + c == row + col:
                return False
        return True

    def draw(self, ans):
        # 注意要考虑没有解的情况
        if not ans:
            return []
        side = len(ans[0])
        solutions = []
        for solution in ans:
            board = []
            for i in range(side):
                row = ['Q' if j == solution[i] else '.' for j in range(side)]
                board.append(''.join(row))
            solutions.append(board)
        return solutions

# Test Cases
if __name__ == "__main__":
    solution = Solution()
