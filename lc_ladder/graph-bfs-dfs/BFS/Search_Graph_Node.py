#! /usr/local/bin/python3

# https://www.jiuzhang.com/solution/search-graph-nodes#tag-highlight-lang-python
# Example
# 给定一张 无向图，一个 节点 以及一个 目标值，返回距离这个节点最近 且 值为目标值的节点，如果不能找到则返回 NULL。
# 在给出的参数中, 我们用 map 来存节点的值

"""
Algo:
D.S.:

Solution:
1. Find target, simply do BFS
2. Find depth, simple BFS + Search by level for i in range(each level size), level += 1

Both way need to use set/hashmap to avoid loop

Corner cases:
"""

class Solution:
    # @param {UndirectedGraphNode[]} graph a list of undirected graph node
    # @param {dict} values a dict, <UndirectedGraphNode, (int)value>
    # @param {UndirectedGraphNode} node an Undirected graph node
    # @param {int} target an integer
    # @return {UndirectedGraphNode} a node
    def searchNode(self, graph, values, node, target):
        # Write your code here
        import Queue
        q = Queue.Queue(maxsize = len(graph))
        if values[node] == target:
            return node

        q.put(node)
        del values[node]

        while not q.empty():
            head = q.get()
            for n in head.neighbors:
                if n in values:
                    if values[n] == target:
                        return n
                    del values[n]
                    q.put(n)
        return None

# Test Cases
if __name__ == "__main__":
    solution = Solution()
