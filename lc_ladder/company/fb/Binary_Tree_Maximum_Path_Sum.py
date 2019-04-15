#! /usr/local/bin/python3

# https://www.lintcode.com/problem/binary-tree-maximum-path-sum/my-submissions
# Example

Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

Example
Example 1:
	Input:  For the following binary tree（only one node）:
	2
	Output：2

Example 2:
	Input:  For the following binary tree:

      1
     / \
    2   3

	Output: 6

      -1
	Output: -1
    
"""
Algo: Divide-conquer
D.S.: Binary Tree

Solution:
can have a rotate,
path doesn't have to reach to leaves

Corner cases:
{-1} : return -1 not 0

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
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        single, multi = self.helper(root)
        return max(single, multi)

    def helper(self, node):
        if not node:
            return 0, 0
        l_single, l_multi = self.helper(node.left)
        r_single, r_multi = self.helper(node.right)

        single = max(l_single, r_single, 0) + node.val
        # multi init as node.val
        # if node is leaf and its value is -1, should return -1 instead of 0
        multi = node.val
        if node.left:
            multi = max(multi, l_multi)
        if node.right:
            multi = max(multi, r_multi)
        multi = max(multi, l_single + r_single + node.val)
        return single, multi

# Test Cases
if __name__ == "__main__":
    solution = Solution()
