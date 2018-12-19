#! /usr/local/bin/python3

# https://lintcode.com/en/problem/connected-component-in-undirected-graph/description
# Example
# 找出无向图中所有的连通块。
#
# 图中的每个节点包含一个label属性和一个邻接点的列表。（一个无向图的连通块是一个子图，其中任意两个顶点通过路径相连，且不与整个图中的其它顶点相连。）
# 样例
# 给定图:
#
# A------B  C
#  \     |  |
#   \    |  |
#    \   |  |
#     \  |  |
#       D   E
# 返回 {A,B,D}, {C,E}。其中有 2 个连通块，即{A,B,D}, {C,E}
"""
Algo: BFS
D.S.:

Solution:
Template question
1. build visited dict using graph
2. bfs starting from nodes that has not been visited
Time: O(n)

Solution2:
Union-Find

Corner cases:
"""

"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque
class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        # write your code here
        if not nodes:
            return []

        visited = {}
        for node in nodes:
            visited[node.label] = False
        res = []
        for node in nodes:
            if visited[node.label] == False:
                nodesSet = self.bfs(node, visited)
                res.append(nodesSet)
        return res

    def bfs(self, node, visited):
        temp = [] # store node.label
        q = deque([]) # store node
        q.append(node)
        visited[node.label] = True
        while len(q):
            cur = q.popleft()
            # node enter and exit queue only once
            # append to result when leaving the queue
            temp.append(cur.label)
            for nei in cur.neighbors:
                # to make sure same element doesn't enter queue twice,
                # check visited dict before put in queue
                if visited[nei.label] == False:
                    q.append(nei)
                    visited[nei.label] = True
        temp.sort()
        return temp



# Test Cases
if __name__ == "__main__":
    solution = Solution()
