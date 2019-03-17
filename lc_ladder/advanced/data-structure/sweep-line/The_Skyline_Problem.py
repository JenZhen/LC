#! /usr/local/bin/python3

# https://www.lintcode.com/problem/the-skyline-problem/description
# Example
# 水平面上有 N 座大楼，每座大楼都是矩阵的形状，可以用一个三元组表示 (start, end, height)，
# 分别代表其在x轴上的起点，终点和高度。大楼之间从远处看可能会重叠，求出 N 座大楼的外轮廓线。
#
# 外轮廓线的表示方法为若干三元组，每个三元组包含三个数字 (start, end, height)，代表这段轮廓的起始位置，终止位置和高度。
#
# 样例
# 给出三座大楼：
#
# [
#   [1, 3, 3],
#   [2, 4, 4],
#   [5, 6, 1]
# ]
# 外轮廓线为：
#
# [
#   [1, 2, 3],
#   [2, 4, 4],
#   [5, 6, 1]
# ]
# 注意事项
# 请注意合并同样高度的相邻轮廓，不同的轮廓线在x轴上不能有重叠。

"""
Algo: Sweepline
D.S.: hashheap, treemap

Solution:

# TODO: Need a better solution for heap removal by key

Corner cases:
"""


class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def buildingOutline(self, buildings):
        # write your code here
        points = []
        for index, (start, end, height) in enumerate(buildings):
            points.append((start, height, index, True))
            points.append((end, height, index, False))
        points = sorted(points)

        maxheap = HashHeap(desc=True)
        intervals = []
        last_position = None
        for position, height, index, is_start in points:
            max_height = maxheap.top()[0] if maxheap.size else 0
            self.merge_to(intervals, last_position, position, max_height)
            if is_start:
                maxheap.push((height, index))
            else:
                maxheap.remove((height, index))
            last_position = position

        return intervals

    def merge_to(self, intervals, start, end, height):
        if start is None or height == 0 or start == end:
            return

        if not intervals:
            intervals.append([start, end, height])
            return

        _, prev_end, prev_height = intervals[-1]
        if prev_height == height and prev_end == start:
            intervals[-1][1] = end
            return

        intervals.append([start, end, height])

class HashHeap:

    def __init__(self, desc=False):
        self.hash = dict()
        self.heap = []
        self.desc = desc

    @property
    def size(self):
        return len(self.heap)

    def push(self, item):
        self.heap.append(item)
        self.hash[item] = self.size - 1
        self._sift_up(self.size - 1)

    def pop(self):
        item = self.heap[0]
        self.remove(item)
        return item

    def top(self):
        return self.heap[0]

    def remove(self, item):
        if item not in self.hash:
            return

        index = self.hash[item]
        self._swap(index, self.size - 1)

        del self.hash[item]
        self.heap.pop()

        # in case of the removed item is the last item
        if index < self.size:
            self._sift_up(index)
            self._sift_down(index)

    def _smaller(self, left, right):
        return right < left if self.desc else left < right

    def _sift_up(self, index):
        while index != 0:
            parent = (index - 1) // 2
            if self._smaller(self.heap[parent], self.heap[index]):
                break
            self._swap(parent, index)
            index = parent

    def _sift_down(self, index):
        if index is None:
            return
        while index * 2 + 1 < self.size:
            smallest = index
            left = index * 2 + 1
            right = index * 2 + 2

            if self._smaller(self.heap[left], self.heap[smallest]):
                smallest = left

            if right < self.size and self._smaller(self.heap[right], self.heap[smallest]):
                smallest = right

            if smallest == index:
                break

            self._swap(index, smallest)
            index = smallest

    def _swap(self, i, j):
        elem1 = self.heap[i]
        elem2 = self.heap[j]
        self.heap[i] = elem2
        self.heap[j] = elem1
        self.hash[elem1] = j
        self.hash[elem2] = i

# Test Cases
if __name__ == "__main__":
    s = Solution()
