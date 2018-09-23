#! /usr/local/bin/python3

# Requirement
# Example
# 给定一个字符串，逐个翻转字符串中的每个单词。
#
# 说明
# 单词的构成：无空格字母构成一个单词
# 输入字符串是否包括前导或者尾随空格？可以包括，但是反转后的字符不能包括
# 如何处理两个单词间的多个空格？在反转字符串中间空格减少到只含一个
"""
Algo:
D.S.:

Solution:
Watch out for corner cases
Time: O(n)

Corner cases:
"""

class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        res = ""
        if not s:
            return res
        l, r = 0, 0
        while r < len(s):
            # find start of a word
            while r < len(s) and s[r] == " ":
                r += 1
            if r >= len(s):
                break
            l = r
            r = l + 1
            # find the end of a word
            while r < len(s) and s[r] != " ":
                r += 1
            if res == "":
                res = s[l:r]
            else:
                res = s[l:r] + " " + res
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
