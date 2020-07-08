#! /usr/local/bin/python3

# https://leetcode.com/problems/candy-crush/
# Example
# This question is about implementing a basic elimination algorithm for Candy Crush.
#
# Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies.
# A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move.
# Now, you need to restore the board to a stable state by crushing candies according to the following rules:
#
# If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
# After crushing all candies simultaneously, if an empty space on the board has candies on top of itself,
# then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
#
# After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
# If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
# You need to perform the above rules until the board becomes stable, then return the current board.
#
# Example:
# Input:
# board =
# [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
#
# Output:
# [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
#
# Explanation:
#
# Note:
# The length of board will be in the range [3, 50].
# The length of board[i] will be in the range [3, 50].
# Each board[i][j] will initially start as an integer in the range [1, 2000].
"""
Algo: Simulate
D.S.:

Solution:
Time: O(mn * mn * how many loop)
Space: O(1)

Corner cases:
注意L 形状，要被flipped的地方都要标记成负数
XXX
00X
00
"""

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])

        while True:
            can_crush = False
            for i in range(m):
                for j in range(n):
                    val = abs(board[i][j])
                    if val == 0:
                        continue # empty
                    # 因为是从左至右，从上至下遍历，所以不用考虑从i,j 向左向下
                    # from i, j search to right, 会有重复计算
                    # 如果从i，j开始向右能有连续3个，那么while loop 去找最多向右能找几个，全部flip
                    if j < n - 2 and abs(board[i][j + 1]) == val and abs(board[i][j + 2]) == val:
                        can_crush = True
                        idx = j # from j to right can crush
                        while idx < n and abs(board[i][idx]) == val:
                            board[i][idx] = -val # update right side val to negative
                            idx += 1 # see how far right idx can go

                    # from i, j search to down, 会有重复计算
                    # 如果从i，j开始向下能有连续3个，那么while loop 去找最多向下能找几个，全部flip
                    if i < m - 2 and abs(board[i + 1][j]) == val and abs(board[i + 2][j]) == val:
                        can_crush = True
                        idx = i
                        while idx < m and abs(board[idx][j]) == val:
                            board[idx][j] = -val
                            idx += 1

            if not can_crush:
                # reach to stable state
                return board

            if can_crush:
                # fall pieces per col from down to top
                for j in range(n):
                    idx = m - 1 # where next non-crushed piece go
                    for i in range(m - 1, -1, -1):
                        if board[i][j] > 0:
                            board[idx][j] = board[i][j]
                            idx -= 1

                    # all above idx should be flipped from negative to 0
                    # 这里不要忘记
                    for k in range(idx, -1, -1):
                        board[k][j] = 0

# Test Cases
if __name__ == "__main__":
    solution = Solution()
