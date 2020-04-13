#! /usr/local/bin/python3

# https://leetcode.com/problems/palindrome-permutation/
# Example
# Given a string, determine if a permutation of the string could form a palindrome.
#
# Example 1:
#
# Input: "code"
# Output: false
# Example 2:
#
# Input: "aab"
# Output: true
# Example 3:
#
# Input: "carerac"
# Output: true

"""
Algo:
D.S.: String

Solution:


Corner cases:
"""

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if not s: return True
        slot = [0] * 256
        for ch in s:
            slot[ord(ch)] += 1
        hasOdd = False
        for s in slot:
            if s % 2 == 1:
                if hasOdd == False:
                    hasOdd = True
                else:
                    return False
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
