#!/usr/bin/python

# http://lintcode.com/en/problem/valid-palindrome/
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

"""
Algo: two pointers
D.S.:

Solution:
Exactly same method as Partition Array
Useful built-in functions
- isalnum() check if alphanumeric
- ord('a') -- get ASCII numer
- chr(90) -- get char

Corner cases:
- empty string: True
"""

class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        if not s:
            return True

        """
        def isAlphaNum(s):
            if (ord(s) >= ord('a') and ord(s) <= ord('z')) or \
                (ord(s) >= ord('A') and ord(s) <= ord('Z')) or \
                (ord(s) >= ord('0') and ord(s) <= ord('9')):
                return True
        """

        l, r = 0, len(s) - 1
        while l < r:
            """
            while l < r and not isAlphaNum(s[l]):
                l += 1
            while l < r and not isAlphaNum(s[r]):
                r -= 1
            """
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].upper() != s[r].upper():
                return False
            l += 1
            r -= 1
        return True
# Test Cases
if __name__ == "__main__":
    solution1 = Solution1()
    testCases = [
        {"s": "Bab"},
        {"s": ""},
    ]
    for t in testCases:
        s = t["s"]
        res1 = solution1.isPalindrome(s)
        print("res1: %s" %res1)
