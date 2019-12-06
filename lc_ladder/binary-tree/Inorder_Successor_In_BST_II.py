#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/inorder-successor-in-bst-ii
# Example

"""
Algo: Tree-Iteration
D.S.: Binary Tree

Solution:
Time Complexity: O(N)
Space Complexity: O(N)

Corner cases:
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # 1. if node has right child
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        # 2. if node successor on upper tree
        # if node is its father's left child, it's father is successor
        if node.parent:
            if node.parent.left == node:
                return node.parent

        # 3. if node is its father's right child,
        # trace its grandfather till it has a left child
        # corner case!
        father = node.parent
        while father:
            if father.right == node:
                node = father
                father = father.parent
            else:
                return father
        return None

# Test Cases
if __name__ == "__main__":
	solution = Solution()
