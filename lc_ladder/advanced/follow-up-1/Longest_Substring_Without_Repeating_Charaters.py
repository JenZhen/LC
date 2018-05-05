#! /usr/local/bin/python3

# https://lintcode.com/en/problem/longest-substring-without-repeating-characters/
# Given a string, find the length of the longest substring without repeating characters.
# Example
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.

"""
Algo: 2-pointers same direction. Can improve by not moving inner loop j backward.
D.S.: With help of set/dictionary
    note char set can be used as charDict = [0] * 256 (if in set, make charDict[char] = 1, else (as init) = 0)

Solution:
With improvement O(n^2) -> O(n)

Corner cases:
- Invalid input "", None return 0
- Very Important: j out of index, when breaking out of while loop, if j at a legal position for to access value s[j] and get distance between i and j
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
                charDict[s[j]] = 1
                # at this step, j is within range of index
                ans = max(ans, j - i + 1)
                j += 1
            del charDict[s[i]]
        return ans

# Test Cases
if __name__ == "__main__":
    testCases = [
        "aaaa",
        "z",
    ]

    solution = Solution()
    for s in testCases:
        res = solution.lengthOfLongestSubstring(s)
        print("res: %s" %res)
