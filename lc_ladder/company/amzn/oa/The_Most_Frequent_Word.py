#! /usr/local/bin/python3

# https://www.lintcode.com/problem/the-most-frequent-word/description?_from=ladder&&fromId=62
# Example
# 给出一个字符串s，表示小说的内容，再给出一个list表示这些单词不参加统计，求字符串中出现频率最高的单词
# (如果有多个，返回字典序最小的那个)
#
# 样例
# Input: s = "Jimmy has an apple, it is on the table, he like it"
# excludeWords = ["a","an","the"]
# Output:"it"

"""
Algo:
D.S.: set, map, comparator

Solution:
Time: O(n) -- not only need the most, no need to sort all
Space: O(n)

If size of s is very very large, it may be a good idea to use trie tree

Corner cases:
"""

class Solution:
    """
    @param s: a string
    @param excludewords: a dict
    @return: the most frequent word
    """
    def frequentWord(self, s, excludewords):
        # Write your code here
        if not s:
            return ""
        exclSet = set()
        for w in excludewords:
            exclSet.add(w)
        novel = s.replace(",", "").split(" ")
        map = {}
        for w in novel:
            if w not in exclSet:
                if w not in map:
                    map[w] = 1
                else:
                    map[w] += 1
        maxOcc = 0
        res = ""
        for key, val in map.items():
            if val > maxOcc:
                res = key
                maxOcc = val
            if val == maxOcc:
                res = key if key < res else res
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
