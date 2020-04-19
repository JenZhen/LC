#!/usr/local/bin/python3

# https://leetcode.com/problems/sort-characters-by-frequency/
# Example
# Given a string, sort it in decreasing order based on the frequency of characters.
#
# Example 1:
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:
#
# Input:
# "Aabb"
#
# Output:
# "bbAa"
#
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

"""
Algo: sorting
D.S.:

Solution1:
Time: O(nlogn), where n is # of different char
Space: O(n)

Solution2:
bucket sort
Time: O(n), where n is length of s
Space: O(n)

Corner cases:
"""

class Solution1:
    def frequencySort(self, s: str) -> str:
        freqMap = {}
        for char in s:
            if char not in freqMap:
                freqMap[char] = 0
            freqMap[char] += 1

        li = []
        for key, freq in freqMap.items():
            li.append((freq, key))
        li.sort(key = lambda x: (-x[0], x[1]))
        print(li)
        res = ""
        for freq, key in li:
            res += key * freq
        return res


class Solution2:
    def frequencySort(self, s: str) -> str:
        # idx: ord(char), val: freq
        freq_list = [0] * 256
        for c in s:
            freq_list[ord(c)] += 1

        # idx: freq, val: list of char ordered by alph
        char_list = [[] for _ in range(max(freq_list) + 1)]

        for i in range(256):
            if freq_list[i] > 0:
                char_list[freq_list[i]].append(chr(i))

        res = ""
        # 倒着树 从高频到低频
        for i in range(len(char_list) - 1, -1, -1):
            if len(char_list[i]) > 0:
                for c in char_list[i]:
                    res += i * c
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
