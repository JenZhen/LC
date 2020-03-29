#!/usr/bin/python

# http://www.jiuzhang.com/solution/climbing-stairs-ii/
# A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
# Example

"""
Algo: DP
D.S.:

Solution:
- State:
- Function:
- Initialization:
- Answer:

Time: O(n)
Space: O(1)

Corner cases:
"""

class Solution:
    """
    @param {int} n a integer
    @return {int} a integer
    """
    def climbStairs2(self, n):
        # write your code here
        if n <= 1:
            return 1
        if n == 2:
            return 2
        # Init
        a, b, c = 1, 2, 4
        for i in range(4, n + 1):
            a, b, c = b, c, a + b + c
        return c

# Test Cases
if __name__ == "__main__":
    solution = Solution()
