#! /usr/local/bin/python3

# https://www.lintcode.com/problem/longest-uncommon-subsequence-i/description?_from=ladder&&fromId=18
# Example

"""
Algo:
D.S.:

Solution:
如果两个序列相同则return -1，如果两个序列不同就return两个序列中长的那个的长度
如果相对较短的字符串来算需要考虑短的是否是长的子串

Corner cases:
"""
class Solution:
    """
    @param a: a string
    @param b: a string
    @return: return a integer
    """
    def findLUSlength(self, a, b):
        # write your code here
        if a == b:
            return -1
        else:
            return max(len(a),len(b))


# Test Cases
if __name__ == "__main__":
    solution = Solution()
