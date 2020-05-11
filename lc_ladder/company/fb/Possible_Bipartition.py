#! /usr/local/bin/python3

# https://leetcode.com/problems/possible-bipartition/
# Example
# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
#
# Each person may dislike some other people, and they should not go into the same group.
#
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
#
# Return true if and only if it is possible to split everyone into two groups in this way.
#
#
#
# Example 1:
#
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
# Example 2:
#
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
# Example 3:
#
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
#
#
# Note:
#
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].

"""
Algo: 二分图 DFS, BFS
D.S.:

Solution:
此题的数据规模太大， 不能用单纯的DFS搜索，会崩溃
Time: O(V + E)
Space: O(V + E)

Corner cases:
"""

class Solution_BFS:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes: return True
        g = self._build_graph(dislikes)
        colors = [0] * (N + 1)
        for i in range(1, N + 1):
            if colors[i] == 0: # 开始一轮新的BFS的条件
                q = collections.deque([(i, 1)])
                colors[i] = 1
                while q:
                    cur_node, cur_color = q.popleft()
                    # 注意 Cornercase: 有可能这个节点就不在dislikes 里面所以要查 在不在graph中
                    # 也可以把 graph 对所有node 建key, 这个方式更好！！
                    if cur_node not in g:
                        continue
                    for nei in g[cur_node]:
                        if colors[nei] == 0:
                            colors[nei] = cur_color * (-1)
                            q.append((nei, colors[nei]))
                        elif colors[nei] == cur_color:
                            return False
        return True

    def _build_graph(self, dislikes):
        g = {} # key: node, val: [list of node it doesn't like]
        for u, v in dislikes:
            if u not in g:
                g[u] = []
            g[u].append(v)
            if v not in g:
                g[v] = []
            g[v].append(u)
        return g


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        colors = [0] * (N + 1)
        # g idx person id (no person 0), value people he dislikes
        graph = [[] for _ in range(N + 1)]
        for e in dislikes:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        for v in range(N):
            if colors[v] == 0 and self.dfs(colors, graph, v, 1) == False:
                return False
        return True

    def dfs(self, colors, graph, v, paint_color):
        colors[v] = paint_color
        for nei in graph[v]:
            if colors[nei] == 0 and self.dfs(colors, graph, nei, paint_color * (-1)) == False:
                return False
            if colors[nei] == paint_color:
                return False
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
