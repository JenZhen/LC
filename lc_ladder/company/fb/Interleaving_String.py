#! /usr/local/bin/python3

# https://leetcode.com/problems/interleaving-string/submissions/
# Example
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#
# Example 1:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
"""
Algo:
D.S.:

Solution:
prefix padding

Time: O(mn) length of s1 * length of s2
Space: O(mn)
Corner cases:
"""

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        m, n = len(s1), len(s2)
        f = [[True for _ in range(n + 1)] for _ in range(m + 1)]

        # init first row
        for j in range(1, n + 1):
            f[0][j] = f[0][j - 1] and s2[j - 1] == s3[j - 1]

        # init first col
        for i in range(1, m + 1):
            f[i][0] = f[i - 1][0] and s1[i - 1] == s3[i - 1]

        # dp inner logic
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = (f[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (f[i - 1][j] and s1[i - 1] == s3[i + j - 1])

        return f[m][n]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
