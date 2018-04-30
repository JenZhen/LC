#!/usr/bin/python

# http://lintcode.com/en/problem/perfect-squares/
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
# Example
# Given n = 12, return 3 because 12 = 4 + 4 + 4
# Given n = 13, return 2 because 13 = 4 + 9

"""
Algo: Sequence DP
D.S.:

Solution:
- State: dp[i] number i can be represented by minimun amount of perfect square numbers
- Function: dp[i] = min(dp[i], dp[i - j ** 2] + 1) where j ** 2 <= i
- Initialization: dp[n + 1] dp[0] = 0, dp[i ** 2] = 1 where i ** 2 <= n, other dp[i] = sys.maxsize
- Answer: dp[n]

Time: O(n * (n ** 0.5)) outter loop O(n) inner loop O(n ** 0.5)
Space: O(n) each inner loop starts from j = 1, it's hard to compress extra space

Corner cases:
"""
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        import sys
        # init dp[]
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0 # can be 1 or 0
        for i in range(1, n + 1):
            if i ** 2 <= n:
                dp[i ** 2]  = 1
        repr(dp)
        # iteratation to calculate dp[i]
        for i in range(1, n + 1):
            # i goes from 1 to n (both end inclusive)
            for j in range(1, i + 1):
                # j goes from 1 to i (both end inclusive)
                if j ** 2 <= i:
                    dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                                                    #  |---- means distance to previous perfect square. distance + one more perfect squares, distance could be 1s or a number
        repr(dp)
        return dp[n]

def repr(array):
    print("Sequence is: ")
    print "[" + ", ".join([str(ele) for ele in array]) + "]"

# Test Cases
if __name__ == "__main__":
    testCases = [
        1, 2, 4, 8, 10, 13, 0
    #   1, 2, 1, 2, 2,  2,  0
    ]
    solution = Solution()
    for n in testCases:
        res = solution.numSquares(n)
        print("res: %s" %(res))
