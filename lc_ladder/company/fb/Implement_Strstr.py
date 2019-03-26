#! /usr/local/bin/python3

# https://www.lintcode.com/problem/implement-strstr/description
# Example
# 对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。
#
# 样例
# 样例  1:
# 	输入: source = "source" ， target = "target"
# 	输出:-1
#
# 	样例解释:
# 	如果source里没有包含target的内容，返回-1
#
# 样例 2:
# 	输入: source = "abcdabcdefg" ，target = "bcd"
# 	输出: 1
#
# 	样例解释:
# 	如果source里包含target的内容，返回target在source里第一次出现的位置
#
# 挑战
# O(n2)的算法是可以接受的。如果你能用O(n)的算法做出来那更加好。（提示：KMP）
#
# 说明
# 在面试中我是否需要实现KMP算法？
#
# 不需要，当这种问题出现在面试中时，面试官很可能只是想要测试一下你的基础应用能力。当然你需要先跟面试官确认清楚要怎么实现这个题。


"""
Algo: KMP
D.S.:

Solution:

Corner cases:
"""


class Solution1:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if source is None or target is None:
            return -1
        len_s, len_t = len(source), len(target)
        for i in range(len_s - len_t + 1):
            j = 0
            while j < len_t:
                if source[i + j] != target[j]:
                    break
                else:
                    j += 1
            if j == len_t:
                return i
        return -1

class Solution_KMP:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        # TODO:

# Test Cases
if __name__ == "__main__":
    solution = Solution()
