#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo:
D.S.:

Solution:
1. Use list prime number O(n)
Issues
1) 26 digits or 52 or 256
2) if string is too long may overflow


Corner cases:
"""

class Solution1:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        if not s and not t:
            return True
        if not s:
            return False
        if not t:
            return False
        if len(s) != len(t):
            return False

        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        ssum, tsum = 0, 0
        for c in s:
            ssum += p[ord(c) - ord('a')]
        for c in t:
            tsum += p[ord(c) - ord('a')]
        return ssum == tsum

class Solution2:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        if not s and not t:
            return True
        if not s:
            return False
        if not t:
            return False
        if len(s) != len(t):
            return False

        lot = [0] * 256
        for c in s:
            lot[ord(c)] += 1
        for c in t:
            lot[ord(c)] -= 1
        # 注意结果不能查 sum(lot), 有可能有1， -1的情况
        for i in lot:
            if i != 0:
                return False
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
