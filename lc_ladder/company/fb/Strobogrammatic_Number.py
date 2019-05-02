#! /usr/local/bin/python3

# https://www.lintcode.com/problem/strobogrammatic-number/description
# Example
# 一个镜像数字是指一个数字旋转180度以后和原来一样(倒着看)。例如，数字"69"，"88"，和"818"都是镜像数字。
# 写下一个函数来判断是否这个数字是镜像的。数字用字符串来表示。
#
# 样例
# 样例1:
#
# 输入 : "69"
# 输出 : true
# 样例 2:
#
# 输入 : "68"
# 输出 : false
"""
Algo: Two pointers
D.S.:

Solution:


Corner cases:
"""
class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        if not num:
            return False

        num_str = str(num)
        l, r = 0, len(num) - 1
        while l < r:
            if (num_str[l] == '6' and num_str[r] == '9') or \
                (num_str[l] == '9' and num_str[r] == '6'):
                    l += 1
                    r -= 1
            elif (num_str[l] == num_str[r] and (num_str[l] in ['0', '1', '8'])):
                l += 1
                r -= 1
            else:
                return False
        if l == r:
            if num_str[l] in ['0', '1', '8']:
                return True
            else:
                return False
        else:
            return True


# Test Cases
if __name__ == "__main__":
    solution = Solution()
