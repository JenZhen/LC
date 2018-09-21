#! /usr/local/bin/python3

# https://lintcode.com/problem/power-of-three/discuss?_from=ladder&&fromId=18
# Example
# Given an integer, write a function to determine if it is a power of three.
#
# 挑战
# Could you do it without using any loop / recursion?

"""
Algo:
D.S.:

Solution:
Solution1: Iteration
Solution2: recursion
Solution3: Math (log)

3 ** x = n
log(3 ** x) = log(n)
xlog(3) = log(n)
x = log(n) / log(3) = log(n, 3) based on 3
3 ** round(log(n, 3)) == n --> condition

Corner cases:
"""

class Solution1:
    """
    @param n: an integer
    @return: if n is a power of three
    """
    def isPowerOfThree(self, n):
        # Write your code here
        if not n or n <= 0:
            return False
        if n < 1:
            return self.isPowerOfThree(1 / n)
        return self.helper(n)

    def helper(self, n):
        while n % 3 == 0:
            n = n / 3
        return n == 1

class Solution2:
    """
    @param n: an integer
    @return: if n is a power of three
    """
    def isPowerOfThree(self, n):
        # Write your code here
        if not n or n <= 0:
            return False
        if n < 1:
            return self.isPowerOfThree(1 / n)
        if n == 1:
            return True
        return n % 3 == 0 and self.isPowerOfThree(n / 3)

class Solution3:
    """
    @param n: an integer
    @return: if n is a power of three
    """
    def isPowerOfThree(self, n):
        from math import log
        # Write your code here
        if not n or n <= 0:
            return False
        if n < 1:
            return self.isPowerOfThree(1 / n)
        return 3 ** round(log(n, 3)) == n
# Test Cases
if __name__ == "__main__":
    solution = Solution()
