#! /usr/local/bin/python3

# https://leetcode.com/problems/expressive-words/submissions/
# Example
# Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".
# In these strings like "heeellooo", we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".
# For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation:
# choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.
#
# For example, starting with "hello", we could do an extension on the group "o" to get "hellooo",
# but we cannot get "helloo" since the group "oo" has size less than 3.
# Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".
# If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.
#
# Given a list of query words, return the number of words that are stretchy.
#
# Example:
# Input:
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation:
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
#
# Notes:
#
# 0 <= len(S) <= 100.
# 0 <= len(words) <= 100.
# 0 <= len(words[i]) <= 100.
# S and all words in words consist only of lowercase letters
"""
Algo: mapping
D.S.:

Solution:
Time: O(len(word) * len(S))
Space: O(len(S))

Corner cases:
1. 'aaa' ['aaaa']
2. "zzzzzyyyyy" ["zzyy","zy","zyy"]
"""

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        stre_s = self.get_stretchy(S)
        res = 0
        for w in words:
            stre_w = self.get_stretchy(w)
            if self.is_match(stre_w, stre_s):
                res += 1
        return res

    def get_stretchy(self, word):
        # pass
        word += '*'
        res = []
        i, j = 0, 0
        while j < len(word):
            if word[i] == word[j]:
                j += 1
            else:
                cnt = j - i
                res.append((word[i], cnt))
                i = j
        return res

    def is_match(self, s1, s2):
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            char1, cnt1, char2, cnt2 = s1[i][0], s1[i][1], s2[i][0], s2[i][1]
            if char1 != char2:
                return False
            if cnt2 < 3 and cnt1 != cnt2:
                return False
            if cnt1 > cnt2:
                return False
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
