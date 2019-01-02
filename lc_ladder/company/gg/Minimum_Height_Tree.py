#! /usr/local/bin/python3

# https://www.lintcode.com/problem/minimum-height-trees/description?_from=ladder&&fromId=18
# Example
# 对于一个树状的无向图，选择任何一个节点作为根。这个图就变成了一个有根树。在所有可能的有根树中，有最小高度的树叫做最小高度树（minimum height trees, MHTs）。
# 给定这样的图，找出所有的MHTs，返回根标记的数组。
# 格式
# 图包含了n个节点，标记从0到n-1。给定n和一个无向边列表edges。每一个边是一组节点标记。
# 假定没有重复的遍。由于所有的边是无向边，所以[0, 1]和[1, 0]是等价的，所以也不会同时出现在edges当中。
#
# 样例
# 样例 1:
#
# 给定 n = 4, edges = [[1, 0], [1, 2], [1, 3]]
#
#         0
#         |
#         1
#        / \
#       2   3
# 返回 [1]
#
# 样例 2:
#
# 给定 n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
#
#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5
# 返回 [3, 4]
#
# 注意事项
# （1）根据树的定义：一个树是一个无向图，且任意两个顶点都有唯一一条路径连通。也即，树中没有环。
# （2）树的高度是树根和叶子之间的最长边数。

"""
Algo: Topology sort, BFS, Use Toplogical sort to handle undirectional graph
D.S.:

Solution:
1. 将undirected graph convert to bi-directed graph 并进行topological sort
Time: O(n)

2. 做2遍BFS, 嵌套的
Time: O(n ^ 2)
不能AC

Corner cases:
"""
class Solution1:
    """
    @param n: n nodes labeled from 0 to n - 1
    @param edges: a undirected graph
    @return:  a list of all the MHTs root labels
    """
    def findMinHeightTrees(self, n, edges):
        if not edges:
            if n == 1:
                return [0]
            else:
                return []
        # Wirte your code here
        nodeMap = {} # key: node, val: [] its neighbors
        inDegree = {} # key: node, val: inDegree Count

        # Re-construct edges
        for e in edges:
            if e[0] not in nodeMap:
                nodeMap[e[0]] = [e[1]]
            else:
                nodeMap[e[0]].append(e[1])
            if e[1] not in nodeMap:
                nodeMap[e[1]] = [e[0]]
            else:
                nodeMap[e[1]].append(e[0])

            if e[0] not in inDegree:
                inDegree[e[0]] = 1
            else:
                inDegree[e[0]] += 1
            if e[1] not in inDegree:
                inDegree[e[1]] = 1
            else:
                inDegree[e[1]] += 1

        from collections import deque
        q = deque([])
        visited = [False for _ in range(n)]
        for key, val in inDegree.items():
            if val == 1:
                q.append(key)
                visited[key] = True

        res = []
        while len(q):
            res = []
            size = len(q)
            for i in range(size):
                curNode = q.popleft()
                res.append(curNode)
                for nei in nodeMap[curNode]:
                    if visited[nei]:
                        continue
                    inDegree[nei] -= 1
                    if inDegree[nei] == 1:
                        q.append(nei)
                        visited[nei] = True
        return res


class Solution2:
    """
    @param n: n nodes labeled from 0 to n - 1
    @param edges: a undirected graph
    @return:  a list of all the MHTs root labels
    """
    def findMinHeightTrees(self, n, edges):
        # Wirte your code here
        if n == 1:
            return [0]
        nodeMap = {} # key node, val: list of its neighbor (guranteed no dup)
        for e in edges:
            if e[0] not in nodeMap:
                nodeMap[e[0]] = [e[1]]
            else:
                nodeMap[e[0]].append(e[1])
            if e[1] not in nodeMap:
                nodeMap[e[1]] = [e[0]]
            else:
                nodeMap[e[1]].append(e[0])
        print(nodeMap)
        res = []
        minHeight = n + 1
        for i in range(n):
            # do bfs starting from each node,
            # find the longest depth for each
            # the smallest of them is the rest
            level = self.bfs(i, nodeMap)
            print("i: %s, level: %s" %(i, level))
            if level < minHeight:
                res = [i]
                minHeight = level
            elif level == minHeight:
                res.append(i)
        return res

    def bfs(self, node, nodeMap):
        from collections import deque
        visited = [False for _ in range(len(nodeMap))]
        level = 0 # increment when start populating that level to queue
        q = deque([node])
        visited[node] = True
        while len(q):
            levelSize = len(q)
            level += 1
            for i in range(levelSize):
                curNode = q.popleft()
                for neighbor in nodeMap[curNode]:
                    if visited[neighbor]:
                        continue
                    q.append(neighbor)
                    visited[neighbor] = True
        return level
# Test Cases
if __name__ == "__main__":
    solution = Solution()
