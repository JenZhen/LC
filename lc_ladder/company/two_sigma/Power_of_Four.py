#! /usr/local/bin/python3

# https://www.lintcode.com/problem/power-of-four/description
# Example
# 给定一个整数（32位有符号整数），写一个方法判断这个数字是否为4的乘方。
#
# 样例
# 样例 1:
#
# 输入：num = 16
# 输出：True
# 样例 2:
#
# 输入：num = 5
# 输出：False
# 挑战
# 你能否不使用循环/递归解决这个问题呢？

"""
Algo: bit operation, iteration, recursion
D.S.:

Solution:
solution1:
32-bit integer: max 2 ^ 32 - 1 --> 4 ^ 16 is over the max, so iterate power will max to 4 ^ 15
multiplication method

solution2:
division method

solution3:
bit method:
4 ^ n in form of binary --> 1000000 aka 1 followed by 2n zeroes
so need to do
1) 1 follows by zeroe
n (10000), n - 1 (01111)
2) there even number of 0s
1000 >> 1 becomes 100

Corner cases:
"""

class Solution:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def isPowerOfFour(self, num):
        # Write your code here
        base = 4
        for i in range(16):
            if base ** i == num:
                return True
            if base ** i > num:
                return False
        return False

class Solution2:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def isPowerOfFour(self, num):
        while num > 1:
            if num % 4 != 0:
                return False
            num = num / 4
        return True if num == 1 else False

class Solution3:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def isPowerOfFour(self, num):
        if num and not(num & (num - 1)):
            cnt = 0
            while num > 1:
                num = num >> 1
                cnt += 1
            if cnt % 2 == 0:
                return True
        return False

# Test Cases
if __name__ == "__main__":
    solution = Solution()
