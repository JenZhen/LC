#! /usr/local/bin/python3

# https://www.lintcode.com/problem/license-key-formatting/description?_from=ladder&&fromId=18
# Example
# 给定一个用字符串S表示的许可证，其中仅仅包含了数字、字母和短横线。字符串被N个短横线“-”切分为了N+1组。
#
# 给定一个数字K，要求重新整理字符串的格式，使得除了第一组之外的每个组正好K个字符，第一组长度可以比K小，但也至少要包含一个字符。此外，对于两个组之间必须要插入一个短横线，所有的小写字母都要转换为大写字母。
#
# 字符串S的长度不会超过12000，而且K是一个正整数。
# 字符串S仅仅包含大小写字母、数字和短横线“-”。
# 字符串S非空。
#
# 您在真实的面试中是否遇到过这个题？
# 样例
# 输入: S = "5F3Z-2e-9-w", K = 4
#
# 输出: "5F3Z-2E9W"
#
# 解释: 字符串S切分为两个部分, 每个部分有4个字符。
# 注意两个额外的横线是多余的，可以删掉。
#
# 输入: S = "2-5g-3-J", K = 2
#
# 输出: "2-5G-3J"
#
# 解释: 字符串S切分为了三部分, 每个部分有两个字符，除了第一个部分，因为如原题所述，它应该更短。

"""
Algo:
D.S.:

Solution:


Corner cases:
"""

class Solution:
    """
    @param S: a string
    @param K: a integer
    @return: return a string
    """
    def licenseKeyFormatting(self, S, K):
        # write your code here
        def pureSs(s):
            s = ""
            for i in s:
                if i == "-":
                    continue
                elif '0' <= i <= '9':
                    s += i
                else:
                    s += i.upper()
            print(s)
            return s[:]

        ss = pureSs(S)
        if ss == "":
            return ""
        firstSecLen = ss % K
        ssList = [ss[:firstSecLen]]
        for i in range(firstSecLen, len(ss)):
            ssList.append(ss[i : (i + 4)])
            i += 4
        print(ssList)
        return "-".join(ssList)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
