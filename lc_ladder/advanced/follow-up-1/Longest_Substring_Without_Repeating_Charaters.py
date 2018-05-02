#! /usr/local/bin/python3

# https://lintcode.com/en/problem/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.
# Example
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.

"""
Algo:
D.S.:

Solution:
TODO: NOT FINISHED YET


Corner cases:
"""

class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        if not s:
            return -1

        charDict = {}
        length = len(s)
        i, j, ans = 0, 0, 0
        for i in range(length):
            while j < length and s[j] not in charDict:
                print("j value: %s" %(s[j]))
                charDict[s[i]] = 1
                j += 1
            if s[j] in charDict:
                print("i: %s, j: %s" %(i, j))
                ans = max(ans, j - i)
            del charDict[s[i]]
        return ans

# Test Cases
if __name__ == "__main__":
    testCases = [
        "aaaa",
    ]

    solution = Solution()
    for s in testCases:
        res = solution.lengthOfLongestSubstring(s)
        print("res: %s" %res)
