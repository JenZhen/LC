#! /usr/local/bin/python3

# Time Complexity:
# Build:  O(n)
# Query:  O(logn)
# Modify: O(logn)
"""
Definition of SegmentTreeNode:
"""

# Complexity:
# Time: O(logn) (tree height logn)

class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None

class Solution:
    """
    @param: root: The root of segment tree.
    @param: start: start value.
    @param: end: end value.
    @return: The count number in the interval [start, end]
    """
    def query(self, root, start, end):
        # write your code here
        if root is None:
            return 0
        if start <= root.start and root.end <= end:
            return root.count
        ans = 0
        mid = (root.start + root.end) // 2
        if mid >= start:
            ans += self.query(root.left, start, end)
        if mid + 1 <= end:
            ans += self.query(root.right, start, end)
        return ans
