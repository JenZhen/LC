#! /usr/local/bin/python3

# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
# Undirectional, given edges list has no duplicate.
# Example
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

"""
Algo: BFS
D.S.: Union-Find

Solution:
1. Union-Find
Time: O(n) n * O(1) -- n nodes, n - 1 valid edges, 2(n - 1) union-find operation on those nodes

2. BFS
See Basic_Algo/graph-bfs-dfs/BFS
Corner cases:
- Invalid input: n - 1 != len(edges)

"""

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n - 1 != len(edges):
            return False

        self.father = [i for i in range(n)]
        def findRoot(a):
            if self.father[a] == a:
                return a
            self.father[a] = findRoot(self.father[a])
            return self.father[a]

        for edge in edges:
            end1, end2 = edge[0], edge[1]
            if end1 == end2:
                continue
            root1 = findRoot(end1)
            root2 = findRoot(end2)
            if root1 != root2:
                self.father[root1] = root2
            else:
                return False
        return True

# Test Cases
if __name__ == "__main__":
    s = Solution()
