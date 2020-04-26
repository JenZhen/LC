#! /usr/local/bin/python3

# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/
# Example
# We are given a binary tree (with root node root), a target node, and an integer value K.
#
# Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.
#
# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# Output: [7,4,1]
#
# Explanation:
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
#
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these objects.
#
# Note:
# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.
"""
Algo: DFS, BFS
D.S.:

Solution:
1. DFS to add parent to node
2. BFS to search k distance

Time: O(n) -- each node visited twice
Space: O(n) - each node add a parent
Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        self.dfs(root, None)

        q = collections.deque([(target, 0)])
        visited = {target}
        while q:
            if q[0][1] == K:
                return [node.val for node, level in q]
            node, level = q.popleft()
            for nei in [node.left, node.right, node.parent]:
                if nei and nei not in visited:
                    visited.add(nei)
                    q.append((nei, level + 1))
        return []

    def dfs(self, node, parent_node):
        if node:
            node.parent = parent_node
            self.dfs(node.left, node)
            self.dfs(node.right, node)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
