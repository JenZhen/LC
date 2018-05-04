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
Extremely difficult to handle corner cases
"""

class Solution1:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s:
            return 0

        charDict = {}
        length = len(s)
        i, j, ans = 0, 0, 0

        def addToDict(val):
            if val not in charDict:
                charDict[val] = 1
            else:
                charDict[val] += 1
        def delFromDict(val):
            if val in charDict:
                charDict[val] -= 1
                if charDict[val] == 0:
                    del charDict[val]

        for i in range(length):
            while j < length:
                if s[j] in charDict:
                    addToDict(s[j])
                else:
                    if len(charDict) == k:
                        break;
                    addToDict(s[j])
                j += 1

            ans = max(ans, j - i)
            delFromDict(s[i])

        return ans


# Test Cases
if __name__ == "__main__":
    testCases = [
        {
         "s": "eceba",
         "k": 3
        },
    ]
    s1 = Solution1()
    for t in testCases:
        s = t["s"]
        k = t["k"]
        res1 = s1.lengthOfLongestSubstringKDistinct(s, k)
        print("res1: %s" %res1)
