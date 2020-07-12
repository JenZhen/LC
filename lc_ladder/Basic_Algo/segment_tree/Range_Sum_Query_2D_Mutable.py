#! /usr/local/bin/python3

# https://leetcode.com/problems/range-sum-query-2d-mutable/submissions/
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
#
# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
#
# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10
# Note:
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.

"""
Time: TLE
Build: O(mn)
Query: O(logmn)
Modify: O(logmn)

"""

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return None
        m, n = len(matrix), len(matrix[0])
        self.segmentTree = SegmentTree(matrix)

    def update(self, row: int, col: int, val: int) -> None:
        self.segmentTree.modify(row, col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.segmentTree.query(row1, col1, row2, col2)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
class SegmentTreeNode:
    def __init__(self, r1, c1, r2, c2, sum = 0):
        self.r1, self.c1, self.r2, self.c2 = r1, c1, r2, c2
        self.lu, self.ru, self.lb, self.rb = None, None, None, None
        self.sum = sum

class SegmentTree:
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.root = self._build(0, 0, m - 1, n - 1, matrix)

    def _build(self, r1, c1, r2, c2, matrix):
        if r1 > r2 or c1 > c2:
            return
        if r1 == r2 and c1 == c2:
            # at one cell
            return SegmentTreeNode(r1, c1, r2, c2, matrix[r1][c1])

        mid_r = (r1 + r2) // 2
        mid_c = (c1 + c2) // 2

        node = SegmentTreeNode(r1, c1, r2, c2, 0)
        node.lu = self._build(r1, c1, mid_r, mid_c, matrix)
        node.ru = self._build(r1, mid_c + 1, mid_r, c2, matrix)
        node.lb = self._build(mid_r + 1, c1, r2, mid_c, matrix)
        node.rb = self._build(mid_r + 1, mid_c + 1, r2, c2, matrix)

        node.sum += node.lu.sum if node.lu else 0
        node.sum += node.ru.sum if node.ru else 0
        node.sum += node.lb.sum if node.lb else 0
        node.sum += node.rb.sum if node.rb else 0
        return node

    def query(self, r1, c1, r2, c2):
        return self._query(self.root, r1, c1, r2, c2)

    def _query(self, node, r1, c1, r2, c2):
        if not node: return 0
        # no intersection
        if node.r1 > r2 or node.r2 < r1 or node.c1 > c2 or node.c2 < c1:
            return 0
        if r1 <= node.r1 and c1 <= node.c1 and r2 >= node.r2 and c2 >= node.c2:
            return node.sum
        return self._query(node.lu, r1, c1, r2, c2) + self._query(node.lb, r1, c1, r2, c2) + self._query(node.ru, r1, c1, r2, c2) + self._query(node.rb, r1, c1, r2, c2)

    def modify(self, r, c, val):
        self._modify(self.root, r, c, val)

    def _modify(self, node, r, c, val):
        if not node: return
        if node.r1 == node.r2 and node.c1 == node.c2:
            if node.r1 == r and node.c1 == c:
                node.sum = val
        else:
            self._modify(node.lu, r, c, val)
            self._modify(node.ru, r, c, val)
            self._modify(node.lb, r, c, val)
            self._modify(node.rb, r, c, val)
            node.sum = 0
            node.sum += node.lu.sum if node.lu else 0
            node.sum += node.ru.sum if node.ru else 0
            node.sum += node.lb.sum if node.lb else 0
            node.sum += node.rb.sum if node.rb else 0
