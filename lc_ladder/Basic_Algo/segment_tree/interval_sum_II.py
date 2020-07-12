#! /usr/local/bin/python3

# https://leetcode.com/problems/range-sum-query-mutable/submissions/
# 在类的构造函数中给一个整数数组, 实现两个方法 query(start, end) 和 modify(index, value):
#
# 对于 query(start, end), 返回数组中下标 start 到 end 的 和。
# 对于 modify(index, value), 修改数组中下标为 index 上的数为 value.
# query 和 modify的时间复杂度需要为O(logN).

"""
Definition of SegmentTreeNode
"""
class SegmentTreeNode(object):
    def __init__(self, start, end, sum=0):
        self.start, self.end, self.sum = start, end, sum
        self.left, self.right = None, None

"""
Definition of SegmentTreeSum
"""
class SegmentTreeSum(object):
    def __init__(self, A):
        # To avoid invalid input and illegal len(A)
        self.arr = A if A is not None else []
        self.root = self._build(0, len(self.arr) - 1, self.arr)

    def _build(self, start, end, A):
        if start > end:
            return None
        elif start == end:
            return SegmentTreeNode(start, end, A[start])
        else:
            mid = (start + end) // 2
            root = SegmentTreeNode(start, end, 0)
            root.left = self._build(start, mid, A)
            root.right = self._build(mid + 1, end, A)
            root.sum = root.left.sum + root.right.sum
            return root

    def query(self, start, end):
        return self._query(self.root, start, end)

    def _query(self, root, start, end):
        if root is None:
            return 0
        if start > end: # unneccessary check
            return 0
        if start <= root.start and root.end <= end:
            return root.sum
        mid = (root.start + root.end) // 2
        ans = 0
        if mid >= start:
            ans += self._query(root.left, start, end)
        if mid + 1 <= end:
            ans += self._query(root.right, start, end)
        return ans

    def modify(self, index, value):
        self._modify(self.root, index, value)

    def _modify(self, root, index, value):
        # if index is out of boundry of segTree interval range
        if root.start == root.end and root.end != index:
            return
        if root.start == index and root.end == index:
            root.sum = value
            return
        mid = (root.start + root.end) // 2
        if index <= mid: # continue on left subtree
            self._modify(root.left, index, value)
        else:
            self._modify(root.right, index, value)
        root.sum = root.left.sum + root.right.sum
        return

class Solution:
    """
    @param: A: An integer array
    """
    def __init__(self, A):
        # do intialization if necessary
        self.segTree = SegmentTreeSum(A)

    """
    @param: start: An integer
    @param: end: An integer
    @return: The sum from start to end
    """
    def query(self, start, end):
        # write your code here
        return self.segTree.query(start, end)

    """
    @param: index: An integer
    @param: value: An integer
    @return: nothing
    """
    def modify(self, index, value):
        # write your code here
        self.segTree.modify(index, value)

if __name__ == "__main__":
    A = [1,2,7,8,5]
    s = Solution(A)
    print(s.query(0, 2)) #return 10.
    s.modify(0, 4) #change A[0] from 1 to 4.
    print(s.query(0, 0))
    print(s.query(0, 1)) #return 6.
    s.modify(2, 1) #change A[2] from 7 to 1.
    print(s.query(2, 2))
    print(s.query(2, 4)) #return 14.
