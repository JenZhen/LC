#! /usr/local/bin/python3

# https://www.lintcode.com/problem/decode-ways/description
# Example
# 有一个消息包含A-Z通过以下规则编码
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 现在给你一个加密过后的消息，问有几种解码的方式
#
# 样例
# 样例 1:
#
# 输入: "12"
# 输出: 2
# 解释: 它可以被解码为 AB (1 2) 或 L (12).
# 样例 2:
#
# 输入: "10"
# 输出: 1

"""
Algo: DP
D.S.:

Solution:
直观第一反应是dfs 讨论各种情况，但是复杂度太高，选用dp
f[i]: 前i个字符能有几种方法
init f[0] = 1, f[i] = 1 or 0 取决于s第一位是不是有效，即是不是0
f[i] = f[i - 1] + f[i - 2]
选用f[i - 1]的条件是这个字符单独有效，ie [1, 9]
选用f[i - 2]的条件是这个字符和前一个拼起来有效，ie [10, 26] 注意 ‘01’ 无效
Corner cases:
"""

class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        if not s:
            return 0
        f = [0] * (len(s) + 1)
        f[0] = 1
        for i in range(1, len(s) + 1):
            if i == 1 and '1' <= s[i - 1] <= '9':
                f[i] = 1
                continue
            if '1' <= s[i - 1] <= '9':
                f[i] += f[i - 1]
            if 10 <= self.sum_pre(s[i - 2], s[i - 1]) <= 26:
                f[i] += f[i - 2]
        print(f)
        return f[len(s)]

    def sum_pre(self, s1, s2):
        return int(s1) * 10 + int(s2)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
