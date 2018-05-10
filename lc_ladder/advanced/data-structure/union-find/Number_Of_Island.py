#! /usr/local/bin/python3

# https://www.lintcode.com/en/old/problem/number-of-islands/
# Given a boolean 2D matrix, 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent,
# we consider them in the same island. We only consider up/down/left/right adjacent.
# Find the number of islands.

"""
Algo: Graph, Search, BFS, Union-Find
D.S.: Union-Find

Solution:
1. UnionFind

2. BFS: O(m*n)
Space O(m*n)

3. DFS: # TODO: 

Corner cases:
"""

#############
# Union-find
#############

class UnionFind(object):
    def __init__(self, n):
        # init a group of isolated nodes
        self.count = n
        self.father = [0] * n # father mapping n empty slot
        for i in range(n):
            self.father[i] = i

    def find(self, node):
        if self.father[node] == node:
            return node
        self.father[node] = self.find(self.father[node])
        return self.father[node]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.count -= 1

    def setCount(self, count):
        self.count = count

    def getCount(self):
        return self.count

    def diagFatherRelation(self):
        print("[")
        for i in range(len(self.father)):
            print("{Father: %s, Son: %s}" %(self.father[i], i))
        print("]")

class Solution1:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        # BFS

        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        numIslands = 0

        # how many isolated island at init
        totalIslands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    totalIslands += 1

        uf = UnionFind(m * n)
        uf.setCount(totalIslands)

        for i in range(m):
            for j in range(n):
                print("At: (%s, %s), value: %s" %(i, j, grid[i][j]))
                if grid[i][j]:
                    # IMPORTANT:
                    # (i, j) to 1D index
                    # i * column + j
                    if i > 0 and grid[i - 1][j]: # check up
                        uf.union(i * n + j, (i - 1) * n + j)
                    if i < m - 1 and grid[i + 1][j]: # check down
                        uf.union(i * n + j, (i + 1) * n + j)
                    if j > 0 and grid[i][j - 1]: # check left
                        uf.union(i * n + j, i * n + (j - 1))
                    if j < n - 1 and grid[i][j + 1]: # check right
                        uf.union(i * n + j, i * n + (j + 1))

        return uf.getCount()

######
# BFS
######

class Solution2:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        # BFS

        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)]for j in range(m)]
        numIslands = 0

        # Serves 2 purposes
        # 1. check if out of boundry
        # 2. check if to be count as part of island grid value == 1 and not visited
        def check(x, y):
            if x >= 0 and x < m and y >= 0 and y < n and \
                grid[x][y] and visited[x][y] == False:
                return True

        def bfs(x,y):
            nbrow = [1,0,-1,0]
            nbcol = [0,1,0,-1]
            q = [(x,y)]
            while len(q) > 0:
                x = q[0][0]
                y = q[0][1]
                q.pop(0)
                for k in range(4):
                    newx = x + nbrow[k]
                    newy = y + nbcol[k]
                    if not (newx >= 0 and newx < m and newy >= 0 and newy < n):
                        continue
                    if grid[newx][newy] and visited[newx][newy] == False:
                        visited[newx][newy] = True
                        q.append((newx,newy))

        for row in range(m):
            for col in range(n):
                if grid[row][col] and visited[row][col] == False:
                    visited[row][col] = True
                    bfs(row,col)
                    numIslands += 1
        return numIslands

# Test Cases
if __name__ == "__main__":
    testCases = [
        [
            [1,1,0,0,0],
            [0,1,0,0,1],
            [0,0,0,1,1],
            [0,0,0,0,0],
            [0,0,0,0,1]
        ], # return 3
        [   [1,1,1,1,1,1],
            [1,0,0,0,0,1],
            [1,0,1,1,0,1],
            [1,0,0,0,0,1],
            [1,1,1,1,1,1]
        ], # return 2
    ]
    s1 = Solution1()
    s2 = Solution2()
    for grid in testCases:
        res1 = s1.numIslands(grid)
        print("res1: %s" %(res1))
        res2 = s2.numIslands(grid)
        print("res2: %s" %(res2))
