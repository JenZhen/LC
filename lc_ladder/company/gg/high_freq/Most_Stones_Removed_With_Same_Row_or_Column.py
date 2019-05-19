#! /usr/local/bin/python3

# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
# Example
# On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.
#
# Now, a move consists of removing a stone that shares a column or row with another stone on the grid.
#
# What is the largest possible number of moves we can make?
#
#
#
# Example 1:
#
# Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# Output: 5
# Example 2:
#
# Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# Output: 3
# Example 3:
#
# Input: stones = [[0,0]]
# Output: 0
#
#
# Note:
#
# 1 <= stones.length <= 1000
# 0 <= stones[i][j] < 10000
"""
Algo: union find
D.S.:

Solution:
思路归纳为：
有相同行或列的点归为一组，一组n个点最多可以remove n-1个
如果有m个组，最多可以remove total_points - m

如何求几个组？ -- number of island
注意这个题join 点的时候不要根据棋盘的横纵坐标扫，只需要扫描所有的点，Join可以归为一组的点的index

Time：O(mn)
Space: O(mn)
Corner cases:
"""

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        if not stones or not len(stones[0]): return 0
        num_stones = len(stones)
        print(num_stones)
        uf = UF(num_stones)
        for i in range(num_stones):
            for j in range(i + 1, num_stones):
                if stones[i][0] == stones[j][0] or \
                    stones[i][1] == stones[j][1]:
                    uf.join(i, j)
        print(uf.cnt)
        return num_stones - uf.cnt

class UF:
    def __init__(self, num):
        self.root = [-1] * num
        self.cnt = num
        for i in range(num):
            self.root[i] = i

    def get_root(self, i):
        if self.root[i] == i:
            return i
        self.root[i] = self.get_root(self.root[i])
        return self.root[i]

    def join(self, i, j):
        i_root = self.get_root(i)
        j_root = self.get_root(j)
        if i_root != j_root:
            self.root[i_root] = j_root
            self.cnt -= 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
