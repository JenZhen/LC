#! /usr/local/bin/python3

# https://lintcode.com/problem/graph-valid-tree/description
# Example

"""
Algo: BFS
D.S.: deque-implemented queue

Solution:
Solution1:Same as lc_ladder/advanced/data-structure/union-find
Solution2: BFS
Define of invalid tree
1. loop
2. not connected dot

conditions
1.
len(edges) == n - 1
2.
connectedSet size == n

Time: O(n)

Corner cases:
"""

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        from collections import deque

        if not n or edges is None or len(edges) != (n - 1):
            return False

        treeGraph = self.getTreeGraph(n, edges)
        q = deque([])
        visited = set()
        q.append(0)
        visited.add(0) # visited used to make sure visted node not visted again, so q won't be inifinte loop
        while len(q):
            cur = q.popleft()
            neighbors = treeGraph[cur]
            print("%s 's neigh: %s" %(cur, neighbors))
            for nei in neighbors:
                if nei in visited:
                    continue
                q.append(nei)
                visited.add(nei)
        print("visited size: %s, %s" %(len(visited), n))
        return len(visited) == n


    def getTreeGraph(self, n, edges):
        graph = {}
        for i in range(n):
            graph[i] = set()

        for e in edges:
            u, v = e[0], e[1]
            graph[u].add(v)
            graph[v].add(u)
        return graph

# Test Cases
if __name__ == "__main__":
    solution = Solution()
