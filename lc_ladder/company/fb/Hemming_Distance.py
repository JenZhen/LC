#! /usr/local/bin/python3

# https://www.lintcode.com/problem/hamming-distance/description
# Example
# 两个整数的Hamming距离是对应比特位不同的个数。
# 给定两个整数x和y，计算两者的Hamming距离。
#
# Example
# 样例1
#
# 输入: x = 1 和 y = 4
# 输出: 2
# 解释:
# 1的二进制表示是001
# 4的二进制表示是100
# 共有2位不同
# 样例2
#
# 输入: x = 5 和 y = 2
# 输出: 3
# 解释:
# 5的二进制表示是101
# 2的二进制表示是010
# 共有3位不同
# Notice
# 0 ≤ x, y < 231

"""
Algo: bit operation
D.S.:

Solution:
bit operation to count how many 1 digit
xnor operation -- 数二进制有多少位不同
01 ^ 10 = 11

Corner cases:
"""
class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """
    def hammingDistance(self, x, y):
        # write your code here
        xnor = x ^ y
        res = 0
        while xnor != 0:
            if xnor % 2 == 1:
                res += 1
            xnor = xnor >> 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
