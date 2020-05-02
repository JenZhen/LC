#! /usr/local/bin/python3

# https://leetcode.com/problems/first-unique-character-in-a-string/
# Example
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
"""
Algo:
D.S.: map

Solution:
注意 如果没有FIRST 要返回-1

Time: O(n)
Space: O(n)
Corner cases:
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        idx_map = {} # key: char, val: [idx]
        for i in range(len(s)):
            char = s[i]
            if char not in idx_map:
                idx_map[char] = []
            idx_map[char].append(i)
        first = len(s)
        for char, idx_list in idx_map.items():
            if len(idx_list) == 1:
                first = min(first, idx_list[0])
        return -1 if first == len(s) else first

# Test Cases
if __name__ == "__main__":
    solution = Solution()
