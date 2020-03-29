#! /usr/local/bin/python3

# https://www.lintcode.com/en/old/problem/connecting-graph-iii/
# Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.
# You need to support the following method:
# 1. connect(a, b), an edge to connect node a and node b
# 2. query(), Returns the number of connected component in the graph

# Example
# 5 // n = 5
# query() return 5
# connect(1, 2)
# query() return 4
# connect(2, 4)
# query() return 3
# connect(1, 4)
# query() return 3

"""
Algo:
D.S.: Union-Find

Solution:
UnionFind template with count of all groups.
Starting with n nodes, then started with n groups each union reduces 1 group
Time: O(1)

Corner cases:
"""
class ConnectingGraph3:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.count = n
        self.father = [i for i in range(n + 1)]

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
            self.count -= 1

    """
    @return: An integer
    """
    def query(self):
        # write your code here
        return self.count


# Test Cases
if __name__ == "__main__":
    s = Solution()
