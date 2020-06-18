#! /usr/local/bin/python3

# https://leetcode.com/problems/tree-diameter/submissions/
# Example
# Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.
# The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.
# Each node has labels in the set {0, 1, ..., edges.length}.
# Example 1:
# Input: edges = [[0,1],[0,2]]
# Output: 2
# Explanation:
# A longest path of the tree is the path 1 - 0 - 2.
# Example 2:
# Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
# Output: 4
# Explanation:
# A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
#
# Constraints:
# 0 <= edges.length < 10^4
# edges[i][0] != edges[i][1]
# 0 <= edges[i][j] <= edges.length
# The given edges form an undirected tree.
"""
Algo: DFS
D.S.:

Solution:
注意 利用parent 属性
Time: O(n) - 每个node visited once
Space: O(1)

Corner cases:
"""

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges: return 0
        # build graph
        self.g = [[] for _ in range(len(edges) + 1)]
        for u, v in edges:
            self.g[u].append(v)
            self.g[v].append(u)
        self.res = 1
        self.dfs(-1, 0)
        return self.res

    def dfs(self, parent, node):
        lpath = spath = 0
        for child in self.g[node]:
            if child == parent:
                continue
            path = self.dfs(node, child)
            if path >= lpath:
                spath = lpath
                lpath = path
            elif path > spath:
                spath = path
        self.res = max(self.res, lpath + spath)
        return lpath + 1
# Test Cases
if __name__ == "__main__":
    solution = Solution()
