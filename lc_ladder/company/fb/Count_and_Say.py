#! /usr/local/bin/python3

# https://www.lintcode.com/problem/count-and-say/description
# Example
# 报数指的是，按照其中的整数的顺序进行报数，然后得到下一个数。如下所示：
#
# 1, 11, 21, 1211, 111221, ...
#
# 1 读作 "one 1" -> 11
#
# 11 读作 "two 1s" -> 21
#
# 21 读作 "one 2, then one 1" -> 1211
#
# 给定一个整数 n, 返回 第 n 个顺序。
#
# 样例
# 样例 1：
#
# 输入：1
# 输出："1"
# 样例 2：
#
# 输入：5
# 输出："111221"
# 注意事项
# 整数的顺序将表示为一个字符串。


"""
Algo:
D.S.:

Solution:


Corner cases:
"""

class Solution:
    """
    @param n: the nth
    @return: the nth sequence
    """
    def countAndSay(self, n):
        # write your code here
        if n <= 0:
            return None
        res = "1"

        def helper(cntStr):
            if len(cntStr) == 1:
                return "1" + cntStr
            res = ""
            pre = 0
            for ptr in range(1, len(cntStr) + 1):
                if ptr == len(cntStr):
                    return res + str(ptr - pre) + cntStr[pre]
                if cntStr[ptr] != cntStr[pre]:
                    res += str(ptr - pre) + cntStr[pre]
                    pre = ptr
            return res

        for i in range(1, n):
            res = helper(res)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
