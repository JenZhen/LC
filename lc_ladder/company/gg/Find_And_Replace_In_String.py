#! /usr/local/bin/python3

# https://leetcode.com/problems/find-and-replace-in-string/solution/
# Example
# All these operations occur simultaneously.  It's guaranteed that there won't be any overlap in replacement:
# for example, S = "abc", indexes = [0, 1], sources = ["ab","bc"] is not a valid test case.
#
# Example 1:
#
# Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
# Output: "eeebffff"
# Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
# "cd" starts at index 2 in S, so it's replaced by "ffff".
# Example 2:
#
# Input: S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
# Output: "eeecd"
# Explanation: "ab" starts at index 0 in S, so it's replaced by "eee".
# "ec" doesn't starts at index 2 in the original S, so we do nothing.
# Notes:
#
# 0 <= indexes.length = sources.length = targets.length <= 100
# 0 < indexes[i] < S.length <= 1000
# All characters in given inputs are lowercase letters.
"""
Algo: String manipulation
D.S.:

Solution:
Time: O(N * len(word in sources))
Space: O(len(sources))

Corner cases:
"""
class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        if not S or not indexes or not sources: return S
        replace_map = {} # (key: start, val: (length, replacement_string))
        for i in range(len(indexes)):
            idx = indexes[i]
            src = sources[i]
            is_match = True
            for j in range(len(src)):
                if S[idx + j] != src[j]:
                    is_match = False
                    break
            if is_match:
                replace_map[idx] = (len(src), targets[i])
        print(replace_map)
        res = ''
        i = 0
        while i < len(S):
            if i not in replace_map:
                res += S[i]
                i += 1
            else:
                length, string = replace_map[i]
                res += string
                i += length
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
