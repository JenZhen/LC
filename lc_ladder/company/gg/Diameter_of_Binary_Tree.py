#! /usr/local/bin/python3

# https://www.lintcode.com/problem/diameter-of-binary-tree/description?_from=ladder&&fromId=18
# Example
# 给定二叉树，您需要计算树的直径长度。 二叉树的直径是树中任意两个节点之间最长路径的长度。 此路径可能会也可能不会通过根。
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
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        # write your code here
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
            self.res = max(self.res, leftSingle + 1)
            return leftSingle + 1, 0
        elif not node.left:
            rightSingle, rightDouble = self.helper(node.right)
            self.res = max(self.res, rightSingle + 1)
            return rightSingle + 1, 0
        else:
            leftSingle, leftDouble = self.helper(node.left)
            print('left', leftSingle, leftDouble)
            rightSingle, rightDouble = self.helper(node.right)
            print('right', rightSingle, rightDouble)
            single = max(leftSingle + 1, rightSingle + 1)
            double = leftSingle + 1 + rightSingle + 1
            print(single, double)
            self.res = max(self.res, single, double)
            return single, double

# Test Cases
if __name__ == "__main__":
    solution = Solution()
