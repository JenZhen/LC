#! /usr/local/bin/python3

# https://www.lintcode.com/problem/add-strings/description
# Example

"""
Algo:
D.S.:

Solution:
O(n) -- 遍历字符串

Corner cases:
Carry 在最后面不要忘了查是不是等于1
‘999’ +
’1’
"""
class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        # write your code here
        if not num1 and not num2:
            return ""
        if not num1:
            return num2
        if not num2:
            return num1

        res = ""
        carry = 0
        for i in range(1, max(len(num1), len(num2)) + 1):
            ttl = 0
            if i <= len(num1):
                ttl += int(num1[-i])
            if i <= len(num2):
                ttl += int(num2[-i])
            ttl += carry
            digit = ttl % 10
            carry = ttl // 10
            res = str(digit) + res
        if carry == 1:
            return "1" + res
        else:
            return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
