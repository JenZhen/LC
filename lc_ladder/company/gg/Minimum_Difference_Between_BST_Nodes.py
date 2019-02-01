#! /usr/local/bin/python3

# https://www.lintcode.com/problem/minimum-difference-between-bst-nodes/description?_from=ladder&&fromId=18
# Example
# 给定一个确定根的二叉搜索树，返回树中任意两个不同节点的值的最小差。
#
# 样例
# 输入: root = {4,2,6,1,3,#,#}
# 输出: 1
# 解答:
# 请留意，root是一个树节点的结构，而非一个普通数组。
#
# 给定的树{4,2,6,1,3,#,#}的样子如下图：
#
#           4
#         /   \
#       2      6
#      / \
#     1   3
#
# 在这棵树中，最小数值差距为 1, 它出现在node 1 与 node 2 之间, 也同时存在 node 3 与 node 2之间
# 注意事项
# 1.这棵二叉搜索树的大小在 2 到100之间。
# 2.这棵二叉搜索树是存在的，每个点的数值是一个整数，而且每个点的数值将会是不同的。


"""
Algo: inorder dfs
D.S.: BST

Solution:
1. in-order dfs,
2. TODO：尝试用iterator 的方式来做

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
    @param root: the root
    @return: the minimum difference between the values of any two different nodes in the tree
    """
    def minDiffInBST(self, root):
        # Write your code here
        import sys
        self.pre = None
        self.minDiff = sys.maxsize
        self.helper(root)
        return self.minDiff

    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        if self.pre == None:
            self.pre = node.val
        else:
            self.minDiff = min(self.minDiff, node.val - self.pre)
            self.pre = node.val
        self.helper(node.right)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
