#! /usr/local/bin/python3
# FB Interview 两个浮点数相加
#
# 输入：
# a = "0.1", b = "1.23"
# 输出：
# "1.33"
#
# 输入：
# a = "11", b = "1.1"
# 输出：
# "12.1"

"""
Algo:
D.S.:

Solution:
用补0 的方式来对齐
考虑各种情况， 有无整数部分，有无小数部分
最后要trim traling 0s, trailing 最后的那个.

Corner cases:

"""

class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addFloat(self, a, b): # input a, b are string type
        a_point = a.find('.')
        b_point = b.find('.')
        a_int, a_decimal = '', ''
        b_int, b_decimal = '', ''
        if a_point != -1: # if has '.'
            a_int = a[:a_point]
            a_decimal = a[a_point+1:]
        else:
            a_int = a
        if b_point != -1: # if has '.'
            b_int = b[:b_point]
            b_decimal = b[b_point+1:]
        else:
            b_int = b

        if len(a_int) < len(b_int):
            a_int = '0' * (len(b_int) - len(a_int)) + a_int
        elif len(b_int) < len(a_int):
            b_int = '0' * (len(a_int) - len(b_int)) + b_int

        if len(a_decimal) < len(b_decimal):
            a_decimal += '0' * (len(b_decimal) - len(a_decimal))
        elif len(b_decimal) < len(a_decimal):
            b_decimal += '0' * (len(a_decimal) - len(b_decimal))

        carry = 0
        res = ''
        for i in range(len(a_decimal) - 1, -1, -1):
            ttl = int(a_decimal[i]) + int(b_decimal[i]) + carry
            res = str(ttl % 10) + res
            carry = ttl // 10
        # 记着 加上这个‘.’
        res = '.' + res
        for i in range(len(a_int) - 1, -1, -1):
            ttl = int(a_int[i]) + int(b_int[i]) + carry
            res = str(ttl % 10) + res
            carry = ttl // 10
        if carry:
            res = str(carry) + res

        # trim trailing 0s and .
        while res[-1] == '0':
            res = res[:-1]
        if res[-1] == '.':
            res = res[:-1]
        return res

# Test Cases
if __name__ == "__main__":
    testcases = [
        {
        'a': '1.2',
        'b': '1.3'
        }, # 2.5
        {
        'a': '1',
        'b': '1.30'
        }, # 2.3
        {
        'a': '1.2',
        'b': '.3'
        }, # 1.5
        {
        'a': '21.2',
        'b': '1.33'
        }, # 22.53
        {
        'a': '1.28',
        'b': '1.22'
        }, # 2.5
        {
        'a': '11.28',
        'b': '1.720'
        } # 13
    ]
    solution = Solution()
    for t in testcases:
        a = t['a']
        b = t['b']
        res = solution.addFloat(a, b)
        print(res)
