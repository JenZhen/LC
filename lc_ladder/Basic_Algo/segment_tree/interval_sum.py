#! /usr/local/bin/python3

# 给定一个整数数组（下标由 0 到 n-1，其中 n 表示数组的规模），以及一个查询列表。每一个查询列表有两个整数 [start, end] 。
# 对于每个查询，计算出数组中从下标 start 到 end 之间的数的总和，并返回在结果列表中。
#
# 每一次查询的时间复杂度为O(logN)
"""
Definition of Interval
"""
class Interval(object):
    def __init__(self, start, end):
        self.start, self.end = start, end

"""
Definition of SegmentTreeNode
"""
class SegmentTreeNode(object):
    def __init__(self, start, end, sum=0):
        self.start, self.end, self.sum = start, end, sum

"""
Definition of SegmentTreeSum
"""
class SegmentTreeSum(object):
    def __init__(self, A):
        self.arr = A if A != None else []
        self.root = self._build(0, len(self.arr) - 1, self.arr)

    def _build(self, start, end, arr):
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(start, end, arr[start])
        if start < end:
            mid = (start + end) // 2
            root = SegmentTreeNode(start, end)
            root.left = self._build(start, mid, arr)
            root.right = self._build(mid + 1, end, arr)
            root.sum = root.left.sum + root.right.sum
            return root

    def query(self, start, end):
        return self._query(self.root, start, end)

    def _query(self, root, start, end):
        if root is None:
            return None
        if start > end:
            return None
        if start <= root.start and root.end <= end:
            return root.sum
        mid = (root.start + root.end) // 2
        ans = 0
        if mid >= start:
            ans += self._query(root.left, start, end)
        if mid + 1 <= end:
            ans += self._query(root.right, start, end)
        return ans

class Solution:
    """
    @param A: An integer list
    @param queries: An query list
    @return: The result list
    """
    def intervalSum(self, A, queries):
        # write your code here
        segTree = SegmentTreeSum(A)
        if segTree.root is None:
            print('root is None')
            return None
        ans = []
        for q in queries:
            start, end = q.start, q.end
            sum = segTree.query(start, end)
            ans.append(sum)
        return ans

if __name__ == "__main__":
    testCases = [
        {"A": [1,2,7,8,5],
         "queries": [Interval(0,4), Interval(1,2), Interval(2,4)]
        },
        {"A": None,
        "queries": [Interval(0,4), Interval(1,2), Interval(2,4)]
        }
    ]
    solution = Solution()
    for test in testCases:
        A = test["A"]
        queries = test["queries"]
        ans = solution.intervalSum(A, queries)
        print("Queried sum: %s" %repr(ans))
