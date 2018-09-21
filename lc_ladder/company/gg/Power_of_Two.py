#! /usr/local/bin/python3

# https://lintcode.com/problem/power-of-two/description?_from=ladder&&fromId=18
# Example

"""
Algo: Recusion / Iteration
D.S.:

Solution:
Time: O(logN)

Corner cases:
"""

class Solution:
    """
    @param n: an integer
    @return: if n is a power of two
    """
    def isPowerOfTwo(self, n):
        # Write your code here
        if not n or n < 0:
            return False
        if n >= 2:
            return self.helper(n)
        else:
            return self.helper(1 / n)

    def helper(self, n):
        while n % 2 == 0:
            n = n / 2
        return n == 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
