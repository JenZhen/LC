#! /usr/local/bin/python3

# https://www.lintcode.com/problem/repeated-substring-pattern/description?_from=ladder&&fromId=18
# Example

"""
Algo:
D.S.:

Solution:
https://zhuanlan.zhihu.com/p/28248482

Solution1 -- simple
Time: O(n * factor_of_n) n is length of s, factor_of_n is n的因数个数

Solution2 -- KMP Strong hire

Corner cases:
"""

class Solution1:
    """
    @param s: a string
    @return: return a boolean
    """
    def repeatedSubstringPattern(self, s):
        # write your code here
        if not s:
            return True
        for i in range(1, len(s)):
            # iterate subarray's length
            subarray = s[:i]
            mulitplier = len(s) // i
            remaining = len(s) % i
            if remaining != 0:
                continue
            makeuparray = subarray * mulitplier
            if makeuparray == s:
                return True
        return False
# Test Cases
if __name__ == "__main__":
    solution = Solution()
