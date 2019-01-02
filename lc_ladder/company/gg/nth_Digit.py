#! /usr/local/bin/python3

# https://www.lintcode.com/problem/nth-digit/description?_from=ladder&&fromId=18
# Example
# 找出无限正整数数列1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中的第n个数位。
#
# 样例
# 样例1：
#
# 输入：
# 3
#
# 输出：
# 3
# 样例2：
#
# 输入：
# 11
#
# 输出：
# 0
#
# 说明：
# 数列1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...的第11位是0，它是数字10的一部分。
# 注意事项
# n是一个正整数，并且不会超出32位有符号整数的范围（n < 2^31）。

"""
Algo: 数学循环
D.S.:

Solution:
digit 长度， 个数
    1，  9 （1-9）
    2，  90 （10-99）
    3，  900 （100-999）
    ...


Corner cases:
"""

class Solution:
    """
    @param n: a positive integer
    @return: the nth digit of the infinite integer sequence
    """
    def findNthDigit(self, n):
        # write your code here
        startNum = 0
        length = 1
        cnt = 9
        while n > length * cnt:
            n -= length * cnt
            # add cnt of number in this level first
            startNum += cnt
            # prepare for next level
            length += 1
            cnt *= 10
        res = 0
        if n % length == 0:
            res = str(startNum + n / length)[length - 1]
        else:
            res = str(startNum + n / length + 1)[n % length - 1]
        return int(res)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
