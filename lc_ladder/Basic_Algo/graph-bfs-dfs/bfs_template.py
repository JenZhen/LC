#! /usr/local/bin/python3

from collections import deque
class Solution1:
    def getAllNodes(self, edges):
        """
        1. transform edges to graph structure node: {neighbor set} -- dict structure
        2. iterate graph to get all nodes
        """
        if not edges:
            return []
        graph = self.constructGraph(edges)
        nodes = [key for key in graph]
        nodes.sort()
        print("nodes: %s" %nodes)
        return nodes

    def getAllSets(self, edges):
        """
        1. transform edges to grpah (dict)
        2. iterate graph to get all nodes and init in visited dict as False
        3. bfs graph
        """
        graph = self.constructGraph(edges)
        nodes = [key for key in graph]
        nodes.sort() # optional

        visited = {}
        for node in nodes:
            visited[node] = False

        res = []
        print("size of nodes : %s" %len(nodes))
        for node in nodes:
            if visited[node] == False:
                getSet = self.bfs(node, visited, graph)
                # Can also do bfs(graph, visited, res) and have res populated inside of function
                print("got a set")
                res.append(getSet)
        print("Got set: %s" %res)
        return res

    def constructGraph(self, edges):
        graph = {}
        for edge in edges:
            u, v = edge[0], edge[1]
            if u not in graph:
                graph[u] = set()
            graph[u].add(v)
            if v not in graph:
                graph[v] = set()
            graph[v].add(u)
        return graph

    def bfs(self, startNode, visited, graph):
        temp = []
        q = deque([startNode])
        visited[startNode] = True
        while len(q):
            print("q %s" %q)
            cur = q.popleft()
            temp.append(cur)
            neighbors = graph[cur]
            for nei in neighbors:
                if visited[nei] == False:
                    q.append(nei)
                    visited[nei] = True
        temp.sort()
        print("one set: %s" %temp)
        return temp


# Test Cases
if __name__ == "__main__":
    """
        1
     /     \
    2 ----- 3
    |
    4 ----- 5

    0 ----- 6
    """
    edges = [
        [1, 2],
        [1, 3],
        [2, 3],
        [2, 4],
        [4, 5],
        [0, 6]
    ]
    s1 = Solution1()
    nodes = s1.getAllNodes(edges)
    s1.getAllSets(edges)
