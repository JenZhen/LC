#!/usr/bin/python

# http://lintcode.com/en/problem/top-k-frequent-words/
# https://leetcode.com/problems/top-k-frequent-words/
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
Algo: heap sort comparator
D.S.:

Solution:
一定更要会写comparator
TODO: python 的各种sort
- built-in sorted(list, key: )
- list.sort(cmp=comparator)

Solution2:
heap sort 排序
如果是MIN HEAP FREQ 升序，WORD 也是升序
如果用positive freq:
[(1, 'a'), (1, 'day'), (2, 'sunny'), (3, 'is'), (4, 'the')]
如果用negative freq:
[(-4, 'the'), (-3, 'is'), (-1, 'a'), (-1, 'day'), (-2, 'sunny')]
区别在于相同freq的Word 排序

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


class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from heapq import heappush, heappop, heapify
        count = collections.Counter(words)
        # heap: min heap, freq 升序 Word 也是升序 Time：O(nlogn)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


# Test Cases
if __name__ == "__main__":
	solution = Solution()
