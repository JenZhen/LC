#! /usr/local/bin/python3

# https://www.jiuzhang.com/solution/zombie-in-matrix#tag-highlight-lang-python
# Example
# 给一个二维网格，每一个格子都有一个值，2 代表墙，1 代表僵尸，0 代表人类(数字 0, 1, 2)。
# 僵尸每天可以将上下左右最接近的人类感染成僵尸，但不能穿墙。将所有人类感染为僵尸需要多久，如果不能感染所有人则返回 -1。
#
# 在线评测地址: http://www.lintcode.com/problem/zombie-in-matrix/
"""
Algo: Level-BFS
D.S.:

Solution:
数层遍历
Time: O(mn) -- nearly all grid element visited twice
Space: O(mn) -- for queue to hold all elements

Corner cases:

"""

class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer
    def zombie(self, grid):
        # Write your code here
        # row
        n = len(grid)
        if n == 0:
            return 0
        # col
        m = len(grid[0])
        if m == 0:
            return 0

        q = []
        for i in range(n):
            for j in range(m):
                # enqueue all zombies as potential starting points
                if grid[i][j] == 1:
                    q.append((i, j))

        d = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        # init days as 0
        days = 0
        while q:
            # each level += 1 (root/first zombie's day is 1 in this case)
            days += 1
            # newly added zombies to new queue
            new_q = []
            for node in q:
                for k in range(4):
                    x = node[0] + d[k][0]
                    y = node[1] + d[k][1]
                    # only enqueu in-boundry human
                    if x >= 0 and x < n and y >= 0 and y < m and grid[x][y] == 0:
                        # convert human to zombie
                        grid[x][y] = 1
                        new_q.append((x, y))
            q = new_q
        # last review if any human left or not
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    return -1
        # since the first zombie is count as 1 day, need remove it, start counting from level2
        return days - 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
