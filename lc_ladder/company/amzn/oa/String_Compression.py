#! /usr/local/bin/python3

# Requirement
# Example

# 设计一种方法，通过给重复字符计数来进行基本的字符串压缩。
#
# 例如，字符串 aabcccccaaa 可压缩为 a2b1c5a3 。而如果压缩后的字符数不小于原始的字符数，则返回原始的字符串。
#
# 可以假设字符串仅包括a-z的字母。
#
# 样例
# str=aabcccccaaa 返回 a2b1c5a3
# str=aabbcc 返回 aabbcc
# str=aaaa 返回 a4

"""
Algo:
D.S.: 字符串双指针

Solution:
1. 注意读题
2. 注意corner Cases
1) ""
2) "a"

Corner cases:
"""

class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """
    def compress(self, originalString):
        # write your code here
        res = ""
        if not originalString:
            return res
        if len(originalString) == 1:
            return originalString
        s, f = 0, 1
        while f < len(originalString):
            while f < len(originalString) and originalString[f] == originalString[s]:
                f += 1
            res += (originalString[s] + str(f - s))
            s = f
            f = s + 1
        return res if len(res) < len(originalString) else originalString

# Test Cases
if __name__ == "__main__":
    solution = Solution()
