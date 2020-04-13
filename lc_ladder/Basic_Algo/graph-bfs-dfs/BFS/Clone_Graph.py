#! /usr/local/bin/python3

# https://leetcode.com/problems/clone-graph/submissions/
# Example

"""
Algo: BFS/DFS
D.S.: deque implemented queue, map

Solution:
BFS:
Time: O(n)
Space: O(n)

DFS:
Time: O(n)
Space: O(n)

Corner cases:
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution_BFS:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        q = collections.deque([node])
        node_map = {}
        node_map[node] = Node(node.val, [])

        while q:
            cur_node = q.popleft()
            for n in cur_node.neighbors:
                # 一定要考虑是否访问过NODE n
                if n not in node_map:
                    node_map[n] = Node(n.val)
                    q.append(n)
                node_map[cur_node].neighbors.append(node_map[n])
        return node_map[node]


class Solution_DFS:
    def __init__(self):
        self.map = {}
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node

        if node in self.map:
            return self.map[node]

        clone_node = Node(node.val)

        self.map[node] = clone_node

        clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node
# Test Cases
if __name__ == "__main__":
    solution = Solution()
