#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/balanced-binary-tree/description/


"""
Algo: Divide-and-Conquer
D.S.: Binary Tree

Solution_1:
Time: O(N ^ 2)， where N is # of nodes in the tree
isBalanced condition:
1. height of left and right child tree different no greater than 1, and
2. left and right tree are balanced as well

复杂度：
getHeight -> O(n), n is the # of nodes in the tree,  因为每个NODE 都要访问一遍
isBalanced -> O(n)，因为每个NODE 都要访问一遍，但是访问每个NODE的O(n) 中又要个getHeight O(n)
综合isBalanced复杂度O(n ^ 2)

Solution_2:
return type 将每层高度同时返回上来
降低复杂度是通过不在单独计算getHeight, 在一遍计算isBalanced访问每个Node的同时计算它的高度，从叶子往根算

Time: O(N) each node will be caculated only once.

Corner cases:
"""

class Solution_1(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1 and \
            (self.isBalanced(root.left) and self.isBalanced(root.right)):
            return True
        else:
            return False

    def getHeight(self, node):
        if node is None:
            return 0
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1

class Solution_2:
    def isBalanced(self, root: TreeNode) -> bool:
        is_balanced, height = self.helper(root)
        return is_balanced

    def helper(self, node):
        if not node:
            return True, 0
        left_is_balanced, left_height = self.helper(node.left)
        right_is_balanced, right_height = self.helper(node.right)
        if not left_is_balanced or not right_is_balanced:
            return False, 0 # height doesn't matter
        if abs(left_height - right_height) >= 2:
            return False, 0 # height doesn't matter
        return True, max(left_height, right_height) + 1


# Test Cases
if __name__ == "__main__":
	solution = Solution()
