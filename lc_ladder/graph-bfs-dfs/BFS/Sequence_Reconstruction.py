#! /usr/local/bin/python3

# https://www.lintcode.com/problem/sequence-reconstruction/description
# Example
# 判断是否序列 org 能唯一地由 seqs重构得出. org是一个由从1到n的正整数排列而成的序列，1 ≤ n ≤ 10^4.
# 重构表示组合成seqs的一个最短的父序列 (意思是，一个最短的序列使得所有 seqs里的序列都是它的子序列).
# 判断是否有且仅有一个能从 seqs重构出来的序列，并且这个序列是org。
#

# 样例
# 给定 org = [1,2,3], seqs = [[1,2],[1,3]]
# 返回 false
# 解释:
# [1,2,3] 并不是唯一可以被重构出的序列，还可以重构出 [1,3,2]
#
# 给出 org = [1,2,3], seqs = [[1,2]]
# 返回 false
# 解释:
# 能重构出的序列只有 [1,2].
#
# 给定 org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
# 返回 true
# 解释:
# 序列 [1,2], [1,3], 和 [2,3] 可以唯一重构出 [1,2,3].
#
# 给定org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
# 返回 true

"""
Algo: BFS
D.S.:

Solution:
经典拓扑BFS， 根据indegree来排先后顺序
len(q) 大于1时说明有可能存在多种排列可能

这个题集中体现用collections defaultdict 比普通dict 的优势 default value 

Corner cases:
1. [] [[]] -> true
2. [1] [[1]] -> true
"""

rom collections import defaultdict
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # edges: {} key: from, val: to list
        # indegrees: {} key: node, val: cnt of coming
        # nodes: set total set of node
        edges = defaultdict(list)
        indegrees = defaultdict(int)
        nodes = set()
        for seq in seqs:
            # note that seq is a list of int not a pair
            # merge all int in seq to nodes.
            nodes |= set(seq)
            for i in range(len(seq)):
                if i == 0:
                    indegrees[seq[i]] += 0
                if i < len(seq) - 1:
                    edges[seq[i]].append(seq[i + 1])
                    indegrees[seq[i + 1]] += 1

        cur = [k for k in indegrees if indegrees[k] == 0]
        res = []

        while len(cur) == 1:
            cur_node = cur.pop()
            res.append(cur_node)
            # use defaultdict to avoid edges[cur_node] not populated
            for node in edges[cur_node]:
                indegrees[node] -= 1
                if indegrees[node] == 0:
                    cur.append(node)
        if len(cur) > 1:
            return False
        # len(res) == len(nodes) ensure all nodes considered
        return len(res) == len(nodes) and res == org


# Test Cases
if __name__ == "__main__":
    solution = Solution()
