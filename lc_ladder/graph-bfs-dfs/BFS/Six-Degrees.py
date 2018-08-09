#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo: BFS, DFS
D.S.: UndirectedGraphNode

Solution:
1. BFS
Use dict = {} key = node, value = dist (Starting from 0) to
Time: O(N) -- n nodes in total
Space: O(3N) -- use visited to avoid loop

2. DFS

Corner cases:
"""

# Definition for Undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


from collections import deque
class Solution1:
    '''
    @param {UndirectedGraphNode[]} graph a list of Undirected graph node
    @param {UndirectedGraphNode} s, t two Undirected graph nodes
    @return {int} an integer
    '''
    def sixDegrees(self, graph, s, t):
        if not graph or not s or not t:
            return -1 # invalid result not 0 distant

        dist = {}
        visited = {}
        q = deque([])

        q.append(s)
        dist[s] = 0

        while len(q):
            curNode = q.leftpop()
            if curNode == t:
                return dist[curNode]
            for nei in curNode.neighbors:
                if not visited[nei]:
                    q.append(nei)
                    dist[nei] = dist[curNode] + 1
                    visited[nei] = True
        return -1 # t not found

class Solution2:
    '''
    @param {UndirectedGraphNode[]} graph a list of Undirected graph node
    @param {UndirectedGraphNode} s, t two Undirected graph nodes
    @return {int} an integer
    '''
    def sixDegrees(self, graph, s, t):




# Test Cases
if __name__ == "__main__":
    solution = Solution()
