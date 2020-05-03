#! /usr/local/bin/python3

# https://leetcode.com/problems/decode-ways/
# Example
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

"""
Algo: DP
D.S.:

Solution:
要特殊考虑 ‘0’的情况
Time: O(len(s))
Space: O(len(s)) 或是滚动变为O(1)
Corner cases:
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1:
            return 0 if s[0] == '0' else 1

        f = [0 for _ in range(len(s) + 1)]
        # init f[0] and f[1]
        f[0] = 1
        if '1' <= s[0] <= '9':
            f[1] = 1

        for i in range(2, len(s) + 1):
            if '1' <= s[i - 1] <= '9':
                f[i] += f[i - 1]
            if 10 <= int(s[i - 2: i]) <= 26:
                f[i] += f[i - 2]
        print(f)
        return f[-1]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
