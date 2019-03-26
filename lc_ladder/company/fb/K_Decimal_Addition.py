#! /usr/local/bin/python3

# https://www.lintcode.com/problem/k-decimal-addition/description
# Example
# 给出一个k，a，b，代表a和b都是一个k进制的数，输出a + b的k进制数。
#
# 样例
# 样例1
#
# 输入: k = 3, a = "12", b = "1"
# 输出: 20
# 解释:
# 12 + 1 = 20 in 3 bases.
# 样例2
#
# 输入: k = 10, a = "12", b = "1"
# 输出: 13
# 解释:
# 12 + 1 = 13 in 10 bases.
# 注意事项
# 2 <= k <= 10
# a, b均为字符串，长度不超过1000。
# 可能有前导零

"""
Algo: two pointers
D.S.:

Solution:
Time O(n)

Corner cases:
注意
1. 2个串的长短不一致
2. 处理长串多余的部分
3. 处理最后的carry
4. 可能有前导零 最后需要remove preceding 0s
"""

class Solution:
    """
    @param k: The k
    @param a: The A
    @param b: The B
    @return: The answer
    """
    def addition(self, k, a, b):
        # Write your code here
        ll = a if len(a) >= len(b) else b
        ss = a if len(a) < len(b) else b
        pl = len(ll) - 1
        ps = len(ss) - 1
        res = ""
        carry = 0
        while ps >= 0:
            ttl = int(ll[pl]) + int(ss[ps]) + carry
            digi = ttl % k
            carry = ttl // k
            res = str(digi) + res
            pl -= 1
            ps -= 1

        while pl >= 0:
            ttl = int(ll[pl]) + carry
            digi = ttl % k
            carry = ttl // k
            res = str(digi) + res
            pl -= 1

        print(carry)
        if carry != 0:
            res = str(carry) + res

        # trunk preceding 0s
        idx = 0
        for idx in range(len(res)):
            if res[idx] != "0":
                break
        return res[idx:]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
