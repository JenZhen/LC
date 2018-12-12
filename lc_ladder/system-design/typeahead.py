#!/usr/local/bin/python3

# https://www.lintcode.com/problem/typeahead/description?_from=ladder&&fromId=8
# Example
# 实现一个typeahead功能，给出一个字符串和一个字典，包含若干个单词，返回所有含有这个字符串子串的单词；字典不能被修改，并且这个方法可能被调用多次。
#
# 样例
# 给出一个字典，dictionary = {"Jason Zhang", "James Yu", "Bob Zhang", "Larry Shi"}
#
# 搜索 "Zhang", 返回 ["Jason Zhang", "Bob Zhang"].
#
# 搜索 "James", 返回 ["James Yu"].

"""
Solution:
遍历字典里每个词
    遍历每个词可能的substring
        将substring: word 建立map

查询时候可以直接访问map

Corner cases:
"""
class Typeahead:
    """
    @param: dict: A dictionary of words dict
    """
    def __init__(self, dict):
        # do intialization if necessary
        self.map = {}
        for word in dict:
            for i in range(len(word)):
                for j in range(i + 1, len(word) + 1):
                    substring = word[i : j]
                    if substring not in self.map:
                        self.map[substring] = [word]
                    elif self.map[substring][-1] != word:
                        # 不考虑字典里的Word有重复的情况
                        # 这里是考虑到一个Word中可能有重复的子串
                        self.map[substring].append(word)

    """
    @param: str: a string
    @return: a list of words
    """
    def search(self, str):
        # write your code here
        if str not in self.map:
            return []
        else:
            return self.map[str]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
