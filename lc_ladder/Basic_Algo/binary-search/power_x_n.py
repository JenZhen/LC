#!/usr/bin/python

# https://leetcode.com/problems/powx-n/
# Implement pow(x, n), which calculates x raised to the power n (xn).
#
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100
# Example 3:
#
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Note:
#
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]

"""
Algo: Binary Search
D.S.:

Solution:
Time: O(logn)
Space: O(1)

Corner cases:
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            return self.helper(x, n)
        else:
            return 1 / self.helper(x, -n)

    def helper(self, x, n):
        if n == 0:
            return 1
        half = self.helper(x, n // 2)
        if n % 2 == 1:
            return half * half * x
        else:
            return half * half

# Test Cases
if __name__ == "__main__":
	solution = Solution()
