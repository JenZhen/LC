#! /usr/local/bin/python3

# https://www.lintcode.com/problem/add-binary/description
# Example
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 样例
# 样例 1：
#
# 输入：
# a = "0", b = "0"
# 输出：
# "0"
# 样例 2：
#
# 输入：
# a = "11", b = "1"
# 输出：
# "100"

"""
Algo:
D.S.:

Solution:
K decimal addition simplified version

Corner cases:
没有前置0的特殊情况

"""

class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        # write your code here
        ll = a if len(a) >= len(b) else b
        ss = a if len(a) < len(b) else b
        pl = len(ll) - 1
        ps = len(ss) - 1
        res = ""
        carry = 0
        while ps >= 0:
            ttl = int(ll[pl]) + int(ss[ps]) + carry
            digi = ttl % 2
            carry = ttl // 2
            res = str(digi) + res
            pl -= 1
            ps -= 1

        while pl >= 0:
            ttl = int(ll[pl]) + carry
            digi = ttl % 2
            carry = ttl // 2
            res = str(digi) + res
            pl -= 1

        if carry:
            res = str(carry) + res
        return res


# Test Cases
if __name__ == "__main__":
    solution = Solution()
