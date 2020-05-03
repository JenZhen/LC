#! /usr/local/bin/python3

# https://leetcode.com/problems/divide-two-integers/submissions/
# Example
# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
# Return the quotient after dividing dividend by divisor.
# The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
#
# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = truncate(3.33333..) = 3.
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = truncate(-2.33333..) = -2.
# Note:
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
# For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
"""
Algo: Binary Search
D.S.:

Solution:
Expotential search

Time: O(logN) ^ 2 -- n is abs(dividend) 两层嵌套的while loop 分别是logN
Space: O(1)
Corner cases:
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = (1 << 31) -1
        INT_MIN = -(1 << 31)
        if dividend == 0:
            return 0
        if divisor == 0:
            return INT_MAX if dividend > 0 else INT_MIN

        # 注意这个特殊的情况
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        sign = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)

        a, b = abs(dividend), abs(divisor)
        res = 0
        while a >= b:
            shift = 0
            while a >= (b << shift):
                shift += 1
            a -= (b << (shift - 1))
            res += (1 << (shift - 1))

        return res if sign else -res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
