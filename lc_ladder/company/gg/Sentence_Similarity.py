#! /usr/local/bin/python3

# https://leetcode.com/problems/sentence-similarity/
# Given two sentences words1, words2 (each represented as an array of strings),
# and a list of similar word pairs pairs, determine if two sentences are similar.
#
# For example, "great acting skills" and "fine drama talent" are similar,
# if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].
#
# Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar,
# and "fine" and "good" are similar, "great" and "good" are not necessarily similar.
#
# However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.
# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"],
# pairs = [] are similar, even though there are no specified similar word pairs.
#
# Finally, sentences can only be similar if they have the same number of words.
# So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].
#
# Note:
#
# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""
Algo:
D.S.:

Solution:
注意：
words 里的词有可能不在 pair 中！
如果word 不在pair 中，但是是相同的，也是可以


Corner cases:
"""
class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        mp = {} # key: word, val: set(words it is similar to)
        for u, v in pairs:
            s_u = mp.get(u, set())
            s_u.add(v)
            mp[u] = s_u
            s_v = mp.get(v, set())
            s_v.add(u)
            mp[v] = s_v
        print(mp)
        for i in range(len(words1)):
            w1, w2 = words1[i], words2[i]
            if w1 != w2 and (w1 not in mp or w2 not in mp[w1]):
                return False
        return True
# Test Cases
if __name__ == "__main__":
    solution = Solution()
