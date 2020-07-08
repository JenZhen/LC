#! /usr/local/bin/python3

# https://leetcode.com/problems/mirror-reflection/solution/
# Example

"""
Algo:
D.S.:

Solution:
Instead of modelling the ray as a bouncing line, model it as a straight line through reflections of the room.
For example, if p = 2, q = 1, then we can reflect the room horizontally, and draw a straight line from (0, 0) to (4, 2).
The ray meets the receptor 2, which was reflected from (0, 2) to (4, 2).

In general, the ray goes to the first integer point (kp, kq) where k is an integer, and kp and kq are multiples of p.
Thus, the goal is just to find the smallest k for which kq is a multiple of p.

The mathematical answer is k = p / gcd(p, q).


Time Complexity: O(log P)O(logP), the complexity of the gcd operation.
Space Complexity: O(1)O(1).

Corner cases:
"""

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        k = self.gcd(p, q)
        p = p // k
        p = p % 2
        q = q // k
        q = q % 2
        if p == 1 and q == 1:
            return 1
        elif p == 1: #q == 0
            return 0
        else:
            return 2

    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b % a, a)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
