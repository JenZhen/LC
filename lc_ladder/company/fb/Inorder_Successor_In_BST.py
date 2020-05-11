#! /usr/local/bin/python3

# https://www.lintcode.com/problem/inorder-successor-in-bst/description
# Example
# 给定一个二叉查找树(什么是二叉查找树)，以及一个节点，求该节点在中序遍历的后继，如果没有则返回null
#
# Example
# 样例 1:
#
# 输入: tree = {1,#,2}, node value = 1
# 输出: 2
# 解释:
#   1
#    \
#     2
# 样例 2:
#
# 输入: tree = {2,1,3}, node value = 1
# 输出: 2
# 解释:
#     2
#    / \
#   1   3
# 二叉树的表示
#
# Challenge
# O(h)，其中h是BST的高度。
#
# Notice
# 保证p是给定二叉树中的一个节点。(您可以直接通过内存地址找到p)


"""
Algo:
D.S.:

首先要确定中序遍历的后继:

如果该节点有右子节点, 那么后继是其右子节点的子树中最左端的节点
如果该节点没有右子节点, 那么后继是离它最近的祖先, 该节点在这个祖先的左子树内.
使用循环实现:

查找该节点, 并在该过程中维护上述性质的祖先节点
查找到后, 如果该节点有右子节点, 则后继在其右子树内; 否则后继就是维护的那个祖先节点
使用递归实现:

如果根节点小于或等于要查找的节点, 直接进入右子树递归
如果根节点大于要查找的节点, 则暂存左子树递归查找的结果, 如果是 null, 则直接返回当前根节点; 反之返回左子树递归查找的结果.
在递归实现中, 暂存左子树递归查找的结果就相当于循环实现中维护的祖先节点.

Solution1:
利用BST 性质
1. 先找到P节点
2. 同时记录STACK 只记录比较大的
3. 找到P之后，先看他有没有右孩子，再stack中记录的比他大的就是in order successor

Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        cur = root
        stack = [root]
        while cur:
            if cur == p:
                break
            if cur.val > p.val:
                stack.append(cur.left)
                cur = cur.left
            else:
                stack.pop()
                stack.append(cur.right)
                cur = cur.right
        if cur == None: return None
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        stack.pop()
        if stack:
            return stack.pop()
        else:
            return None

class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if not root or not p:
            return None
        suc = None
        cur = root
        while cur != None and cur.val != p.val:
            if cur.val < p.val:
                cur = cur.right
            else:
                suc = cur
                cur = cur.left
        if cur == None:
            # p not found
            return None

        # p found
        if p.right:
            cur = p.right
            while cur.left:
                cur = cur.left
            return cur
        else:
            return suc


# Test Cases
if __name__ == "__main__":
    solution = Solution()
