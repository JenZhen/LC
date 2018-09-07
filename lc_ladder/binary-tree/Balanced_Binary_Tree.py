#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/balanced-binary-tree/description/


"""
Algo: Divide and Conquer
D.S.: Binary Tree

Solution:
Time: O(N!) ??
isBalanced condition:
1. height of left and right child tree different no greater than 1, and
2. left and right tree are balanced as well

Follow-Up:
Add a field in TreeNode structure to note the depth of the node
Same node's information can be re-used
Time: O(N) each node will be caculated only once.

Corner cases:
"""

class Solution(object):
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


# Test Cases
if __name__ == "__main__":
	solution = Solution()
