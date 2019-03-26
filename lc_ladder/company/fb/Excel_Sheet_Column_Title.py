#! /usr/local/bin/python3

# https://www.lintcode.com/problem/excel-sheet-column-title/description
# Example
# 给定一个正整数，返回相应的列标题，如Excel表中所示。
#
# 样例
# Example1
#
# Input: 28
# Output: "AB"
# Example2
#
# Input: 29
# Output: "AC"
# 注意事项
# 1 -> A
# 2 -> B
# 3 -> C
#  ...
# 26 -> Z
# 27 -> AA
# 28 -> AB

"""
Algo: 数学，进制转换
D.S.:

Solution:
n -= 1 很重要。
一定不要%27

Corner cases:
"""
class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        # write your code here
        if n <= 0:
            return None
        res = ""
        while n > 0:
            n -= 1
            digi = n % 26
            char = chr((digi) + ord('A'))
            res = char + res
            n = n // 26
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
