#!/usr/bin/python

# http://lintcode.com/en/problem/top-k-frequent-words/
# Example

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
