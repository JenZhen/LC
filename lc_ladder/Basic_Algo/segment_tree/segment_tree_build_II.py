#! /usr/local/bin/python3

# Time Complexity:
# Build:  O(n)
# Query:  O(logn)
# Modify: O(logn)

"""
Definition of SegmentTreeNode:
"""

class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None

class Solution:
    """
    @param A: a list of integer
    @return: The root of Segment Tree
    """
    def build(self, A):
        # write your code here
        return self.helper(0, len(A) - 1, A)

    def helper(self, start, end, A):
        if start > end:
            return None

        root = SegmentTreeNode(start, end, A[start])
        if start == end:
            return root

        mid = (start + end) // 2
        root.left = self.helper(start, mid, A)
        root.right = self.helper(mid + 1, end, A)

        if root.left is not None:
            root.max = max(root.max, root.left.max)
        if root.right is not None:
            root.max = max(root.max, root.right.max)
        return root
