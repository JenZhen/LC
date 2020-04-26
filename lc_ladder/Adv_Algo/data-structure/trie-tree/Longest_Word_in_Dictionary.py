#! /usr/local/bin/python3

# https://leetcode.com/problems/longest-word-in-dictionary/
# Example
# Given a list of strings words representing an English Dictionary,
# find the longest word in words that can be built one character at a time by other words in words.
# If there is more than one possible answer, return the longest word with the smallest lexicographical order.
#
# If there is no answer, return the empty string.
# Example 1:
# Input:
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation:
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:
# Input:
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation:
# Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
# Note:
#
# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].
"""
Algo:
D.S.: Trie

Solution:
这个题 意图有些怪

重点在于先将所有的词按照词长排序


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
        # given a word, add it to trie
        # return if could be build step by step
        cur = self.root
        flag = True
        # 注意 词的最后一个位置可以不标记，所以要考虑到WORD[:-1]的位置
        for i in range(len(word) - 1):
            char = word[i]
            if char not in cur.children:
                flag = False
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
            if not cur.is_end:
                flag = False
        # 额外考虑词的最后一个字符
        last_char = word[-1]
        if last_char not in cur.children:
            cur.children[last_char] = TrieNode(last_char])
        cur = cur.children[last_char]
        cur.is_end = True
        # 注意 如果 单词只有一个字母， 也就不是从前一个变来的，总要返回true
        return True if len(word) == 1 else flag

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # 先按次长 再按词的字幕顺序排序
        words.sort(key = lambda x: (len(x), x))

        maxWord = None
        maxLen = 0
        trie = TrieTree()
        for word in words:
            can_build = trie.add(word)
            if can_build:
                if len(word) > maxLen:
                    maxLen = len(word)
                    maxWord = word
                if len(word) == maxLen and word < maxWord:
                    maxWord = word
        return maxWord

# Test Cases
if __name__ == "__main__":
    s = Solution()
