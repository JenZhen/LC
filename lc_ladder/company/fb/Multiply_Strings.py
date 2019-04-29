#! /usr/local/bin/python3

# https://www.lintcode.com/problem/multiply-strings/description
# Example
# 以字符串的形式给定两个非负整数 num1 和 num2，返回 num1 和 num2 的乘积。
#
# 样例
# 样例1
#
# 输入：
# "123"
# "45"
# 输出：
# "5535"
# 解释：
# 123 x 45 = 5535
# 样例2
#
# 输入：
# "0"
# "0"
# 输出：
# "0"
# 注意事项
# num1 和 num2 的长度都小于110。
# num1 和 num2 都只包含数字 0 - 9。
# num1 和 num2 都不包含任意前导零。
# 您不能使用任何内置的BigInteger库内方法或直接将输入转换为整数。

"""
Algo:
D.S.:

Solution:

Corner cases:
"""

class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return product of num1 and num2
    """
    def multiply(self, num1, num2):
        # write your code here
        if not num1 or not num2:
            return 0

        sml, lge = None, None
        if len(num1) < len(num2):
            sml, lge = num1, num2
        else:
            sml, lge = num2, num1
        sml = sml[::-1]

        res = 0
        for i in range(len(sml)):
            res += self.time(lge, sml[i]) * (10 ** i)
        return str(res)

    def time(self, num, dgt):
        res = ""
        carry = 0
        num = num[::-1]
        for ele in num:
            m = int(dgt) * int(ele) + carry
            res = str(m % 10) + res
            carry = m // 10
        if carry:
            res = str(carry) + res
        return int(res)


# Test Cases
if __name__ == "__main__":
    solution = Solution()
