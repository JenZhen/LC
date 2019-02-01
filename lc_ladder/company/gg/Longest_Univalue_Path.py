#! /usr/local/bin/python3

# https://www.lintcode.com/problem/longest-univalue-path/description?_from=ladder&&fromId=18
# Example
# 给定一颗二叉树，找到路径中每个节点具有相同值的最长路径的长度。 此路径可能会也可能不会通过根节点。
#
# 样例
# 样例 1:
#
# 输入:
#
#               5
#              / \
#             4   5
#            / \   \
#           1   1   5
# 输出:
# 2
# 样例 2:
#
# 输入:
#
#               1
#              / \
#             4   5
#            / \   \
#           4   4   5
# 输出:
# 2
# 注意事项
# 1.两个节点之间的路径长度由它们之间的边数表示。
# 2.给定的二叉树不超过10000个节点。 树的高度不超过1000。
"""
Algo: divide and conquer
D.S.: binary tree

Solution:


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
    @param root:
    @return: the length of the longest path where each node in the path has the same value
    """
    def longestUnivaluePath(self, root):
        # Write your code here
        if not root:
            return 0

        import sys
        self.res = -sys.maxsize
        single, double = self.helper(root)
        return self.res

    def helper(self, node):
        if not node.left and not node.right:
            self.res = max(self.res, 0)
            return 0, 0
        elif not node.right:
            leftSingle, leftDouble = self.helper(node.left)
            if node.val == node.left.val:
                single = leftSingle + 1
                double = 0
                self.res = max(self.res, single)
                return single, double
            else:
                return 0, 0
        elif not node.left:
            rightSingle, rightDouble = self.helper(node.right)
            if node.val == node.right.val:
                single = rightSingle + 1
                double = 0
                self.res = max(self.res, single)
                return single, double
            else:
                return 0, 0
        else:
            leftSingle, leftDouble = self.helper(node.left)
            rightSingle, rightDouble = self.helper(node.right)
            if node.val != node.left.val and node.val != node.right.val:
                return 0, 0
            elif node.val != node.right.val:
                single = leftSingle + 1
                double = 0
                self.res = max(self.res, single)
                return single, double
            elif node.val != node.left.val:
                single = rightSingle + 1
                double = 0
                self.res = max(self.res, single)
                return single, double
            else:
                single = max(leftSingle, rightSingle) + 1
                double = leftSingle + 1 + rightSingle + 1
                self.res = max(self.res, single, double)
                return single, double

# Test Cases
if __name__ == "__main__":
    solution = Solution()
