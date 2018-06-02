#! /usr/local/bin/python3

# https://www.lintcode.com/problem/sqrtx-ii/description
# Implement double sqrt(double x) and x >= 0.
# Compute and return the square root of x.
# Example
# Given n = 2 return 1.41421356


"""
Algo: Binary Search template
D.S.:

Solution:
key point:
compare two integers:
if a == b:
    # pass
Compare two double/float
if a - x < epsilon:
    # pass
特征：find **the last number** such that number ** 2 <= x
Time: O(logx)

Corner cases:
"""
class Solution:
    """
    @param: x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        l = 0
        r = x if x >= 1 else 1
        eps = 10 ** -10
        while l + eps < r:
            mid = (l + r) / 2
            if mid ** 2 < x:
                l = mid
            elif mid ** 2 > x:
                r = mid
            else:
                return mid
        if r ** 2 <= x:
            return r
        else:
            return l

# Test Cases
if __name__ == "__main__":
    s = Solution()
