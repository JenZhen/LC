#! /usr/local/bin/python3

# https://www.lintcode.com/problem/edit-distance/description
# Example
# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Example
# Given word1 = "mart" and word2 = "karma", return 3.

"""
Algo: DP -- 二维滚动数组/匹配类dp
D.S.: 字符串处理加padding

Solution:
方法一： 滚动二维数组
1. 无滚动数组
Time: O(mn) Space: O(mn)

2. 滚动数组
Time: O(mn) Space: O(m)

DP 分析
1. 状态
f[i][j]: 到位置word1的i 和word2的j，要有几步修改
(注意要用padding来处理“”空字符串的情况)
2. 方程
if word1[i] == word2[j]:
    f[i][j] = f[i - 1][j - 1]
else:
    f[i][j] = (f[i - 1][j - 1], f[i - 1][j], f[i][j - 1]) + 1
                替换                 减            增

3. 初始化
第一行0: l1
第一列0: l2
滚动数组时候注意在循环里定义f[i][0]的值
4. 答案
f[l1][l2]

Corner cases:
"""

class Solution1:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        l1, l2 = len(word1), len(word2)
        # l1 is row, l2 is col
        f = [[0] * (l2 + 1) for i in range(l1 + 1)]
        # init first row as [0, 1, ... , l1]
        # init first col as [0, 1, ... , l2]
        for j in range(l2 + 1):
            f[0][j] = j
        for i in range(l1 + 1):
            f[i][0] = i
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1]) + 1
        print("res: %s" %repr(f))
        return f[l1][l2]

class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        # write your code here
        if not word1 and not word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        l1, l2 = len(word1), len(word2)
        # l1 is row, l2 is col
        f = [[j for j in range(l2 + 1)], [1] * (l2 + 1)]
        # init first row as [0, 1, ... , l1]
        # init first col as [0, 1, ... , l2]
        for i in range(1, l1 + 1):
            # the folloing line is super important!!!
            f[i%2][0] = i
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    f[i%2][j] = f[(i - 1)%2][j - 1]
                else:
                    f[i%2][j] = min(f[(i - 1)%2][j], f[i%2][j - 1], f[(i - 1)%2][j - 1]) + 1
        print("res: %s" %repr(f))
        return f[l1%2][l2]
# Test Cases
if __name__ == "__main__":
    solution = Solution()
