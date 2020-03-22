#! /usr/local/bin/python3

# https://www.lintcode.com/problem/connecting-graph/description
# Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.
# You need to support the following method:
# 1. connect(a, b), add an edge to connect node a and node b. 2.query(a, b)`, check if two nodes are connected
# Example
# 5 // n = 5
# query(1, 2) return false
# connect(1, 2)
# query(1, 3) return false
# connect(2, 4)
# query(1, 4) return true

"""
Algo:
D.S.: Union-Find/BFS

Solution:
1. UnionFind template.
Time: O(1)
2. BFS: # TODO: 

Corner cases:
"""

class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.father = [0] * (n + 1)
        for i in range(1, n + 1):
            self.father[i] = i # each node is its own father

    def find(self, a):
        if self.father[a] == a:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        # write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b

    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        # write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b

# Test Cases
if __name__ == "__main__":
    s = Solution()
