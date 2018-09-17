#! /usr/local/bin/python3

# https://www.lintcode.com/problem/valid-word-square/description
# Example
# 给定一个单词序列，检查它是否构成一个有效单词广场。
# 一个有效的单词广场满足：如果第k行和第k列读取相同的字符串,并且0≤k<max(numRows numColumns)。
#
# 样例
# 给定
# [
#   "abcd",
#   "bnrt",
#   "crmy",
#   "dtye"
# ]
# 返回 true
#
# 解释:
# 第一行和第一列都是“abcd”。
# 第二行和第二列都是“bnrt”。
# 第三行和第三列都是“crmy”。
# 第四行和第四列都是“dtye”。
#
# 因此，这是一个有效的单词广场.
# 给定
# [
#   "abcd",
#   "bnrt",
#   "crm",
#   "dt"
# ]
# 返回 true
#
# 解释:
# 第一行和第一列都是“abcd”。
# 第二行和第二列都是“bnrt”。
# 第三行和第三列都是“crm”。
# 第四行和第四列都是“dt”。
#
# 因此，这是一个有效的单词广场.
# 给定
# [
#   "ball",
#   "area",
#   "read",
#   "lady"
# ]
# 返回 false
#
# 解释:
# 第三行是 "read" 但是第三列是 "lead".
#
# 因此，这不是一个有效的单词广场.
# 注意事项
# 给定的单词数量至少为1，且不超过500。
# 单词长度至少为1，不超过500。
# 每个单词只包含小写英文字母a-z。

"""
Algo:
D.S.: 2D array

Solution:
暴力揭发，考察corner case
case1
x, x, x
x
cause: m != n
case2
x, x, x
x, x, x --> (1, 2) <=> (2, 1) row2 has no col1: i >= words[j].size()
x
case3
x, x, x
x, x
x, x --> (2, 1) <=> (1, 2) row1 has no col2: i >= words[j].size()
case4
x, x, x
x, x, x, x --> (1, 3), no row j: j >= len(words)
x,

Corner cases:
"""

class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # Write your code here
        if not words or not words[0]:
            return True
        m = len(words) # number of words
        n = len(words[0])
        if m != n:
            return False
        if m == n == 1:
            return True
        for i in range(m):
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
