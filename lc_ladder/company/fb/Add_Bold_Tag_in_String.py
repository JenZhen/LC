#! /usr/local/bin/python3

# https://leetcode.com/problems/add-bold-tag-in-string/submissions/
# Example
# Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings 
# in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag.
# Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
# Example 1:
# Input:
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
#
# Example 2:
# Input:
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
#
# Constraints:
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].
# Note: This question is the same as 758: https://leetcode.com/problems/bold-words-in-string/
"""
Algo: merge intervals
D.S.:

Solution:

Time: O(nlogn) -- sorting an array, could be as big as n, size of s
Space: O(n) -- size of intervals

Corner cases:
"""

class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        if not s or not dict: return s

        intervals = [] # intervals of substrings that match the dict
        for word in dict:
            # find all occurrance of word in string, append to intervals
            idx = s.find(word)
            while idx != -1:
                intervals.append([idx, idx+len(word)])
                idx = s.find(word, idx+1)

        # DO NOT FORGET this logic
        intervals.sort(key=lambda x: x[0])
        if not intervals:
            return s

        # Merge intervals
        merged_itvs = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start > merged_itvs[-1][1]:
                merged_itvs.append(intervals[i])
            else:
                merged_itvs[-1][0] = min(merged_itvs[-1][0], start)
                merged_itvs[-1][1] = max(merged_itvs[-1][1], end)

        res = ''
        i = 0
        for start, end in merged_itvs:
            if start > i:
                res += s[i:start]
            res += '<b>' + s[start:end] + '</b>'
            i = end
        res += s[i::]
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
