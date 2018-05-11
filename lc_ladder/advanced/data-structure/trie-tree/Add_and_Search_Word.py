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


Corner cases:
"""

class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    def addWord(self, word):
        # write your code here

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # write your code here


# Test Cases
if __name__ == "__main__":
    s = Solution()
