#! /usr/local/bin/python3

# https://www.lintcode.com/problem/rotated-digits/description?_from=ladder&&fromId=18
# Example
# X是一个好数当且仅当单独旋转每一个数位180度之后，能够得到一个合法的不同于X的数。每一个数位必须被旋转 - 我们不能选择不管它。
#
# 如果每一个数位在旋转之后仍然是一个数位，那么这个数字是合法的。0,1和8旋转保持不变; 2和5旋转后互相变换; 6和9旋转后互相变换，其余数字旋转后不会变成任何数字所以是不合法的。
#
# 现在给定一个正数 N，多少1 到 N 之间的数X是好的?
#
# 样例
# 样例1:
#
# 输入: 10
# 输出: 4
# 解释:
# 在[1, 10]之内存在4个好数：2, 5, 6, 9.
# 注意1和10不是好数，因为它们在旋转之后没有变化。
# 样例2:
#
# 输入: 5
# 输出: 2
# 解释:
# 在[1, 5]之内存在2个好数：2, 5
# 注意事项
# N 会在范围 [1, 10000]内。

"""
Algo:
D.S.:

Solution:
1. Time: O(N * len(num)), Space: O(len(num))
2. Time: O(N * len(num)), Space: O(1)

Corner cases:
"""

class Solution:
    """
    @param N: a positive number
    @return: how many numbers X from 1 to N are good
    """
    def rotatedDigits(self, N):
        # write your code here
        if not N:
            return 0
        cnt = 0
        for i in range(1, N + 1):
            if self.ifGoodNum(i):
                cnt += 1
        return cnt
    def ifGoodNum(self, num):
        strnum = str(num)
        strList = list(strnum)
        for char in strList:
            if char in set(['3', '4', '7']):
                return False
        reversedNum = self.reverseNum(strList)
        if reversedNum == num:
            return False
        return True
    def reverseNum(self, strList):
        res = []
        for char in strList:
            if char == '0':
                res.append('0')
            elif char == '1':
                res.append('1')
            elif char == '2':
                res.append('5')
            elif char == '5':
                res.append('2')
            elif char == '6':
                res.append('9')
            elif char == '8':
                res.append('8')
            else:
                res.append('6')
        return int(''.join(res))


class Solution2:
    """
    @param N: a positive number
    @return: how many numbers X from 1 to N are good
    """
    def rotatedDigits(self, N):
        # write your code here
        if not N:
            return 0
        cnt = 0
        for i in range(1, N + 1):
            if self.ifGoodNum(i):
                cnt += 1
        return cnt
    def ifGoodNum(self, num):
        strlist = list(str(num))
        lenNum = len(strlist)
        lenSysm = 0
        lenAsysm = 0
        for char in strlist:
            if char in set(['0','1','8']):
                lenSysm += 1
            elif char in set(['2', '5', '6', '9']):
                lenAsysm += 1
            else:
                return False
        if lenSysm == lenNum:
            return False
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
