#!/usr/bin/python

# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# Example
# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.

"""
Algo: Heap, Binary Search
D.S.:

Solution:

Solution1:
Min heap: not ideal
Time: O(nlogn) - heap operation, where n is the size of matrix
Space: O(n) - min heap size

Can reduce heap to size of k, while k is also the scale of n

Solution2:
从左上角最小的数开始找第k小, 每次都能找到当前最小数。寻找过程有点儿想bfs
Time: O(k) * O(n)
Space: O(n) size of heap each iteration come in 2 pop 1. it's the scale of the size of matrix

Solution3:
https://www.jiuzhang.com/solution/kth-smallest-number-in-sorted-matrix/#tag-highlight-lang-python
二分法:
二分答案,初始区间即矩阵最小值和最大值构成的区间.
二分过程查找区间中点 mid 在矩阵中的排名, 假设为 t

若 t == k, 该点即是结果
若 t > k, 区间变成 [l, mid - 1]
若 t < k, 区间变成 [mid + 1, r]

TODO: 快速找到mid在矩阵中的排名

Corner cases:
"""

class Solution1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        from heapq import heappush, heappop

        if k is None or not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return None
        n = len(matrix)
        if n * n < k:
            return matrix[-1][-1]

        heap = []
        for i in range(n):
            for j in range(n):
                heappush(heap, matrix[i][j])

        for it in range(k - 1):
            heappop(heap)
        return heappop(heap)

class Solution2:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        from heapq import heappush, heappop

        if k is None or not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return None

        row, col = len(matrix), len(matrix[0])
        num = None # result
        heap = [(matrix[0][0], 0, 0)] # init heap with top-left value and it's x, y
        visited = set([0]) # use one-directional coordinate 路径会有重复，一定要记录访问过的位置
        for _ in range(k):
			# 每一次pop都能找到当前最小数
            num, x, y = heappop(heap)
			# 从x,y 向下一行找 下一个大的数
            if x < row - 1 and (x + 1) * col + y not in visited:
                heappush(heap, (matrix[x + 1][y], x + 1, y))
				# 放进heap 中的数一定要加到visited中
                visited.add((x + 1) * col + y)
			# 从x,y 向下一列找 下一个大的数
            if y < col - 1 and x * col + y + 1 not in visited:
                heappush(heap, (matrix[x][y + 1], x, y + 1))
                visited.add(x * col + y + 1)
        return num


# Test Cases
if __name__ == "__main__":
	solution = Solution()
