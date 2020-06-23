#! /usr/local/bin/python3

# https://leetcode.com/problems/construct-binary-tree-from-string/submissions/
# Example
# You need to construct a binary tree from a string consisting of parenthesis and integers.
# The whole input represents a binary tree. It contains an integer followed by zero,
# one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
# You always start to construct the left child node of the parent first if it exists.
#
# Example:
# Input: "4(2(3)(1))(6(5))"
# Output: return the tree root node representing the following tree:
#
#        4
#      /   \
#     2     6
#    / \   /
#   3   1 5
# Note:
# There will only be '(', ')', '-' and '0' ~ '9' in the input string.
# An empty tree is represented by "" instead of "()".
"""
Algo: Recursion, stack
D.S.:

Solution_1:
类似：calculator

Time: O(N)
Space: O(1)

Solution_2:
Time: O(N)
Space: O(1)
Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_Recursion(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        self.i = 0
        if not s:
            return None
        return self.helper(s)

    def helper(self, s):

        if self.i > len(s):
            return

        sign = 1
        if s[self.i] == '-':
            sign = -1
            self.i += 1

        val = 0
        while self.i < len(s) and s[self.i] != '(' and s[self.i] != ')':
            val = val * 10 + int(s[self.i])
            self.i += 1

        node = TreeNode(val * sign)
        if self.i < len(s) and s[self.i] == '(':
            self.i += 1
            node.left = self.helper(s)
        if self.i < len(s) and s[self.i] == '(':
            self.i += 1
            node.right = self.helper(s)
        if self.i < len(s) and s[self.i] == ')':
            self.i += 1
        return node



class Solution_Iteration(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s: return None

        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
                continue
            val = 0
            sign = 1
            if s[i] == '-':
                sign = -1
                i += 1
            if i < len(s) and s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    val = val * 10 + int(s[i])
                    i += 1
                new_node = TreeNode(val * sign)

                if stack:
                    parent = stack[-1]
                    if parent.left:
                        parent.right = new_node
                    else:
                        parent.left = new_node
                stack.append(new_node)
            if i < len(s) and s[i] == ')': # marking close of a node, which has no more child, pop it from stack
                stack.pop()
            i += 1
        return stack[0]
# Test Cases
if __name__ == "__main__":
    solution = Solution()
