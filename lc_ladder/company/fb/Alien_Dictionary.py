#! /usr/local/bin/python3

# https://www.lintcode.com/problem/alien-dictionary/description
# Example
# 有一种新的使用拉丁字母的外来语言。但是，你不知道字母之间的顺序。你会从词典中收到一个非空的单词列表，其中的单词在这种新语言的规则下按字典顺序排序。请推导出这种语言的字母顺序。
#
# Example
# 在字典中给出以下单词
#
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# 正确的顺序为: "wertf"
#
# 在字典中给出以下单词
#
# [
#   "z",
#   "x"
# ]
# 正确的顺序为: "zx".
#
# Notice
# 你可以假设所有的字母都是小写。
# 你可以假设如果a是b的前缀，那么a必须出现在给定字典中的b之前。
# 如果顺序是无效的，则返回空字符串。
# 这里可能有多个有效的字母顺序，返回以字典顺序看来最小的。

"""
Algo: graph, topological sort
D.S.: map, heap

Solution:
1. 建立graph 有向图， 注意有些节点没有跟其他char有字典顺序，也要包含
2. 顺序无效的条件是最后拓扑顺序的节点个数 小于 之前所有节点个数，因为有些有相互依赖关系，没有进queue
3. 这里可能有多个有效的字母顺序，返回以字典顺序看来最小的，这个要求要在同时indegree = 0的节点按照正常字典顺序排序
所以不能正常使用拓扑排序用的queue，而是使用heap，来选择下一个node

Time: O(n) 访问每个词的每个char + O(nlogn) heapsort
Space: O(n) 每个char

Corner cases:
"""

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        g = self._build_graph(words)
        return self._get_topo_order(g)

    def _build_graph(self, words):
        # build g = {}, where
        # key is char, value: set of char it points to
        # for char cannot find relationship to other chars, its neighbor = {}
        g = {}
        for word in words:
            for c in word:
                g[c] = set()

        for i in range(1, len(words)):
            for j in range(min(len(words[i]), len(words[i - 1]))):
                if words[i][j] != words[i - 1][j]:
                    g[words[i - 1][j]].add(words[i][j])
                    break
        return g

    def _get_topo_order(self, g):
        from collections import deque
        from heapq import heapify, heappush, heappop
        # key: char, value: number of indegree to this char
        indegree = {}
        # init indegree
        for node in g:
            if node not in indegree:
                indegree[node] = 0
            for nei in g[node]:
                ind = indegree.get(nei, 0)
                indegree[nei] = ind + 1

        # q = deque([node for node in g if indegree[node] == 0])
        q = [node for node in g if indegree[node] == 0]
        heapify(q)
        topo_order = ""
        while q:
            # cur_node = q.popleft()
            cur_node = heappop(q)
            topo_order += cur_node
            for nei in g[cur_node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    # q.append(nei)
                    heappush(q, nei)

        if len(topo_order) == len(g):
            return topo_order
        else:
            return ""

# Test Cases
if __name__ == "__main__":
    solution = Solution()
