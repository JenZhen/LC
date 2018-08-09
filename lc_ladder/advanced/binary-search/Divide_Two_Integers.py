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
    def divide(self, dividend, divisor):
        # write your code here
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        neg = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        a, b = abs(dividend), abs(divisor)
        ans, shift = 0, 31
        while shift >= 0:
            if a >= b << shift:
                a -= b << shift
                ans += 1 << shift
            shift -= 1
        if neg:
            ans = - ans
        if ans > INT_MAX:
            return INT_MAX
        return ans

# Test Cases
if __name__ == "__main__":
    s = Solution()
