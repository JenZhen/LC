#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/balanced-binary-tree/description/


"""
Algo: Divide and Conquer
D.S.: Binary Tree

Solution1:
Time: O(N ^ 2)， where N is # of nodes in the tree
isBalanced condition:
1. height of left and right child tree different no greater than 1, and
2. left and right tree are balanced as well

复杂度：
getHeight -> O(n), n is the # of nodes in the tree,  因为每个NODE 都要访问一遍
isBalanced -> O(n)，因为每个NODE 都要访问一遍，但是访问每个NODE的O(n) 中又要个getHeight O(n)
综合isBalanced复杂度O(n ^ 2)

Follow-Up:
Add a field in TreeNode structure to note the depth of the node
Same node's information can be re-used
降低复杂度是通过不在单独计算getHeight, 在一遍计算isBalanced访问每个Node的同时计算它的高度，从叶子往根算

Time: O(N) each node will be caculated only once.

Corner cases:
"""

class Solution1(object):
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

class Solution1(object):
    class Height(object):
        def __init__(self):
            self.height = 0

    # input root of the tree, height of the root (init a Height object for root)
    # return bool (is balanced or not)
    def isBalanced(self, root, root_height):
        if not root:
            return True

        lh = Height()
        rh = Height()

        l_balanced = self.isBalanced(root.left, lh)
        r_balanced = self.isBalanced(root.right, rh)

        root_height.height = max(lh, rh) + 1

        if abs(lh - rh) <= 1 and l_balanced and r_balanced:
            return True
        return False

# root = TreeNode(10)
# root_height = Height(0)
# return isBalanced(root, root_height)

# Test Cases
if __name__ == "__main__":
	solution = Solution()
