#! /usr/local/bin/python3

# https://leetcode.com/problems/stream-of-characters/
# Example
# Implement the StreamChecker class as follows:
#
# StreamChecker(words): Constructor, init the data structure with the given words.
# query(letter): returns true if and only if for some k >= 1, the last k characters queried
# (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
#
# Example:
#
# StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
# streamChecker.query('a');          // return false
# streamChecker.query('b');          // return false
# streamChecker.query('c');          // return false
# streamChecker.query('d');          // return true, because 'cd' is in the wordlist
# streamChecker.query('e');          // return false
# streamChecker.query('f');          // return true, because 'f' is in the wordlist
# streamChecker.query('g');          // return false
# streamChecker.query('h');          // return false
# streamChecker.query('i');          // return false
# streamChecker.query('j');          // return false
# streamChecker.query('k');          // return false
# streamChecker.query('l');          // return true, because 'kl' is in the wordlist
#
# Note:
#
# 1 <= words.length <= 2000
# 1 <= words[i].length <= 2000
# Words will only consist of lowercase English letters.
# Queries will only consist of lowercase English letters.
# The number of queries is at most 40000.

"""
Algo:
D.S.: Trie

Solution:
技巧： 倒着录入trie

Corner cases:
"""

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_end = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode("*")

    def add(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        cur.is_end = True

    def find_prefix(self, string):
        cur = self.root
        for char in string:
            if char not in cur.children:
                return False
            cur = cur.children[char]
            if cur.is_end:
                return True
        return False

class StreamChecker:
    def __init__(self, words: List[str]):
        self.maxsize = max([len(w) for w in words])
        self.q = collections.deque([])
        self.trie = TrieTree()

        # add words backward-wise "cd" will be added in as "dc"
        for w in words:
            w = w[::-1]
            self.trie.add(w)

    def query(self, letter: str) -> bool:
        self.q.append(letter)
        if len(self.q) > self.maxsize:
            self.q.popleft()

        string = ""
        for i in range(len(self.q) - 1, -1, -1):
            string += self.q[i]

        return self.trie.find_prefix(string)



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
# Test Cases
if __name__ == "__main__":
    s = Solution()
