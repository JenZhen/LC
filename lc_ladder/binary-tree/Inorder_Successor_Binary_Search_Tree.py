#!/usr/bin/python
import BinaryTree
# http://www.jiuzhang.com/solution/inorder-successor-in-binary-search-tree/
# Example
#      6
#    /  \
#   2    7
#  / \    \
# 1   4    9
#    / \  /
#   3   5 8
# Inorder traversal: 1,2,3,4,5,6,7,8,9
"""
Algo: DFS
D.S.: Binary Search Tree

Solution:
Given root = 6, p = 2, to find 3
    p.right.left.left....
Given root = 6, p = 1, to find 2
    p.right = None, return 2
Given root = 6, p = 9, to find None
    p.right = None, p is its parent right child
Given root = 6, p = 7.5, to find None
    7.left = None, p not in the tree return None
1. Iteration
Time Complexity O(N) iterate all nods
2. Divde and conquer (dfs)
Time Complexity O(logN) tree height if tree balanced (worst case also all tree nodes)

Corner cases:
"""

class Solution1(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        if root is None or p is None:
            return None
        successor = None
        cursor = root
        # try to find p
        while cursor is not None or cursor.val != p.val:
            if cursor.val > p.val:
                # update a new successor value, since moving to left
                # previous cursor could be a successor later
                successor = cursor
                cursor = cursor.left
            else:
                # no need to update successor when moving to right
                cursor = cursor.right
        # when exit while loop
        # 1. find p (cursor.val == p.val)
        #   1.1 if p has right child, left-most of p's right child
        #   1.2 if p has no right child, return successor
        # 2. cursor is None, cursor to find a node not in the tree
        #   return None
        if cursor.right is not None:
            cursor = cursor.right
            while cursor.left is not None:
                cursor = cursor.left
            return cursor
        else:
            return successor
        if cursor is None:
            return None


class Solution2(object):
    """
    @param root <TreeNode>: The root of the BST.
    @param p <TreeNode>: You need find the successor node of p.
    @return <TreeNode>: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        if root is None or p is None:
            return None

        if root.val <= p.val:
        # p on the right subtree
            return inorderSuccessor(root.right, p)
        else:
        # p on the left subtree
            leftSuccessor = inorderSuccessor(root.left, p)
            if leftSuccessor is None:
                return root
            else:
                return leftSuccessor



# Test Cases
if __name__ == "__main__":
	solution = Solution()
