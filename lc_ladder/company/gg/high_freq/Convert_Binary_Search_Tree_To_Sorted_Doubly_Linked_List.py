#! /usr/local/bin/python3

# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
# You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list.
# For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
#
# We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor,
# and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.
#
# Example 1:
# Input: root = [4,2,5,1,3]
# Output: [1,2,3,4,5]
# Explanation: The figure below shows the transformed BST. The solid line indicates the successor relationship,
# while the dashed line means the predecessor relationship.
#
# Example 2:
# Input: root = [2,1,3]
# Output: [1,2,3]
#
# Example 3:
# Input: root = []
# Output: []
# Explanation: Input is an empty tree. Output is also an empty Linked List.
#
# Example 4:
# Input: root = [1]
# Output: [1]
#
# Constraints:
#
# -1000 <= Node.val <= 1000
# Node.left.val < Node.val < Node.right.val
# All values of Node.val are unique.
# 0 <= Number of Nodes <= 2000
"""
Algo: inorder traversal, divide conquer
D.S.:

Solution:
Time: O(n) all nodes iterated once

Corner cases:
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        head, tail = self.helper(root)
        head.left = tail
        tail.right = head
        return head

    def helper(self, node):
        if not node:
            return None, None
        left_head, left_tail = self.helper(node.left)
        right_head, right_tail = self.helper(node.right)
        head, tail = None, None
        if left_tail is None:
            head = node
        else:
            head = left_head
            left_tail.right = node
            node.left = left_tail
        if right_head is None:
            tail = node
        else:
            tail = right_tail
            node.right = right_head
            right_head.left = node
        return head, tail

# Test Cases
if __name__ == "__main__":
    solution = Solution()
