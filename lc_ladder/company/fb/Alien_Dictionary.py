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

from heapq import heappush, heappop, heapify
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        out_map, in_degree = self._build_order(words)
        if not out_map or not in_degree:
            return ''

        q = []
        for char, degree in in_degree.items():
            if degree == 0:
                q.append(char)
        heapify(q)

        res = ''
        while q:
            cur = heappop(q)
            res += cur
            for nei in out_map[cur]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    heappush(q, nei)
        if len(res) == len(out_map):
            return res
        return ''

    def _build_order(self, words):
        out_map = {} # key: char, val: set(next char)
        in_degree = {} # key: char, val: in_degree value
        # init value
        for w in words:
            for c in w:
                if c not in out_map:
                    out_map[c] = set()
                if c not in in_degree:
                    in_degree[c] = 0

        for i in range(1, len(words)):
            w1 = words[i - 1] + ' '
            w2 = words[i] + ' '
            for k in range(min(len(w1), len(w2)) + 1):
                if w1[k] == ' ':
                    break
                if w2[k] == ' ':
                    return None, None
                if w1[k] != w2[k]:
                    if w2[k] not in out_map[w1[k]]:
                        out_map[w1[k]].add(w2[k])
                        in_degree[w2[k]] += 1
                    break # break inner for loop
        return out_map, in_degree
                    
# Test Cases
if __name__ == "__main__":
    solution = Solution()
