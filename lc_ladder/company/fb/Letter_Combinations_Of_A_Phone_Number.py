#! /usr/local/bin/python3

# https://www.lintcode.com/problem/letter-combinations-of-a-phone-number/description
# Example
# 给一个不包含'0'和'1'的数字字符串，每个数字代表一个字母，请返回其所有可能的字母组合。
#
# 下图的手机按键图，就表示了每个数字可以代表的字母。
#         '2': ["a", "b", "c"],
#         '3': ["d", "e", "f"],
#         '4': ["g", "h", "i"],
#         '5': ["j", "k", "l"],
#         '6': ["m", "n", "o"],
#         '7': ["p", "q", "r", "s"],
#         '8': ["t", "u", "v"],
#         '9': ["w", "x", "y", "z"]
#
# 1	2
# ABC	3
# DEF
# 4
# GHI	5
# JKL	6
# MNO
# 7
# PQRS	8
# TUV	9
# WXYZ
# 样例
# 样例 1:
#
# 输入: "23"
# 输出: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# 解释:
# '2' 可以是 'a', 'b' 或 'c'
# '3' 可以是 'd', 'e' 或 'f'
# 样例 2:
#
# 输入: "5"
# 输出: ["j", "k", "l"]
# 注意事项
# 以上的答案是按照词典编撰顺序进行输出的，不过，在做本题时，你也可以任意选择你喜欢的输出顺序。

"""
Algo: DFS, Backtracking
D.S.:

Solution:
Time: O(N ^ 3)
Space: O(N) -- path

Corner cases:
"""
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    charMap = {
        '2': ["a", "b", "c"],
        '3': ["d", "e", "f"],
        '4': ["g", "h", "i"],
        '5': ["j", "k", "l"],
        '6': ["m", "n", "o"],
        '7': ["p", "q", "r", "s"],
        '8': ["t", "u", "v"],
        '9': ["w", "x", "y", "z"]
    }
    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []
        path = ""
        res = []
        startwith = 0
        self.dfs(path, res, startwith, digits)
        return res

    def dfs(self, path, res, startwith, digits):
        if len(path) == len(digits):
            res.append(path[:])
            return
        for ele in self.charMap[digits[startwith]]:
            path += ele
            self.dfs(path, res, startwith + 1, digits)
            path = path[:-1]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
