#! /usr/local/bin/python3

# https://www.lintcode.com/problem/climbing-stairs/description
# Example
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example
# Given an example n=3 , 1+1+1=2+1=1+2=3
# return 3

"""
Algo: DP
D.S.:

Solution:


Corner cases:
n = 0, return 0
"""

class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n is None or n <= 0:
            return 0

        f = [1, 1] # init with level 0, level 1 with 1, 1
        for i in range(2, n + 1):
            f[i % 2]  = f[(i - 1) % 2] + f[(i - 2) % 2]
        return f[n % 2]



# Test Cases
if __name__ == "__main__":
    solution = Solution()
