#! /usr/local/bin/python3

# https://www.lintcode.com/problem/detect-capital/description?_from=ladder&&fromId=18
# Example
# 给定一个单词，你需要判断其中大写字母的使用是否正确。
#
# 当下列情况之一成立时，我们将单词中大写字母的用法定义为正确：
#
# 这个单词中的所有字母都是大写字母，如“USA”。
# 这个单词中的所有字母都不是大写字母，如“leetcode”。
# 如果它有多个字母，例如“Google”，那么这个单词中的第一个字母就是大写字母。
# 否则，我们定义该单词没有以正确的方式使用大写字母。
#
# 样例
# 输入: "USA"
# 输出: True
#
# 输入: "FlaG"
# 输出: False
#
# 注意事项
# 输入将是一个由大写和小写拉丁字母组成的非空单词。
"""
Algo:
D.S.: string manipulation

Solution:
Time: O(length of word)
        | 第一位大写 | 后面有小写 | 后面有大写
全小写       F          T          F
首字母大      F          T          F
全大写       F          T          F
找到规律即可
Corner cases:
"""

class Solution:
    """
    @param word: a string
    @return: return a boolean
    """
    def detectCapitalUse(self, word):
        # write your code here
        def isUpper(c):
            return c.upper() == c

        firstUpper = isUpper(word[0])
        hasLower = False
        hasUpper = False
        for i in range(1, len(word)):
            if isUpper(word[i]):
                hasUpper = True
            else:
                hasLower = True
        return (hasLower and not hasUpper) or (firstUpper and not hasLower and hasUpper)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
