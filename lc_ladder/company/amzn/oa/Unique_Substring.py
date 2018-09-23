#! /usr/local/bin/python3

# Requirement
# Example
# 给出一个字符串 s，找出所有的不同的长度为 k 的它的子串，并将结果按照字典序排序
#
# 样例
# Input: s = "caaab"
# k = 2
# Output:["aa","ab","ca"]

"""
Algo: Sort 就有nlogn
D.S.:

Solution:
1. Time: O(nlogn)


Corner cases:
"""

class Solution1:
    """
    @param s: a string
    @param k: an integer
    @return: all unique substring
    """
    def uniqueSubstring(self, s, k):
        # Write your code here
        ss = set([])
        if not s or not k:
            return []
        if k >= len(s):
            return []
        for i in range(k, len(s) + 1):
            sub = s[i - k : i]
            if sub not in ss:
                ss.add(sub)
        return [i for i in sorted(ss)]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
