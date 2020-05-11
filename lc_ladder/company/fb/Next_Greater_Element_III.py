#! /usr/local/bin/python3

# https://leetcode.com/problems/next-greater-element-iii/submissions/
# Example
# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer
# which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.
#
# Example 1:
# Input: 12
# Output: 21
#
# Example 2:
# Input: 21
# Output: -1
"""
Algo: Same as next permutation
D.S.:

Solution:
32 digit int max  =  (1 << 31) -1

Time: O(len(s))
Space: O(1)
Corner cases:
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if not n: return -1
        INT_MAX = (1 << 31) -1
        s = [c for c in str(n)]
        print(s)
        p = len(s) - 1
        while p - 1 >= 0:
            if s[p - 1] < s[p]:
                l, r = p, len(s) - 1
                while l <= r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                i = p
                while i < len(s):
                    if s[i] > s[p - 1]:
                        s[i], s[p - 1] = s[p - 1], s[i]
                        num = int(''.join(s))
                        if num > INT_MAX:
                            return -1
                        return num
                    i += 1
            p -= 1
        return -1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
