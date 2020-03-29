#!/usr/bin/python

# http://lintcode.com/en/problem/top-k-frequent-words/
# Example
# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest.If two words have the same frequency, then the word with the lower alphabetical order comes first.
#
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.

"""
Algo:
D.S.:

Solution:
一定更要会写comparator
TODO: python 的各种sort
- built-in sorted(list, key: )
- list.sort(cmp=comparator)

Corner cases:
"""
def topKFrequentWords(self, words, k):
        # write your code here
        if words is None or len(words) == 0:
            return None
        if k is None or k == 0:
            return []

        # get a dict of freq
        # key: word, val: freq
        freq_dict = {}
        for w in words:
            if w not in freq_dict:
                freq_dict[w] = 1
            else:
                freq_dict[w] += 1

        # prepare a list
        wordList = []
        for key, value in freq_dict.items():
            wordList.append((key, value))

        ########################
        # It's important to write this
        # customized comparator
        ########################
        #
        def comp(a, b):
            if a[1] > b[1] or a[1] == b[1] and a[0] < b[0]:
                return -1
            elif a[1] == b[1] and a[0] == b[0]:
                return 0
            else:
                return 1

        wordList.sort(cmp = comp)
        result = []
        for i in xrange(k):
            result.append(wordList[i][0])
        return result

# Test Cases
if __name__ == "__main__":
	solution = Solution()
