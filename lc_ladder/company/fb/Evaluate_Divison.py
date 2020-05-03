#! /usr/local/bin/python3

# https://leetcode.com/problems/evaluate-division/submissions/
# Example
# Equations are given in the format A / B = k, where A and B are variables represented as strings,
# and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.
#
# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
# The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries ,
# where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.
#
# According to the example above:
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
"""
Algo: BFS, UnionFind, DFS
D.S.:

Solution1 BFS:

Solution2 UnionFind:

Time: O(N) -- all node
Space: O(N) -- edges and queue
Corner cases:
"""

class Solution1_BFS:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build bi-directional graph
        # graph: {
        #     key: from_node,
        #     val: {
        #         key: to_node,
        #         val: edge_value
        #     }
        # }
        graph = self._build_graph(equations, values)
        # calculate each query
        res = []
        for u, v in queries:
            res.append(self._get_value(u, v, graph))
        return res

    def _build_graph(self, equations, values):
        graph = {}
        for i in range(len(equations)):
            u, v, w = equations[i][0], equations[i][1], values[i]
            if u not in graph:
                graph[u] = {}
            if v not in graph[u]:
                graph[u][v] = 0
            graph[u][v] = w

            if v not in graph:
                graph[v] = {}
            if u not in graph[v]:
                graph[v][u] = 0
            graph[v][u] = 1.0 / w
        return graph

    def _get_value(self, u, v, graph):
        if u not in graph or v not in graph:
            return -1.0

        q = collections.deque([u])
        visited = set([u])
        # 注意path 的使用来记录走到当前节点的距离

        # path = {
        #     key: to_node,       eg: u
        #     val: to_node_value  eg: from u to to_node value
        # }
        path = {u: 1.0} # 注意：初始起点到起点的距离是1.0 不是1
        while q:
            cur_node = q.popleft()
            if cur_node == v:
                return path[cur_node]
            to_cur_value = path[cur_node]
            for next_node, value in graph[cur_node].items():
                if next_node in visited:
                    continue
                next_value = to_cur_value * value
                # 注意一定要记着mark visited
                visited.add(next_node)
                path[next_node] = next_value
                q.append(next_node)
        return -1.0

class Solution2_UnionFind:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def find(x):
            if x != U[x][0]:
                px, pv = find(U[x][0])
                U[x] = (px, U[x][1] * pv)
            return U[x]

        def divide(x, y):
            rx, vx = find(x)
            ry, vy = find(y)
            if rx != ry: return -1.0
            return vx / vy

        U = {}
        for (x, y), v in zip(equations, values):
            if x not in U and y not in U:
                U[x] = (y, v)
                U[y] = (y, 1.0)
            elif x not in U:
                U[x] = (y, v)
            elif y not in U:
                U[y] = (x, 1.0 / v)
            else:
                rx, vx = find(x)
                ry, vy = find(y)
                U[rx] = (ry, v / vx * vy)

        ans = [divide(x, y) if x in U and y in U else -1 for x, y in queries]
        return ans
# Test Cases
if __name__ == "__main__":
    solution = Solution()
