#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo:
D.S.:

Solution:
1. 用map的粗暴做法
2. 用array[256] extra space, 过一遍字符串，过一遍数数组


Corner cases:
"""

class Solution1:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        if len(str) == 0:
            return ""
        dic = {}
        for i in range(len(str)):
            if str[i] not in dic:
                dic[str[i]] = [1, i]
            else:
                dic[str[i]][0] += 1
        pos = len(str)
        res = ""
        for key, val in dic.items():
            if val[0] == 1 and val[1] < pos:
                pos = val[1]
                res = key
        return res

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        if len(str) == 0:
            return ""
        lot = [-1] * 256
        for i in range(len(str)):
            c = str[i]
            if lot[ord(c)] == -1: # not visited
                lot[ord(c)] = i # idx
            elif lot[ord(c)] >= 0: # visited once
                lot[ord(c)] = -2 # visited more than once
            """
            else:
                continue  #do nothing if  == -2
            """
        import sys
        res = sys.maxsize
        for i in lot:
            if i >= 0:
                res = min(res, i)
        return str[res]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
