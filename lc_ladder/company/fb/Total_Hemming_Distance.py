#! /usr/local/bin/python3

# https://www.lintcode.com/problem/total-hamming-distance/description
# Example
# 两个整数之间的汉明距离是相应位不同的位置数。
#
# 现在你的工作是找到所有给定数字对之间的总汉明距离。
#
# Example
# 例1:
#
# 输入: [4, 14, 2]
# 输出: 6
# 解释：在二进制表示中，4是0100,14是1110,2是0010（只是显示在这种情况下相关的四个位）。 所以答案是：
# 汉明距离(4,14) + 汉明距离(4,2) + 汉明距离(14,2) = 2 + 2 + 2 = 6。
# 例2:
#
# 输入: [2, 1, 0]
# 输出: 4
# 解释：在二进制表示中，2是10,1是01,0是00（只是显示在这种情况下相关的四个位）。 所以答案是：
# 汉明距离(2,1) + 汉明距离(1,0) + 汉明距离(2,0) = 2 + 1 + 1 = 4。
# Notice
# 1.给定数组的元素在0到10^9的范围内
# 2.数组长度不超过10^4。


"""
Algo: 组合数，bit operation
D.S.:

Solution:
这个题也要考虑数据规模 10 ^ 4 如果用暴力 O(n^2) 会超时

优化解法
4： 0100
14：1110
2： 0010

每一列可以分为2组：在i列为1 的和为0的。
i 列 x个1 就有n - x 个0, 差异组合为 x * (n - x)
把每一列的加起来就是ttl hemming distance

Time：O(n * 32)

Corner cases:
"""

class Solution:
    """
    @param nums: the gievn integers
    @return: the total Hamming distance between all pairs of the given numbers
    """
    def totalHammingDistance(self, nums):
        ttl = 0
        for i in range(32):
            cnt_1 = 0
            for n in nums:
                cnt_1 += (n >> i) & 1
            cnt_0 = len(nums) - cnt_1
            ttl += cnt_0 * cnt_1
        return ttl

# Test Cases
if __name__ == "__main__":
    solution = Solution()
