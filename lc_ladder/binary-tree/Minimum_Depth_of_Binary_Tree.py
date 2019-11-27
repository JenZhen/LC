#!/usr/bin/python
import BinaryTree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from 
# he root node down to the nearest leaf node.

"""
Algo: DFS(Traverse) / Divide-and-Conquer
D.S.: Binary Tree

Solution:
1. Divide-and-Conquer
Calculate left/right sub tree then get the min + 1
Similar to "Maximum Depth of Binary Tree"

Time Complexity: O(N)

2. Hard to write a recursion. 

Corner cases:
Very Important
The difference from "Max"-verion of problem
 - if node has only one child, it should use the longer side

"""
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        elif root.left is None and root.right is not None:
            return self.minDepth(root.right) + 1
        elif root.left is not None and root.right is None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# Test Cases
if __name__ == "__main__":
	solution = Solution()