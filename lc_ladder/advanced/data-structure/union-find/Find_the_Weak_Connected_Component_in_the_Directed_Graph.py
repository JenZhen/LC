#! /usr/local/bin/python3

# https://www.lintcode.com/en/old/problem/find-the-weak-connected-component-in-the-directed-graph/
# Find the number Weak Connected Component in the directed graph. Each node in the graph contains a label and a list of its neighbors.
# (a connected set of a directed graph is a subgraph in which any two vertices are connected by direct edge path.)
# Example
# A----->B  C
#  \     |  |
#   \    |  |
#    \   |  |
#     \  v  v
#      ->D  E <- F
# Return {A,B,D}, {C,E,F}. Since there are two connected component which are {A,B,D} and {C,E,F}

"""
Algo:
D.S.: Union-Find/BFS

Solution:
1. Extension of Union-find model -- return all groups, which is presented as [[],[],[]]
Compare with "Connected Component in Undirected Graph"
Time: O(1) * n -- n is the number of edges

2. BFS # TODO:

Corner cases:
"""

"""
Definition for a directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

class Solution:
    """
    @param: nodes: a array of Directed graph node
    @return: a connected set of a directed graph
    """
    def __init__(self):
        self.father = {}
        # self.count = 0 # this alternative is working, but not key of this solution

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
            # self.count -= 1

    def connectedSet2(self, nodes):
        # write your code here
        if not nodes:
            return None
        self.count = len(nodes)
        for node in nodes:
            self.father[node.label] = node.label
        for node in nodes:
            for nei in node.neighbors:
                self.union(node.label, nei.label)
        # Re-iterate all nodes to find their roots
        # using map group to organize diff roots
        res = []
        group = {}
        cnt = 0
        for node in nodes:
            father = self.find(node.label)
            if father not in group:
                cnt += 1
                group[father] = cnt
            # IMPORTANT: this step is important!! Do not forget.
            if len(res) < cnt:
                res.append([])
            res[group[father] - 1].append(node.label)
        return res

# Test Cases
if __name__ == "__main__":
    s = Solution()
