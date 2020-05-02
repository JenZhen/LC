#! /usr/local/bin/python3

# https://leetcode.com/problems/add-and-search-word-data-structure-design/
# Example
# Design a data structure that supports the following two operations:
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.
#
# Example:
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
"""
Algo:
D.S.:

Solution:

Time: O()
Space: O()
Corner cases:
"""

class TrieNode:
    def __init__(self, char):
        self.char = char # unncessary
        self.children = {} # key char, value trie node
        self.isWordEnd = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode("*")

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        cur.isWordEnd = True

    def search(self, word: str) -> bool:
        res = self._search(word, 0, self.root)
        return res

    def _search(self, word, depth, curNode):
        if depth == len(word):
            return curNode.isWordEnd

        char = word[depth]
        if char == ".":
            for key, node in curNode.children.items():
                if self._search(word, depth + 1, node):
                    return True
            return False # Be careful where this return is!
        elif char in curNode.children:
            return self._search(word, depth + 1, curNode.children[char])
        else:
            return False
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
