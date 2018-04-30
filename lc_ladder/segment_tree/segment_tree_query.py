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

import sys
class Solution:
    """
    @param root: The root of segment tree.
    @param start: start value.
    @param end: end value.
    @return: The maximum number in the interval [start, end]
    """
    def query(self, root, start, end):
        # write your code here
        # Not considering root is None here
        # Can return None
        if start <= root.start and end >= root.end:
            return root.max

        mid = (root.start + root.end) // 2
        # Note:
        # max: sys.maxsize
        # min: -sys.minsize - 1 (minsize is not a member of sys)
        ans = -sys.maxsize - 1
        if mid >= start:
            # Important:
            # sublevel query use same start, end as question input
            ans = max(ans, self.query(root.left, start, end))
        if mid + 1 <= end:
            ans = max(ans, self.query(root.right, start, end))
        return ans
