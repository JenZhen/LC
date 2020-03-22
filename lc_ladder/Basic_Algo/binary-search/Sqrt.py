#!/usr/bin/python

# https://leetcode.com/problems/sqrtx/
# Example
# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.

"""
Algo: Binary Search
D.S.:

Solution:
Time: O(logx)
Space: O(1)

Corner cases:
binary search range from 0 to x (itself).
Note: high range end is not x / 2. if x == 1 1 // 2 = 0, this is a corner case

"""
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r  = 0, x
        while l + 1 < r:
            mid = l + (r - l) // 2
            if mid ** 2 < x:
                l = mid
            elif mid ** 2 > x:
                r = mid
            else:
                return mid
        return r if r ** 2 <= x else l


# Test Cases
if __name__ == "__main__":
	solution = Solution()
