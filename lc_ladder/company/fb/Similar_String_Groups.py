#! /usr/local/bin/python3

# https://leetcode.com/problems/similar-string-groups/
# Example

"""
Algo:
D.S.:

Solution:
Basic
Time: O(N^2 * M) N words in the list, M is word length
anagram possible : M!
Space: O(N)
Corner cases:
"""

class Solution2_Improve:
    def numSimilarGroups(self, A: List[str]) -> int:
        A.sort()
        k = 0
        for i in range(len(A)):
            if i > 0 and A[i] == A[i - 1]:
                continue
            A[k] = A[i]
            k += 1

        uf = UnionFind(k) # elements are 0 - len(A) - 1
        for i in range(k):
            for j in range(i + 1, k):
                w1 = A[i]
                w2 = A[j]
                if self._is_similar(w1, w2):
                    uf.union(i, j)
        return uf.group

    def _is_similar(self, w1, w2):
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
                if diff > 2:
                    return False
        return True

class UnionFind:
    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.group = n

    def find(self, i):
        if i == self.father[i]:
            return i
        self.father[i] = self.find(self.father[i])
        return self.father[i]

    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota != rootb:
            self.father[roota] = rootb
            self.group -= 1


class Solution1_Basic:
    def numSimilarGroups(self, A: List[str]) -> int:
        uf = UnionFind(len(A)) # elements are 0 - len(A) - 1
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                w1 = A[i]
                w2 = A[j]
                if self._is_similar(w1, w2):
                    uf.union(i, j)
        return uf.group

    def _is_similar(self, w1, w2):
        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
                if diff > 2:
                    return False
        return True

class UnionFind:
    def __init__(self, n):
        self.father = [i for i in range(n)]
        self.group = n

    def find(self, i):
        if i == self.father[i]:
            return i
        self.father[i] = self.find(self.father[i])
        return self.father[i]

    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota != rootb:
            self.father[roota] = rootb
            self.group -= 1


# Test Cases
if __name__ == "__main__":
    solution = Solution()
