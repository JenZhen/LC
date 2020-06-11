#! /usr/local/bin/python3

# https://leetcode.com/problems/partition-labels/
# Example
# A string S of lowercase letters is given. We want to partition this string into as many parts as possible
# so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
#
# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# Note:
#
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
"""
Algo:
D.S.:

Solution:
有意思

Corner cases:
"""
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        res = []
        curmax, curstart = 0, 0
        for i, c in enumerate(S):
            curmax = max(curmax, last[c])
            if curmax == i:
                res.append(i - curstart + 1)
                curstart = i + 1
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
