#! /usr/local/bin/python3

# https://www.lintcode.com/problem/add-and-search-word-data-structure-design/description
# Design a data structure that supports the following two operations: addWord(word) and search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or ..
# A . means it can represent any one letter.
# Note: You may assume that all words are consist of lowercase letters a-z.

# Example
"""
addWord("bad")
addWord("dad")
addWord("mad")
search("pad")  // return false
search("bad")  // return true
search(".ad")  // return true
search("b..")  // return true
"""

"""
Algo:
D.S.: TrieTree

Solution:
1. Trie Tree
Time: O(m), m is the max length of a word

2. Hashmap with DFS #TODO:

Corner cases:
"""

class TrieNode(object):
    def __init__(self, char):
        self.char = char # unncessary
        self.children = [None] * 26
        self.isWordEnd = False

class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """

    def __init__(self):
        self.root = TrieNode("*")

    def addWord(self, word):
        # write your code here
        if not word:
            return
        cur = self.root
        for char in word:
            pos = ord(char) - ord("a")
            if cur.children[pos] == None:
                cur.children[pos] = TrieNode(char)
            cur = cur.children[pos]
        cur.isWordEnd = True

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # To handle ".", which requires for iterating all possible 26 children, then trace back -- DFS
        #                             depth(pos in word)
        res = self._search(word, 0, self.root)
        print("Search result: %s" %res)
        return res

    def _search(self, word, depth, curNode):
        if depth == len(word):
            return curNode.isWordEnd

        char = word[depth]
        if char == ".":
            for child in curNode.children:
                if child is not None:
                    if self._search(word, depth + 1, child):
                        return True
            return False # Be careful where this return is!
        elif curNode.children[ord(char) - ord("a")] != None:
            return self._search(word, depth + 1, curNode.children[ord(char) - ord("a")])
        else:
            return False



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
    s1 = WordDictionary()
    s1.addWord("bad"),
    s1.addWord("dad"),
    s1.addWord("mad"),
    s1.search("pad"),  # return false
    s1.search("bad"),  # return true
    s1.search(".ad"),  # return true
    s1.search("b..")   # return true
