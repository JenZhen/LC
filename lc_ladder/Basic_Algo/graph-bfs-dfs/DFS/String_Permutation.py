#! /usr/local/bin/python3

# https://leetcode.com/problems/permutation-in-string/submissions/
# Example
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
# In other words, one of the first string's permutations is the substring of the second string.
# Example 1:
#
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
#
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
#
#
# Note:
#
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].

"""
Algo:
D.S.: Array

Solution:
Iteration
Using array for frequency of char

Corner cases:
 so need to check invalidity using A is None or B is None
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_slot = [0] * 256
        for ch in s1:
            s1_slot[ord(ch)] += 1

        for i in range(len(s2) - len(s1) + 1):
            if s1_slot[ord(s2[i])] > 0:
                s2_slot = [0] * 256
                for j in range(i, i + len(s1)):
                    # build s2_slot
                    s2_slot[ord(s2[j])] += 1
                if self.match(s1_slot, s2_slot):
                    return True
        return False

    def match(self, s1_slot, s2_slot):
        for i in range(len(s1_slot)):
            if s1_slot[i] != s2_slot[i]:
                return False
        return True


# Test Cases
if __name__ == "__main__":
    solution = Solution()
