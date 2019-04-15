#! /usr/local/bin/python3

# https://www.lintcode.com/problem/sum-of-left-leaves/description
# Example
# 找出给定二叉树中，所有左叶子的值之和。
#
# 样例
# 样例1
#
# 输入：
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 输出：24
# 解释：这棵二叉树中，有两个左叶子结点，它们的值分别为9和15。因此返回24。
"""
Algo: Divide and Corner, tree, recursion
D.S.:

Solution:
树的divide conquer,
因为对待左右孩子不一样，所以要有2套control flow

Time: O(all tree nodes)
Space: O(1)
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
    @param root: t
    @return: the sum of all left leaves
    """
    def sumOfLeftLeaves(self, root):
        # Write your code here
        if not root:
            return 0
        ttl = 0
        if root.left:
            leftchild = root.left
            if leftchild.left is None and leftchild.right is None:
                # leftchild is leaf
                ttl += leftchild.val
            else:
                ttl += self.sumOfLeftLeaves(leftchild)
        if root.right:
            ttl += self.sumOfLeftLeaves(root.right)
        return ttl

# Test Cases
if __name__ == "__main__":
    solution = Solution()
