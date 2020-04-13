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
1.len(edges) == n - 1
2.ConnectedSet size == n
Time: O(n)

Corner cases:
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 很重要的一个CORNER CASE
        # 只有一个节点 没有边
        if n == 1 and len(edges) == 0:
            return True
        if not n or not edges or len(edges) != n - 1:
            return False

        graph = self.getTreeGraph(n, edges)

        visited = set([0])
        q = collections.deque([0])

        while q:
            cur_node = q.popleft()
            for node in graph[cur_node]:
                if node not in visited:
                    visited.add(node)
                    q.append(node)
        return len(visited) == n

    def getTreeGraph(self, n, edges):
        graph = [[] for _ in range(n)]
        for e in edges:
            u, v = e[0], e[1]
            graph[u].append(v)
            graph[v].append(u)
        return graph


# Test Cases
if __name__ == "__main__":
    solution = Solution()
