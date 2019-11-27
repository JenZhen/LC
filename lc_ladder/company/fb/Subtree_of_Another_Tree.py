#! /usr/local/bin/python3

# https://www.lintcode.com/problem/subtree-of-another-tree/description
# Example
# 给定两个非空二叉树s和t，检查树t是否和树s的一个子树具有完全相同的结构和节点值。 s的子树是一个由s中的一个节点和该节点的后续组成的树。 树s本身也可以被视为自己的一个子树。
#
# Example
# 样例1:
#
# 给出树s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
# 给出树t:
#    4
#   / \
#  1   2
# 返回true，因为t和s的子树具有完全相同的结构和节点值。
# 样例2:
#
# 给出树s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# 给出树t:
#    4
#   / \
#  1   2
# 返回false.

"""
Algo: divide-conquer
D.S.: Tree

Solution:
2层Divide-and-Conquer

Corner cases:

"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param s: the s' root
    @param t: the t' root
    @return: whether tree t has exactly the same structure and node values with a subtree of s
    """
    def isSubtree(self, s, t):
        # Write your code here
        # 注意这里一定要考虑 s != None 应为要考虑s.left， s.right和t
        return s != None and (self.equal(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))

    def equal(self, s, t):
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False

        return s.val == t.val and self.equal(s.left, t.left) and self.equal(s.right, t.right)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
