#! /usr/local/bin/python3

import sys
"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

"""
Definition of SegmentTreeMinNode
"""
class SegmentTreeMinNode(object):
    def __init__(self, start, end, min=-sys.maxsize-1):
        self.start, self.end, self.min = start, end, min
        self.left, self.right = None, None

"""
Definition of SegmentTreeMin
"""
class SegmentTreeMin(object):
    def __init__(self, A):
        self.arr = A if A is not None else []
        self.root = self._build(0, len(self.arr) - 1, self.arr)

    def _build(self, start, end, A):
        if start > end:
            return None
        elif start == end:
            return SegmentTreeMinNode(start, end, A[start])
        else:
            mid = (start + end) // 2
            root = SegmentTreeMinNode(start, end, A[start])
            root.left = self._build(start, mid, A)
            root.right = self._build(mid + 1, end, A)
            root.min = min(root.left.min, root.right.min)
            return root

    def query(self, start, end):
        return self._query(self.root, start, end)

    def _query(self, root, start, end):
        if root is None or start > end: #start > end meaning out of range
            return None
        if start <= root.start and root.end <= end:
            return root.min
        mid = (root.start + root.end) // 2
        ans = sys.maxsize
        if mid >= start: # need to query left sub tree
            ans = min(ans, self._query(root.left, start, end))
        if mid + 1 <= end:
            ans = min(ans, self._query(root.right, start, end))
        return ans


class Solution:
    """
    @param A: An integer array
    @param queries: An query list
    @return: The result list
    """
    def intervalMinNumber(self, A, queries):
        # write your code here
        segTree = SegmentTreeMin(A)
        ans = []
        for q in queries:
            ans.append(segTree.query(q.start, q.end))
        return ans

if __name__ == "__main__":
    testCases = [
        {
            "A": [1,2,7,8,5],
            "queries": [Interval(1,2), Interval(0,4), Interval(2,4)]
        },
    ]
    s = Solution()
    for t in testCases:
        A = t["A"]
        queries = t["queries"]
        res = s.intervalMinNumber(A, queries)
        print("res: %s" %repr(res))
