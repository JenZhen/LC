#! /usr/local/bin/python3

# https://lintcode.com/problem/divide-two-integers/description
# Example
# Divide two integers without using multiplication, division and mod operator.
# If it is overflow, return 2147483647

"""
Algo: Binary Seach; Bit Operation
D.S.:

Solution:
Cannot use * / % meaning bit operation
# TDOO: more practice on bit operaiton

Time: O(31)

Corner cases:
INT_MAX = 2147483647 ie 2^31 - 1
1. if denominator = 0, return INT_MAX
2. 1/-1, -1/1, make note the result sign, then convert both numerator and denominator to positive
3.
"""

class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = (1 << 31) -1
        INT_MIN = -(1 << 31)
        if dividend == 0:
            return 0
        if divisor == 0:
            return INT_MAX if dividend > 0 else INT_MIN

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
    s = Solution()
