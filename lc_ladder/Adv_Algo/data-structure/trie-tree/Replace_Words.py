#! /usr/local/bin/python3

# https://leetcode.com/problems/replace-words/
# Example
# In English, we have a concept called root, which can be followed by some other words to form another longer word -
# let's call this word successor. For example, the root an, followed by other, which can form another word another.
#
# Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor
# in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.
#
# You need to output the sentence after the replacement.
#
# Example 1:
#
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
#
#
# Note:
#
# The input will only have lower-case letters.
# 1 <= dict words number <= 1000
# 1 <= sentence words number <= 1000
# 1 <= root length <= 100
# 1 <= sentence words length <= 1000
"""
Algo:
D.S.: Trie

Solution:
灵活使用TrieNode 的标记

Corner cases:
"""

class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {} # key: val,  val: TrieNode(val)
        self.is_word = None

class TrieTree:
    def __init__(self):
        self.root = TrieNode("*")

    def add(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        cur.is_word = word

    def get_root(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return None
            cur = cur.children[char]
            if cur.is_word:
                return cur.is_word
        return cur.is_word

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        if not dict:
            return sentence

        trie = TrieTree()
        for word in dict:
            trie.add(word)

        word_list = sentence.split()
        for i in range(len(word_list)):
            word_root = trie.get_root(word_list[i])
            if word_root:
                word_list[i] = word_root
        return " ".join(word_list)

# Test Cases
if __name__ == "__main__":
    s = Solution()
