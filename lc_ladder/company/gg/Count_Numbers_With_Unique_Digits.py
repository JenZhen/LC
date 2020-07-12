#! /usr/local/bin/python3

# https://leetcode.com/problems/count-numbers-with-unique-digits/submissions/
# Example
# Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
# Example:
#
# Input: 2
# Output: 91
# Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100,
#              excluding 11,22,33,44,55,66,77,88,99
#
# Constraints:
# 0 <= n <= 8
"""
Algo: DP
D.S.:

Solution:


Corner cases:
"""
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 10
        if n == 2: return 91
        f = [0] * (n + 1)
        f[1] = 10
        f[2] = 9 * 9
        for i in range(3, n + 1):
            f[i] = f[i - 1] * (11 - i)
        return sum(f)

    '''
    n = 0: 0 (required as 1)
    n = 1: 10
    n = 2: 9 * 9 = 81
    n = 3: 9 * 9 * 8
    n = 4: 9 * 9 * 8 * 7
    n = 5: 9 * 9 * 8 * 7 *6
    ...
    '''

# Test Cases
if __name__ == "__main__":
    solution = Solution()
