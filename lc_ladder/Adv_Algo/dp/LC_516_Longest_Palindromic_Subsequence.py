#! /usr/local/bin/python3

# https://leetcode.com/problems/longest-palindromic-subsequence/submissions/
# Example
# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
# Input:
# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
#
# Example 2:
# Input:
# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".
#
# Constraints:
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
"""
Algo: Match DP
D.S.:

Solution:
Time: O(n ^ 2)
Space: O(n ^ 2)

Corner cases:
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.helper(s, s[::-1])

    def helper(self, s, revs):
        f = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        for i in range(1, len(s) + 1):
            for j in range(1, len(s) + 1):
                if s[i - 1] == revs[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])
        return f[-1][-1]
# Test Cases
if __name__ == "__main__":
    solution = Solution()
