#! /usr/local/bin/python3

# https://www.lintcode.com/en/problem/longest-substring-with-at-most-k-distinct-characters/
# Given a string s, find the length of the longest substring T that contains at most k distinct characters.
# Example
# For example, Given s = "eceba", k = 3,
# T is "eceb" which its length is 4.

"""
Algo: 2-Pointers same direction. With improvement of inner j move forward only.
D.S.: With help of set/dictionary

Solution:

Corner cases:
"""

class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s or not k:
            return 0

        i, j, ans = 0, 0, 0
        length = len(s)
        charDict = {}
        for i in range(length):
            # TODO NOT FINISHED YET



# Test Cases
if __name__ == "__main__":
    solution = Solution()
