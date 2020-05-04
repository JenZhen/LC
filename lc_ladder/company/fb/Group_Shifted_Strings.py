#! /usr/local/bin/python3

# https://leetcode.com/problems/group-shifted-strings/submissions/
# Example
# Given a string, we can "shift" each of its letter to its successive letter,
# for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
#
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
#
# Example:
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output:
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]
"""
Algo: chr() ord()
D.S.:

Solution:
rebase string
每个string rebase 到第一个字母为'a'
'a' -> 0
'z' -> 25
超过25 要 % 26
xyz --> abc
Time: O(N) --length of strings
Space: O(N) -- size of map
Corner cases:
"""

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if not strings or len(strings) == 1: return strings
        mp = {} # key: based_on_a, val: [list of origin string]
        for s in strings:
            key = self._rebase(s)
            if key not in mp:
                mp[key] = []
            mp[key].append(s)
        res = []
        for key, arr_list in mp.items():
            res.append(arr_list)
        return res

    def _rebase(self, s):
        if s[0] == 'a':
            return s
        base = ord('a')
        diff = ord('z') + 1 - ord(s[0])
        new_s = ''
        for i in range(len(s)):
            new_s += chr(base + (ord(s[i]) - base + diff) % 26)
        return new_s

# Test Cases
if __name__ == "__main__":
    solution = Solution()
