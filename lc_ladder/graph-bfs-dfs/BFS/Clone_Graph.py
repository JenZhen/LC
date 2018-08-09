#! /usr/local/bin/python3

# https://lintcode.com/problem/clone-graph/description
# Example

"""
Algo: BFS
D.S.: deque implemented queue, map

Solution:
Time: O(n)

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
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        root = node
        if not node:
            return node

        nodes = self.getNodes(node)
        nodeMap = {}
        # copy nodes
        for node in nodes:
            nodeMap[node] = UndirectedGraphNode(node.label)
        # copy edges/neighbors
        for node in nodes:
            for neighbor in node.neighbors:
                nodeMap[node].neighbors.append(nodeMap[neighbor])
        # IMPORTANT:
        # return nodeMap[node], is wrong in lintcode, need a copy of node
        # Even tho I don't think value of node is modified
        return nodeMap[root]

    def getNodes(self, node):
        s = set()
        q = deque([])
        q.append(node)
        s.add(node)
        while len(q):
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in s:
                    q.append(neighbor)
                    s.add(neighbor)
        return s

#  additionally, compare 2 methods of getting all nodes
def getNodes(self, node):
        s1 = set()

        q1 = deque([])
        q1.append(node)
        s1.add(node)
        while len(q1):
            cur = q1.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in s1:
                    q1.append(neighbor)
                    s1.add(neighbor)
        print("s1: %s" %(','.join([str(ele.label) for ele in s1])))
        s2 = set()
        q2 = [node]
        s2.add(node)
        idx = 0
        while idx < len(q2):
            cur = q2[idx]
            for neighbor in cur.neighbors:
                if neighbor not in s2:
                    q2.append(neighbor)
                    s2.add(neighbor)
            idx += 1
        print("s2: %s" %(','.join([str(ele.label) for ele in s2])))
        return s2
# Test Cases
if __name__ == "__main__":
    solution = Solution()
