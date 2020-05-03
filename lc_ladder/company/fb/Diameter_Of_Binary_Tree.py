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
Algo: Recursion, Divide-and-Conquer
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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        self.dfs(root)
        return self.res - 1

    def dfs(self, node):
        if not node: return 0
        left_depth = self.dfs(node.left)
        right_depth = self.dfs(node.right)

        self.res = max(self.res, left_depth + right_depth + 1)

        return max(left_depth, right_depth) + 1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
