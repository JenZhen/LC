#! /usr/local/bin/python3

# https://leetcode.com/problems/prefix-and-suffix-search/
# Example
# Given many words, words[i] has weight i.
#
# Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix).
# It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.
#
# Examples:
#
# Input:
# WordFilter(["apple"])
# WordFilter.f("a", "e") // returns 0
# WordFilter.f("b", "") // returns -1
#
# Note:
#
# words has length in range [1, 15000].
# For each test case, up to words.length queries WordFilter.f may be made.
# words[i] has length in range [1, 10].
# prefix, suffix have lengths in range [0, 10].
# words[i] and prefix, suffix queries consist of lowercase letters only.
"""
Algo:
D.S.: 2 Trie + 2 Set

Solution:
reverse order for suffix problem

Corner cases:
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = set()

class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def add(self, prefix, word):
        self.root.words.add(word)
        cur = self.root
        # to make "" a prefix, add word to prefix_trie.root words
        self.root.words.add(word)
        for char in prefix:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            cur.words.add(word)

    def find(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return set()
            cur = cur.children[char]
        return cur.words


class WordFilter:
    def __init__(self, words: List[str]):
        self.prefix_trie = TrieTree()
        self.suffix_trie = TrieTree()
        self.weight = {} # key: word, val: weight

        # add words to weight map
        for i in range(len(words)):
            self.weight[words[i]] = i

        # add words to prefix trie
        for i in range(len(words)):
            prefix = words[i]
            self.prefix_trie.add(prefix, words[i])

        # add words to suffix trie
        for i in range(len(words)):
            suffix = words[i][::-1]
            self.suffix_trie.add(suffix, words[i])


    def f(self, prefix: str, suffix: str) -> int:
        prefix_set = self.prefix_trie.find(prefix)
        suffix_set = self.suffix_trie.find(suffix[::-1])
        candidates = prefix_set.intersection(suffix_set)
        res = -1
        for c in candidates:
            res = max(res, self.weight[c])
        return res




# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# Test Cases
if __name__ == "__main__":
    s = Solution()
