#! /usr/local/bin/python3

# https://leetcode.com/problems/number-of-matching-subsequences/
# Example
# Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.
#
# Example :
# Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
# Note:
#
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
"""
Algo: Map, binary Search
D.S.:

Solution:
1. 暴力算法会超时
前提： S很长，每次去扫一遍S 非常费时

2. 为了重复利用S构造 map
S: 'acbca'
mp: {
    'a': [0, 4],
    'b': [2],
    'c': [1, 3]
}
["bb", "acc"]

Corner cases:
"""

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        if not S or not words: return 0

        idx_mp = {} # key: char, val: [idx of char in S]
        for i, char in enumerate(S):
            if char not in idx_mp:
                idx_mp[char] = []
            idx_mp[char].append(i)
        # print(idx_mp)

        res = 0
        for word in words:
            if self.isSubSequence(word, idx_mp):
                # print(word)
                res += 1
        return res

    def isSubSequence(self, word, idx_mp):
        prev = -1
        for char in word:
            # char has idx range[l, r]
            # find the leftmost char idx that is greater than or equal to prev + 1
            if char not in idx_mp:
                return False
                # 注意这里应该是 prev + 1
            left_most_idx = bisect.bisect_left(idx_mp[char], prev + 1)
            if left_most_idx == len(idx_mp[char]):
                return False
            else:
                prev = idx_mp[char][left_most_idx]
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
