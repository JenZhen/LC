#! /usr/local/bin/python3

# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Example
# Given an integer n, return any array containing n unique integers such that they add up to 0.
#
# Example 1:
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# Example 2:
# Input: n = 3
# Output: [-1,0,1]
# Example 3:
# Input: n = 1
# Output: [0]
#
# Constraints:
# 1 <= n <= 1000
"""
Algo:
D.S.:

Solution:


Corner cases:
"""

class Solution1:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2 == 1:
            n -= 1
            res.append(0)
        k = 1
        while n > 0:
            res.append(k)
            res.append(k * (-1))
            k += 1
            n -= 2
        return res
class Solution2:
    def sumZero(self, n: int) -> List[int]:
        res = []
        res.extend([i + 1 for i in range(n // 2)])
        res.extend([(i + 1) * (-1) for i in range(n // 2)])
        if n % 2 == 1:
            res.append(0)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
