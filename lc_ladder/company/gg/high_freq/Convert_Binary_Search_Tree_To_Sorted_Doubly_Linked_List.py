#! /usr/local/bin/python3

# LC426 no access
# Example
# Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
#
# Let's take the following BST as an example, it may help you understand the problem better:
#
# We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.
#
# The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.
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
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # base case
        if not root: return None
        head, tail = self.helper(root)
        # note(ZZ): I think it's better to make a list in recursion
        # and link head and tail only once in the main function
        return head

    def helper(self, root):
        '''construct a doubly-linked list, return the head and tail'''
        head, tail = root, root
        if root.left:
            left_head, left_tail = self.helper(root.left)
            left_tail.right = root
            root.left = left_tail
            head = left_head
        if root.right:
            right_head, right_tail = self.helper(root.right)
            right_head.left = root
            root.right = right_head
            tail = right_tail

        head.left = tail
        tail.right = head
        return head, tail

# Test Cases
if __name__ == "__main__":
    solution = Solution()
