#! /usr/local/bin/python3

# https://leetcode.com/problems/decode-ways-ii/
# Example
# A message containing letters from A-Z is being encoded to numbers using the following mapping way:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.
#
# Given the encoded message containing digits and the character '*', return the total number of ways to decode it.
#
# Also, since the answer may be very large, you should return the output mod 109 + 7.
#
# Example 1:
# Input: "*"
# Output: 9
# Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
# Example 2:
# Input: "1*"
# Output: 9 + 9 = 18
# Note:
# The length of the input string will fit in range [1, 105].
# The input string will only contain the character '*' and digits '0' - '9'.
"""
Algo: DP
D.S.:

Solution:
考虑一下情况
- 数数 （其中0是个特殊情况）
- *数
- 数*
- * *
    2个一位数 = 9 * 9 = 81
    1个两位数 = 15 from 11 -> 26 出去 20
Time: O(len(s))
Space: O(len(s)) 或是滚动变为O(1)
Corner cases:
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        f = [0 for _ in range(len(s) + 1)]
        # init f[0] and f[1]
        f[0] = 1
        # f[1] depends on s[0]
        if s[0] == '*': f[1] = 9
        elif s[0] == '0': f[1] = 0
        else: f[1] = 1

        for i in range(2, len(f)):
            if s[i - 1] == '*':
                if s[i - 2] == '0':
                    f[i] += f[i - 1] * 9
                elif s[i - 2] == '1':
                    f[i] += f[i - 1] * 9 + f[i - 2] * 9
                elif s[i - 2] == '2':
                    f[i] += f[i - 1] * 9 + f[i - 2] * 6
                elif '3' <= s[i - 2] <= '9':
                    f[i] += f[i - 1] * 9
                elif s[i - 2] == '*':
                    f[i] += f[i - 1] * 9 + f[i - 2] * 15
            elif s[i - 1] == '0':
                if s[i - 2] == '1' or s[i - 2] == '2':
                    f[i] += f[i - 2]
                elif s[i - 2] == '*':
                    f[i] += f[i - 2] * 2
            else: # s[i - 1] 1 - 9
                f[i] += f[i - 1]
                if s[i - 2] != '*' and 10 <= int(s[i - 2: i]) <= 26:
                    f[i] += f[i - 2]
                if s[i - 2] == '*':
                    if '1' <= s[i - 1] <= '6':
                        f[i] += f[i - 2] * 2
                    else:
                        f[i] += f[i - 2] * 1
        # 注意最后要MOD 否则不能过
        return f[-1] % 1000000007

# Test Cases
if __name__ == "__main__":
    solution = Solution()
