#! /usr/local/bin/python3

# https://www.lintcode.com/en/old/problem/number-of-islands-ii/
# Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k).
# Originally, the 2D matrix is all 0 which means there is only sea in the matrix.
# The list pair has k operator and each operator has two integer A[i].x, A[i].y means that
# you can change the grid matrix[A[i].x][A[i].y] from sea to island.
# Return how many island are there in the matrix after each operator.
#
# Notice
# 0 is represented as the sea, 1 is represented as the island. If two 1 is adjacent,
# we consider them in the same island. We only consider up/down/left/right adjacent.
# Example
# Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].
# return [1,1,2,2].

"""
Algo:
D.S.: UnionFind

Solution:
Similar to "Number_of_Islands".

Skill to check up/down/left/right:
- Like in this problem, use 4 if's, and check boundry in those if's
- xChg = [1, -1, 0, 0]; yChg = [0, 0, 1, -1]
    need to add extra step to check boundry

Corner cases:
***
if there is a duplicate Point (already painted as 1) in operators:
eg. "operators": [Point(0,0), Point(0,1), Point(2,2), Point(2,2)], use current cnt, then skip to next iteration
"""

"""
Definition for a point.
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class UnionFind(object):
    def __init__(self, number):
        self.father = [i for i in range(number)]
        self.cnt = 0

    def find(self, a):
        if self.father[a] == a:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.cnt -= 1

    def increCnt(self):
        self.cnt += 1

    def getCnt(self):
        return self.cnt

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        # write your code here
        # n -- #row
        # m -- #col
        if not m or not n or not operators:
            return []

        def twoD_oneD(x, y):
            return x * m + y # m is column number

        uf = UnionFind(n * m)
        grid = [[0 for j in range(m)] for i in range(n)]
        res = []
        for op in operators:
            x, y = op.x, op.y
            # check with itself first
            if grid[x][y] == 1:
                res.append(uf.getCnt())
                continue
            uf.increCnt()
            # check up
            if x > 0 and grid[x - 1][y] == 1:
                uf.union(twoD_oneD(x, y), twoD_oneD(x - 1, y))
            # check down
            if x + 1 < n and grid[x + 1][y] == 1:
                uf.union(twoD_oneD(x, y), twoD_oneD(x + 1, y))
            # check left
            if y > 0 and grid[x][y - 1] == 1:
                uf.union(twoD_oneD(x, y), twoD_oneD(x, y - 1))
            # check right
            if y + 1 < m and grid[x][y + 1] == 1:
                uf.union(twoD_oneD(x, y), twoD_oneD(x, y + 1))
            # paint grid[x][y] = 1
            grid[x][y] = 1
            res.append(uf.getCnt())
        return res



# Test Cases
if __name__ == "__main__":
    testCases = [
        {
            "n": 3,
            "m": 3,
            "operators": [Point(0,0), Point(0,1), Point(2,2), Point(2,1)]
        },
        {
            "n": 3,
            "m": 3,
            "operators": [Point(0,0), Point(0,1), Point(2,2), Point(2,2)]
        },
    ]
    s = Solution()
    for t in testCases:
        n = t["n"]
        m = t["m"]
        operators = t["operators"]
        res = s.numIslands2(n, m, operators)
        print("res: %s" %res)
