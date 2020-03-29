#! /usr/local/bin/python3

# https://www.lintcode.com/en/old/problem/implement-trie-prefix-tree/
# Implement a trie with insert, search, and startsWith methods.
# Note: You may assume that all inputs are consist of lowercase letters a-z.
# Example
"""
insert("lintcode")
search("code")
>>> false
startsWith("lint")
>>> true
startsWith("linterror")
>>> false
insert("linterror")
search("lintcode)
>>> true
startsWith("linterror")
>>> true
"""

"""
Algo:
D.S.: TrieTree

Solution:
Time: O(m), m is the max length of a word

Corner cases:
"""

class TrieNode(object):
    def __init__(self, char):
        self.char = char # unncessary
        # [None] * 26 is for alphabet only
        # use self.children = {} dictionary/hashmap for wider range of char
        self.children = [None] * 26
        self.isWordEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
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
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        if not word:
            return False
        cur = self.root
        for char in word:
            # IMPORTANT:
            # Iteration -- 当前curNode 的孩子有没有char
            # char 的次序from 0->n-1
            # When 次序便利到n = len(word) meaning word is found
            pos = ord(char) - ord("a")
            if cur.children[pos] == None:
                return False
            cur = cur.children[pos]
        return cur.isWordEnd

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        if not prefix:
            return False
        cur = self.root
        for char in prefix:
            pos = ord(char) - ord("a")
            if cur.children[pos] == None:
                return False
            cur = cur.children[pos]
        return True


# children using dictionary
class TrieNode2(object):
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.isWordEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode("*")

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        if not word:
            return
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        cur.isWordEnd = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        if not word:
            return False
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.isWordEnd

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        if not prefix:
            return False
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True

# Test Cases
if __name__ == "__main__":
    trie = Trie()
