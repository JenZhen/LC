#! /usr/local/bin/python3

# https://lintcode.com/problem/scramble-string/description
# Example
# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

# Below is one possible representation of s1 = "great":

#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.

# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".

# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".

# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

# Challenge
# O(n3) time


"""
Algo: DP
D.S.:

Solution:
Time: O(n*nlogn)
TODO: 自己再好好做做
Corner cases:
"""


# DFS WITHOUT MEMO
class Solution:
    """
    @param s1: A string
    @param s2: Another string
    @return: whether s2 is a scrambled string of s1
    """
    def isScramble(self, s1, s2):
        # write your code here
        if len(s1)!=len(s2): return False
        if s1==s2: return True
        # l1, l2 check can be removed
        l1=list(s1); l2=list(s2)
        l1.sort();l2.sort()
        if l1!=l2: return False
        length=len(s1)
        for i in range(1,length):
            # rotate locates in sub level of s1, such as rg eat
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]): return True
            # rotaet locate in s1 level, such as eat gr
            if self.isScramble(s1[:i],s2[length-i:]) and self.isScramble(s1[i:],s2[:length-i]): return True
        return False


# Test Cases
if __name__ == "__main__":
    solution = Solution()
