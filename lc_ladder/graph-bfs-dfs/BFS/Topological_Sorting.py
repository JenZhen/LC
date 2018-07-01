#! /usr/local/bin/python3

# https://www.lintcode.com/problem/topological-sorting/description
# Example

"""
Algo: BFS, topological sorting
D.S.:

Solution:
topological applies only to "Directed Acyclical Graph" -- "有向无环图"
入度： inDegree -- how many edges point to a node
出度： outDegree -- how many nodes this node points to
For a starting node, 入度 == 0， 出度 > 0
可以同时有好几个starting nodes
When removing a starting node, 它指向的nodes 的入度要减1， 当入度==1时，该点变为starting node
所以维护一个入度的map 很有必要

如果有环，会出现：starting node 遍历结束， len(queue) == 0, 但是还有点入度 > 0, 同时可以用这个性质来证明是否有环存在

对于有向无环图，通常可以用topological sorting

Corner cases:
"""

"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        # step1: build inDegree map for all neighbors
        inDegree = {}
        for node in graph:
            for nei in node.neighbors:
                if nei.label not in inDegree:
                    inDegree[nei.label] = 1
                else:
                    inDegree[nei.label] += 1
        # step2: iterate all possible heads, if not in inDegree map,
        # add to queue, it could be a starting node
        res = []
        q = deque([])
        for node in graph:
            if node.label not in inDegree:
                q.append(node)
        # BFS head, and when removing head, updating inDegree value
        while len(q):
            cur = q.popleft()
            res.append(cur) # append node, sometimes append node.label
            for nei in cur.neighbors:
                inDegree[nei.label] -= 1
                if inDegree[nei.label] == 0:
                    q.append(nei)
        # check if there's a loop
        # if len(res) != len(graph):
        #     return -1 
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
