#! /usr/local/bin/python3

# https://www.lintcode.com/problem/permutation-in-string/description
# Example
# 给定两个字符串s1和s2，如果s2包含s1的排列，则写一个函数返回true。 换句话说，第一个字符串的排列之一是第二个字符串的substring。
#
# 样例
# 样例1:
#
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: true
# 解释: s2包含s1的一个排列("ba").
# 样例2:
#
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: false
# 注意事项
# 输入的字符串只包含小写字母。
# 两个字符串的长度范围都为[1, 10,000]。
"""
Algo: sliding window
D.S.:

Solution:
Time: O(n) -- len of s2
Space: O(m * n) -- m len of s1, n len of s2

sliding window

Corner cases:
注意一个细节，s1 比s2长，直接返回错

"""

class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """
    def checkInclusion(self, s1, s2):
        # write your code here
        if not s1 or not s2 or len(s1) > len(s2):
            return False
        l1 = len(s1)
        l2 = len(s2)
        dic = [0] * 26
        for i in range(l1):
            dic[ord(s2[i]) - ord('a')] += 1

        l, r = 0, l1 - 1
        while True:
            if self.isPerm(s1, dic[:]):
                return True
            if r + 1 < l2:
                r += 1
                dic[ord(s2[r]) - ord('a')] += 1
                dic[ord(s2[l]) - ord('a')] -= 1
                l += 1
            else:
                break
        return False

    def isPerm(self, s1, dic):
        for i in s1:
            dic[ord(i) - ord('a')] -= 1
        for ele in dic:
            if ele != 0:
                return False
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
