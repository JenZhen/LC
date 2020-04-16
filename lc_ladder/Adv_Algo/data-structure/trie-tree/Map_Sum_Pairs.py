#! /usr/local/bin/python3

# https://leetcode.com/problems/map-sum-pairs/
# Example
# Implement a MapSum class with insert, and sum methods.
#
# For the method insert, you'll be given a pair of (string, integer).
# The string represents the key and the integer represents the value.
# If the key already existed, then the original key-value pair will be overridden to the new one.
#
# For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.
#
# Example 1:
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5

"""
Algo:
D.S.: Trie + DFS
找到prefix 后 DFS 下面的可能解

Solution:


Corner cases:
"""

class TrieNode:
    def __init__(self):
        self.children = {} # key: char, val: TrieNode
        self.val = None

class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word, val):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.val = val

    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        # start dfs from cur
        sum = [0] # 用list比用INTEGER 方便
        self._dfs(cur, sum)
        return sum[0]

    def _dfs(self, node, sum):
        if node.val is not None:
            sum[0] += node.val
        for char, n in node.children.items():
            self._dfs(n, sum)

class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieTree()

    def insert(self, key: str, val: int) -> None:
        self.trie.add(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.sum(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

# Test Cases
if __name__ == "__main__":
    s = Solution()
