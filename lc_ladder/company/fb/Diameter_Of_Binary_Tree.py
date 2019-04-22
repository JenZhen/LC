#! /usr/local/bin/python3

# https://www.lintcode.com/problem/diameter-of-binary-tree/description
# Example
# 给定一颗二叉树，您需要计算树的直径长度。 二叉树的直径是树中任意两个节点之间最长路径的长度。 此路径不一定会通过树根。
#
# 样例
# 给定一棵二叉树
#           1
#          / \
#         2   3
#        / \
#       4   5
# 返回3, 这是路径[4,2,1,3] 或者 [5,2,1,3]的长度.
# 注意事项
# 两个节点之间的路径长度由它们之间的边数表示。
#
# [1]


"""
Algo: Recursion, Divide and conquer
D.S.: Tree,

Solution:
针对每个node, return 他的左深度和右深度
更新global max vs (左深度 + 右深度)
返回上一层 左 、 右深度较大的一个
返回上一层的时候 计算新的深度一定要 + 1

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
    @param root: a root of binary tree
    @return: return a integer
    """
    max_dia = 0
    def diameterOfBinaryTree(self, root):
        # write your code here
        self.helper(root)
        return self.max_dia

    def helper(self, root):
        if not root.left and not root.right:
            return 0
        left = 0
        right = 0
        if root.left:
            left = self.helper(root.left) + 1
        if root.right:
            right = self.helper(root.right) + 1
        self.max_dia = max(self.max_dia, left + right)
        return max(left, right)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
