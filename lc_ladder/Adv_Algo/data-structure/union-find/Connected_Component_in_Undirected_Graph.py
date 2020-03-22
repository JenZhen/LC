#! /usr/local/bin/python3

# https://www.lintcode.com/problem/connected-component-in-undirected-graph/description
# Find the number connected component in the undirected graph.
# Each node in the graph contains a label and a list of its neighbors.
# (a connected component (or just component) of an undirected graph is a subgraph in which
# any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.)

# Example
# A------B  C
#  \     |  |
#   \    |  |
#    \   |  |
#     \  |  |
#       D   E
# Return {A,B,D}, {C,E}. Since there are two connected component which is {A,B,D}, {C,E}

"""
Algo:
D.S.: Union-Find/BFS

Solution:
1. Union-Find template
Compare with "find-the-weak-connected-component-in-the-directed-graph"
Time: O(1) * (2 * n) -- n is the number of edges, undirected edge will be counted twice

2. BFS # TODO:

Corner cases:
"""

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
class UnionFind(object):
    def __init__(self, nodes):
        self.father = {}
        for node in nodes:
            self.father[node.label] = node.label

    def find(self, label):
        if self.father[label] == label:
            return label
        self.father[label] = self.find(self.father[label])
        return self.father[label]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b

class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        if not nodes:
            return None

        uf = UnionFind(nodes)
        for node in nodes:
            for nei in node.neighbors:
                uf.union(node.label, nei.label)
        res = []
        group = {}
        cnt = 0
        for node in nodes:
            root_node = uf.find(node.label)
            if root_node not in group:
                cnt += 1
                group[root_node] = cnt
            if len(res) < cnt:
                res.append([])
            res[group[root_node] - 1].append(node.label)
        return res




"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution_BFS:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        if not nodes:
            return []
        from collections import deque
        res = []
        visited = set()
        for node in nodes:
            if node not in visited:
                group = [node.label]
                q = deque([node])
                visited.add(node)
                while len(q):
                    curnode = q.popleft()
                    for nei in curnode.neighbors:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
                            group.append(nei.label)
                # NOTE sorted(group) ->return a sorted list
                # group.sort()->modify group but return none
                res.append(sorted(group))
        return res
# Test Cases
if __name__ == "__main__":
    s = Solution()
