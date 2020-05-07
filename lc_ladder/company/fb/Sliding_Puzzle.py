#! /usr/local/bin/python3

# https://leetcode.com/problems/sliding-puzzle/submissions/
# Example
# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.
# A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
#
# The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
# Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.
#
# Examples:
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
# Note:
#
# board will be a 2 x 3 array as described above.
# board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
"""
Algo:
D.S.:

Solution:

Time: O((row * col)!) -- all possibility
Space: O((row * col)!)
Corner cases:
"""

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        row, col = len(board), len(board[0])

        x, y = 0, 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == 0:
                    x, y = i, j
                    break

        final_state = ''.join([str(ele) for ele in range(1, row * col)]) + '0'
        start_state = self._get_state(board)
        print('start_state: ', start_state)
        print('final_state: ', final_state)
        visited = set([start_state])
        q = collections.deque([])
        q.append((start_state, 0))

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:
            state, step = q.popleft()
            if state == final_state:
                return step
            pos_0 = state.find('0')
            x, y = pos_0 // col, pos_0 % col
            for dx, dy in dirs:
                nx, ny = dx + x, dy + y
                if 0 <= nx < row and 0 <= ny < col:
                    pos_new = nx * col + ny
                    nstate = state
                    n_list = [c for c in nstate]
                    n_list[pos_0], n_list[pos_new] = n_list[pos_new], n_list[pos_0]
                    nstate = ''.join(n_list)
                    print('nstate: ', nstate)
                    if nstate in visited:
                        continue
                    q.append((nstate, step + 1))
                    visited.add(nstate)
        return -1

    def _get_state(self, board):
        row, col = len(board), len(board[0])
        res = ''
        for row in board:
            res += ''.join(str(ele) for ele in row)
        return res

    def _state_to_board(self, state, row, col):
        res = [[None for _ in range(col)] for _ in range(row)]
        for k in range(len(state)):
            i = k // col
            j = k % col
            res[i][j] = int(state[k])
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
