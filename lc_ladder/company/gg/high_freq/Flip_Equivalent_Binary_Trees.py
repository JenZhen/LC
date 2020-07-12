#! /usr/local/bin/python3

# https://leetcode.com/problems/flip-equivalent-binary-trees/
# Example
# For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
#
# A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
#
# Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.
#
#
#
# Example 1:
#
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.
"""
Algo: divide-conquer,
D.S.: binary tree

Solution1:
Time: O(min(size of tree1, size of tree2)) -- 每个Node都被访问1遍
Time: O(min(height of tree1, height of tree2)

Solution2:
Time: O(size of tree1 + size of tree2) -- 每个Node都被访问1遍
Time: O(size of tree1 + size of tree2)

Corner cases:
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1: return not root2
        if not root2: return not root1
        if root1.val != root2.val:
            return False
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2s:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        val1, val2 = [], []
        self.dfs(root1, val1)
        self.dfs(root2, val2)
        print(val1)
        print(val2)
        return val1 == val2

    def dfs(self, node, val):
        if not node: return
        val.append(node.val)
        l = node.left.val if node.left else -1
        r = node.right.val if node.right else -1

        if l < r:
            self.dfs(node.left, val)
            self.dfs(node.right, val)
        else:
            self.dfs(node.right, val)
            self.dfs(node.left, val)
        val.append('#')
# Test Cases
if __name__ == "__main__":
    solution = Solution()
