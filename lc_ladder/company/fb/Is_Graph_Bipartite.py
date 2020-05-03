#! /usr/local/bin/python3

# https://www.lintcode.com/problem/is-graph-bipartite/description
# Example

# 给定一个无向图 graph, 输出 true 当且仅当这个图是可以被二分的（也叫二部图）。
#
# 如果一个图是二部图，则意味着我们可以将图里的点集分为两个独立的子集A和B，并且图中所有的边都是一个端点属于A，另一个端点属于B。
#
# 关于图的表示：graph[i] 为一个列表，表示与节点i有边相连的节点。这个图中一共有 graph.length 个节点，为0到graph.length-1。
#
# 图中没有自边或者重复的边存在，即: graph[i] 中不包含 i, 也不会包含某个点两次。
#
# Example
# 样例 1:
#
# 输入: [[1,3], [0,2], [1,3], [0,2]]
# 输出: true
# 解释:
#   图看上去长这样：
#   0----1
#   |    |
#   |    |
#   3----2
#   所以我们可以把图分成以下两部分，并且各自内部没有连线: {0, 2} and {1, 3}.
# 样例 2:
#
# 输入: [[1,2,3], [0,2], [0,1,3], [0,2]]
# 输出: false
# 解释:
#   图看上去长这样：
#   0----1
#   | \  |
#   |  \ |
#   3----2
#   我们没有办法将这个点集分为两个独立的子集。（即各自内部没有连线）
# Notice
# graph 中包含的总节点数的范围为 [1, 100]。
# graph[i] 只包含范围为 [0, graph.length - 1].中的一些整数。
# graph[i] 不会包含 i 自己或是某个值两次。
# 图是无向的：如果点 j 存在于 graph[i]这个列表里，则 i 也会存在于 graph[j]这个列表里


"""
Algo: 二分图算法， DFS, BFS
D.S.: Graph

Solution:
重点题型 -- 二分图算法
solution1: DFS

step1: 构建vertex -> neighbors 无向图
step2: 给vertex涂色，以表示归类，没有颜色起始状态为0，先尝试图1色，它的邻居就是-1
step3: 做深度优先搜索，如果邻居没有颜色就涂上相反颜色，如果有颜色而且和当前vertex颜色一样，就可以返回false，所有邻居都满足条件返回true
step4: 要遍历每个没有被标记过得vertex

因为每个vertex 和 edge 都被访问一遍，所以复杂度是
Time: O(V + E)
Space: : O(V + E)

solution2: BFS
Time: O(V + E)
Space: : O(V + E)


Corner cases:
"""


class Solution1_DFS:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """
    def isBipartite(self, graph):
        # Write your code here

        n = len(graph)
        colors = [0] * n
        # graph is
        # index is vertex, value is vertex's neighbors
        for v in range(n):
            if colors[v] == 0 and self.dfs(graph, colors, v, 1) == False:
                return False
        return True

    def dfs(self, graph, colors, v, paint_color):
        colors[v] = paint_color
        for nei in graph[v]:
            if colors[nei] == 0 and self.dfs(graph, colors, nei, paint_color * (-1)) == False:
                return False
            if colors[nei] == colors[v]:
                return False
        return True

class Solution2_BFS:
    """
    @param graph: the given undirected graph
    @return:  return true if and only if it is bipartite
    """
    def isBipartite(self, graph):
        # Write your code here
        from collections import deque
        n = len(graph)
        colors = [0] * n
        # graph is
        # index is vertex, value is vertex's neighbors
        for v in range(n):
            if colors[v] == 0:
                q = deque([(v, 1)])
                colors[v] = 1
                while q:
                    (cur_v, cur_c) = q.popleft()
                    for nei in graph[cur_v]:
                        if colors[nei] == 0:
                            colors[nei] = cur_c * (-1)
                            q.append((nei, cur_c * (-1)))
                        if colors[nei] == cur_c:
                            return False
        return True
# Test Cases
if __name__ == "__main__":
    solution = Solution()
