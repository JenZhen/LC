#! /usr/local/bin/python3

# https://www.lintcode.com/problem/longest-repeating-subsequence/description
# Example
# Given a string, find length of the longest repeating subsequence such that the two subsequence
# don’t have same string character at same position, i.e., any ith character in the two subsequences shouldn’t have the same index in the original string.
#
# Example
# str = abc, return 0, There is no repeating subsequence
#
# str = aab, return 1, The two subsequence are a(first) and a(second).
# Note that b cannot be considered as part of subsequence as it would be at same index in both.
#
# str = aabb, return 2

"""
Algo:
D.S.:

Solution:

Solution1:
Time O(n^2), Space O(n^2)

Solution2:
Time O(n^2), Space O(n)


Corner cases:
"""
class Solution1:
    """
    @param str: a string
    @return: the length of the longest repeating subsequence
    """
    def longestRepeatingSubsequence(self, str):
        # write your code here
        if not str:
            return 0
        n = len(str)
        f = [[0 for j in range (n + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if str[i - 1] == str[j - 1] and i != j:
                    f[i][j] = f[i - 1][j - 1] + 1
                else:
                    f[i][j] = max(f[i][j - 1], f[i - 1][j])

        return f[n][n]

class Solution2:
    """
    @param str: a string
    @return: the length of the longest repeating subsequence
    """
    def longestRepeatingSubsequence(self, str):
        # write your code here
        if not str:
            return 0
        n = len(str)
        f = [[0 for j in range (n + 1)] for i in range(2)]
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if str[i - 1] == str[j - 1] and i != j:
                    f[i % 2][j] = f[(i - 1) % 2][j - 1] + 1
                else:
                    f[i % 2][j] = max(f[i % 2][j - 1], f[(i - 1) % 2][j])
                #res = max(res, f[i][j]) # useless, since it's always increaseing, f[n][n] is max
        return f[n % 2][n]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
