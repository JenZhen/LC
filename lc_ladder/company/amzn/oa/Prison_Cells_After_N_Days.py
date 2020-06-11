#! /usr/local/bin/python3

# https://leetcode.com/problems/prison-cells-after-n-days/submissions/
# Example
# There are 8 prison cells in a row, and each cell is either occupied or vacant.
# Each day, whether the cell is occupied or vacant changes according to the following rules:
# If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)
# We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
# Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)
#
# Example 1:
#
# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation:
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
#
# Example 2:
# Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
# Output: [0,0,1,1,1,1,1,0]
#
# Note:
# cells.length == 8
# cells[i] is in {0, 1}
# 1 <= N <= 10^9
"""
Algo:
D.S.:

Solution:
注意：
这个日子的变化是有周期性的
注意到条件N可以非常大，所以要用这个周期来减少复杂度

Corner cases:
"""
class Solution1:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def nextDay(cells):
            res = [0 for _ in range(len(cells))]
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    res[i] = 1
                else:
                    res[i] = 0
            return res

        visited = {}
        while N > 0:
            c = tuple(cells)
            if c in visited:
                N = N % (visited[c] - N)
            visited[c] = N
            if N > 0:
                N -= 1
                cells = nextDay(cells)
        return cells

class Solution2:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        n = len(cells)
        res = [0 for _ in range(n)]
        for _ in range(N):
            for i in range(1, n - 1):
                if cells[i - 1] == cells[i + 1]:
                    res[i] = 1
                else:
                    res[i] = 0
            cells = res
            res = [0 for _ in range(n)]
        return cells



# Test Cases
if __name__ == "__main__":
    solution = Solution()
