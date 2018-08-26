#! /usr/local/bin/python3

# https://lintcode.com/problem/k-edit-distance/description
# Example
# Given a set of strings which just has lower case letters and a target string, output all the strings for each the edit distance with the target no greater than k.

# You have the following 3 operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
# Example
# Given words = ["abc", "abd", "abcd", "adc"] and target = "ac", k = 1
# Return ["abc", "adc"]

"""
Algo: 匹配DP
D.S.: trie-tree dp

Solution:
#TODO: 重新好好写
Corner cases:
"""

class TrieNode:
    def __init__(self):
        # Initialize your data structure here.
        self.children = [None for i in range(26)]
        self.hasWord = False
        self.str = None

    @classmethod
    def addWord(cls, root, word):
        node = root
        for letter in word:
            child = node.children[ord(letter) - ord('a')]
            if child is None:
                child = TrieNode()
                node.children[ord(letter) - ord('a')] = child
            node = child

        node.hasWord = True
        node.str = word
class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """
    def kDistance(self, words, target, k):
        root = TrieNode()
        for word in words:
            TrieNode.addWord(root, word)

        result = []
        n = len(target)
        dp = [i for i in range(n + 1)]

        self.find(root, result, k, target, dp)
        return result

    def find(self, node, result, k, target, dp):
        n = len(target)

        if node.hasWord and dp[n] <= k:
            result.append(node.str)

        next = [0 for i in range(n + 1)]

        for i in range(26):
            if node.children[i] is not None:
                next[0] = dp[0] + 1
                for j in range(1, n + 1):
                    if ord(target[j - 1]) - ord('a') == i:
                        next[j] = min(dp[j - 1], min(next[j - 1] + 1, dp[j] + 1))
                    else:
                        next[j] = min(dp[j - 1] + 1, min(next[j - 1] + 1, dp[j] + 1))

                self.find(node.children[i], result, k, target, next)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
