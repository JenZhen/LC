#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo: UnionFind
D.S.:

Solution:


Corner cases:
"""

class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        pairs_set = set()
        for u, v in pairs:
            pairs_set.add(u)
            pairs_set.add(v)

        uf = UF(pairs_set)
        for u, v in pairs:
            uf.union(u, v)
        for i in range(len(words1)):
            w1, w2 = words1[i], words2[i]
            if w1 == w2: continue
            # 这里很重要，一定要先查word是否在pair中，才能再进uf find root
            if w1 not in pairs_set or w2 not in pairs_set:
                return False
            if not uf.is_similar(w1, w2):
                return False
        return True

class UF:
    def __init__(self, pairs_set):
        self.father = {} # key: word, val: it's father

        for u in pairs_set:
            if u not in self.father:
                self.father[u] = u

    def _get_root(self, a):
        if self.father[a] != a:
            self.father[a] = self._get_root(self.father[a])
        return self.father[a]

    def union(self, u, v):
        root_u = self._get_root(u)
        root_v = self._get_root(v)
        if root_u != root_v:
            self.father[root_u] = root_v

    def is_similar(self, u, v):
        root_u = self._get_root(u)
        root_v = self._get_root(v)
        return root_u == root_v

# Test Cases
if __name__ == "__main__":
    solution = Solution()
