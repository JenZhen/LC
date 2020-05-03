#! /usr/local/bin/python3

# https://www.lintcode.com/problem/find-all-anagrams-in-a-string/description
# Example
# 给定一个字符串 s 和一个 非空字符串 p ，找到在 s 中所有关于 p 的字谜的起始索引。
# 字符串仅由小写英文字母组成，字符串 s 和 p 的长度不得大于 40,000。
# 输出顺序无关紧要。
#
# 样例
# 样例 1:
#
# 输入 : s = "cbaebabacd", p = "abc"
# 输出 : [0, 6]
# 说明 :
# 子串起始索引 index = 0 是 "cba"，是"abc"的字谜。
# 子串起始索引 index = 6 是 "bac"，是"abc"的字谜。

"""
Algo:
D.S.: array, anagrams, 包含关系
类似：minimum window substring
https://www.lintcode.com/problem/minimum-window-substring/

Solution:
Time: O(n)
Space：O(256)

Follow up: https://leetcode.com/problems/find-all-anagrams-in-a-string/
Time: O(n)
Time: O(1)
Sliding window

Corner cases:
"""

class Solution:
    """
    @param s: a string
    @param p: a string
    @return: a list of index
    """
    def findAnagrams(self, s, p):
        # write your code here
        if not s or not p or len(s) < len(p):
            return []
        source = [0] * 256
        target = self.init_target(p)
        len_s = len(s)
        len_p = len(p)
        for i in range(len(p)):
            source[ord(s[i])] += 1
        i = 0
        res = []
        while i + len_p - 1 < len_s:
            if self.isAnagram(source, target):
                res.append(i)
            source[ord(s[i])] -= 1
            if i + len_p < len_s:
                source[ord(s[i + len_p])] += 1
            else:
                return res
            i += 1
        return res

    def init_target(self, p):
        target = [0] * 256
        for i in p:
            target[ord(i)] += 1
        return target

    def isAnagram(self, s, p):
        for i in range(256):
            if s[i] != p[i]:
                return False
        return True

class Solution_FollowUP:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if s is None or p is None: return []
        s_len = len(s)
        p_len = len(p)
        if s_len < p_len:
            return []

        res = []

        # init p_map
        p_map = [0] * 26
        for c in p:
            p_map[ord(c) - ord('a')] += 1
        # init s_map
        s_map = [0] * 26
        for i in range(p_len):
            s_map[ord(s[i]) - ord('a')] += 1
        # check the first set
        if self.match(s_map, p_map):
            res.append(0)

        for i in range(p_len, s_len):
            s_map[ord(s[i]) - ord('a')] += 1
            s_map[ord(s[i - p_len]) - ord('a')] -= 1
            if self.match(s_map, p_map):
                # be careful about index
                res.append(i - p_len + 1)
        return res

    def match(self, s_map, p_map):
        for i in range(26):
            if s_map[i] != p_map[i]:
                return False
        return True
# Test Cases
if __name__ == "__main__":
    solution = Solution()
