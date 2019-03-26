#! /usr/local/bin/python3

# https://www.lintcode.com/problem/roman-to-integer/description
# Example
# 给定一个罗马数字，将其转换成整数。
#
# 输入数据保证返回的结果1到3999的范围内。
#
# 样例
# 样例 1:
#
# 输入: "IV"
# 输出: 4
# 样例 2:
#
# 输入: "XCIX"
# 输出: 99
# 说明
# 什么是 罗马数字?
#
# https://en.wikipedia.org/wiki/Roman_numerals
# https://zh.wikipedia.org/wiki/罗马数字
# http://baike.baidu.com/view/42061.htm
"""
Algo: math
D.S.:

Solution:
careful for cases like "IV" if later is greater than prev do + V - I * 2
remember to remove previously added small value
Time: O(n)
Space: O(1)

Corner cases:
"""
class Solution:
    """
    @param s: Roman representation
    @return: an integer
    """
    digiMap = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    def romanToInt(self, s):
        # write your code here
        if not s:
            return 0

        res = 0
        for i in range(len(s)):
            curVal = self.digiMap[s[i]]
            res += curVal
            if i > 0:
                preVal = self.digiMap[s[i - 1]]
                if preVal < curVal:
                    res -= (preVal * 2)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
