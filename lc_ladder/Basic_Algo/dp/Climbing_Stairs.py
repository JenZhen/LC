#!/usr/bin/python

# http://lintcode.com/en/problem/climbing-stairs/
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example
# Given an example n=3 , 1+1+1=2+1=1+2=3
# return 3

"""
Algo: Sequence DP
D.S.:

Solution:
- State: How many option to go to a certain step
- Function: step(i) = step(i - 1) + step(i - 2)
- Initialization: step(1) = 1 (only 1 way there) step(2) = 2 (2 ways to get there)
- Answer: step(n)

Time: O(n)
Space: O(1), only need 2 varibles to memorize later-used small problem answers

Corner cases:
"""
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        preSteps = [1, 2]
        res = None
        for i in range(3, n + 1):
            res = sum(preSteps)
            preSteps[0] = preSteps[1]
            preSteps[1] = res
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
