#! /usr/local/bin/python3

# import math # for python# (1 + 2) / 2 = 1.5
"""
Definition of SegmentTreeNode:
"""

# Complexity:
# Time: O(n): Interval of length n, tree leaf level n nodes, in total n

class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None

class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        # write your code here
        if start > end:
            return None
        root = SegmentTreeNode(start, end)
        if start == end:
            return root

        # mid = math.floor((start + end) / 2)
        mid = (start + end) // 2 # // is floor-division
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        return root # DO NOT forget to return root!!
