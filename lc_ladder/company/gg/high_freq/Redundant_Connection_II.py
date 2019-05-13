#! /usr/local/bin/python3

# https://leetcode.com/problems/redundant-connection-ii/
# Example
# In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.
#
# The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
#
# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.
#
# Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.
#
# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given directed graph will be like this:
#   1
#  / \
# v   v
# 2-->3
# Example 2:
# Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# Output: [4,1]
# Explanation: The given directed graph will be like this:
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3
# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
"""
Algo: union-find
D.S.:

Solution:
有向图的两种不满足情况
1. 2个父
2. 有环
3. 有2个父亲且有环，要找出那个在环中的父亲

Corner cases:
"""

class UnionFind():
    def __init__(self, n):
        self.father = [i for i in range(n + 1)]

    def find(self, i):
        if self.father[i] == i:
            return i
        self.father[i] = self.find(self.father[i])
        return self.father[i]

    def union(self, a, b):
        # a is father of b
        a_father = self.find(a)
        b_father = self.find(b)
        if a_father == b_father:
            return False
        else:
            a_father = self.find(a)
            b_father = self.find(b)
            self.father[b_father] = a_father
            return True

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        # 2 cases of invalidity
        # 1. more than 1 parent
        n = len(edges) # number of nodes 1 - n n nodes
        father = [0 for _ in range(n + 1)]
        candA = candB = None
        for e in edges:
            u, v = e[0], e[1]
            if father[v] != 0:
                # v has another father
                candA = [father[v], v] # first father
                candB = [u, v] # second father
                break
            father[v] = u

        # start to find if loop exists
        uf = UnionFind(len(edges))
        for e in edges:
            u, v = e[0], e[1]
            if [u, v] == candB: continue # 不把第二个father connection 考虑
            if not uf.union(u, v):
                # loop from u -> v
                if candA == None:
                    # has loop, 只有一个父亲，那么这个构成环的边需要返回
                    return [u, v]
                else:
                    # loop, 2 fathers, return candA in loop
                    # 有环，只考虑了第一个父亲，无论第第二个怎么样，这个在环里的父亲is the problem
                    print("loop 2 father")
                    return candA

        # when not counting candB, everything ok then candB's fault
        # 没环，应该有2个父亲，返回第二个
        print("no loop 2 father")
        return candB

# Test Cases
if __name__ == "__main__":
    solution = Solution()
