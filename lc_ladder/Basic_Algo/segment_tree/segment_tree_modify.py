#! /usr/local/bin/python3

"""
Definition of SegmentTreeNode:
"""

# Complexity:
# Time: O(logn) (tree height logn)

class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of segment tree.
    @param index: index.
    @param value: value
    @return: nothing
    """
    def modify(self, root, index, value):
        # write your code here
        if root.start == index and root.end == index:
            root.max = value
            return

        mid = (root.start + root.end) // 2
        if index <= mid: # at left sub tree
            self.modify(root.left, index, value)
        else:
            self.modify(root.right, index, value)
        root.max = max(root.left.max, root.right.max)
