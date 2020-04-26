#! /usr/local/bin/python3

# https://leetcode.com/problems/palindrome-pairs/submissions/
# Example
# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
# so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
#
# Example 1:
#
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# Example 2:
#
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
"""
Algo:
D.S.: Trie

Solution:
A <-> ""A ; A""
CAT <-> CAT + TAC; CAT + AC; TAC + CAT; TA + CAT
SOLOSTAC <-> CAT + SOLOSTAC;
CATSOLOS <-> CATSOLOS + TAC

注意一个特殊情况
“a”, ""  <-> 空串可以在左 或在右
Corner cases:
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = None
class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word, idx):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.idx = idx

    def find(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return None
            cur = cur.children[c]
        return cur.idx

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = TrieTree()
        for i in range(len(words)):
            trie.add(words[i], i)

        res = []
        for i in range(len(words)):
            w = words[i]
            for k in range(len(w) + 1):
                # left string range from "" to full w string
                left = w[:k]
                right = w[k:]
                if self.is_pal(left):
                    # if left is palindrome, reverse right, put at left end of w
                    idx = trie.find(right[::-1])
                    if idx is not None and idx != i:
                        res.append([idx, i])
                if len(right) > 0 and self.is_pal(right):
                    # right is non-empty and is palindrome
                    # reverse left, put at right end of w
                    idx = trie.find(left[::-1])
                    if idx is not None and idx != i:
                        res.append([i, idx])

        return res

    def is_pal(self, w):
        return w == w[::-1]

class Solution_TLE:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if self.valid(words[i] + words[j]):
                        res.append([i, j])
        return res

    def valid(self, w):
        return w == w[::-1]

# Test Cases
if __name__ == "__main__":
    s = Solution()
