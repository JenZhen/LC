#! /usr/local/bin/python3

# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/
# Example
# Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.
# Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree.
# Also, a node is called a leaf if it has no children.
# In the following examples, the input tree is represented in flattened form row by row.
# The actual root tree given will be a TreeNode object.
#
# Example 1:
#
# Input:
# root = [1, 3, 2], k = 1
# Diagram of binary tree:
#           1
#          / \
#         3   2
#
# Output: 2 (or 3)
#
# Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
# Example 2:
#
# Input:
# root = [1], k = 1
# Output: 1
#
# Explanation: The nearest leaf node is the root node itself.
# Example 3:
#
# Input:
# root = [1,2,3,4,null,null,null,5,null,6], k = 2
# Diagram of binary tree:
#              1
#             / \
#            2   3
#           /
#          4
#         /
#        5
#       /
#      6
#
# Output: 3
# Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
# Note:
# root represents a binary tree with at least 1 node and at most 1000 nodes.
# Every node has a unique node.val in range [1, 1000].
# There exists some node in the given binary tree for which node.val == k.
"""
Algo: BFS, DFS
D.S.:

Solution:
1. DFS : build neighbor
2. 叶节点 只有一个nei 注意区别 root 的parent也是只有一个Nei
BFS 从K节点找到第一个leaf

Time: O(n)
Space: O(n)
Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        if not root:
            return None
        self.graph = {} # key: node, val, neighbor node
        # build father node
        self.dfs(root, TreeNode('*'))

        # init q with node of value k, then bfs
        q = collections.deque([node for node in self.graph if node.val == k])
        visited = set(q)
        while q:
            node = q.popleft()
            if node.val == '*':
                # skip root's parent
                continue
            if len(self.graph[node]) == 1:
                # leaf node has only one edge
                return node.val
            for nei in self.graph[node]:
                if nei in visited:
                    continue
                q.append(nei)
                visited.add(nei)


    def dfs(self, node, parent):
        if not node:
            return
        if node not in self.graph:
            self.graph[node] = []
        if parent not in self.graph:
            self.graph[parent] = []
        self.graph[node].append(parent)
        self.graph[parent].append(node)
        self.dfs(node.left, node)
        self.dfs(node.right, node)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
