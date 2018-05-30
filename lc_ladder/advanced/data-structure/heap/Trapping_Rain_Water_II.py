#! /usr/local/bin/python3

# https://www.lintcode.com/en/old/problem/trapping-rain-water-ii/
# Given n x m non-negative integers representing an elevation map 2d where the area of each cell is 1 x 1, compute how much water it is able to trap after raining.
# Example
# Given
# [12,13,0,12]
# [13,4,13,12]
# [13,8,10,12]
# [12,13,12,12]
# [13,13,13,13]
# return 14.

"""
Algo:
D.S.: Heap

Solution:
Follow up for Trap Rain Water.
Time: O(mn * log(mn)) where log(mn) is heap operation for a heap of size mn
Corner cases:
"""

import heapq
class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    def trapRainWater(self, heights):
        # write your code here
        if not heights or not heights[0]:
            return 0
        row = len(heights)
        col = len(heights[0])
        visited = [[False for j in range(col)] for i in range(row)]
        minHeap = []
        # Prepare outer range of elements into minHeap
        # And mark visited as True
        # 1. Get the leftmost and rightmost column to minHeap
        for i in range(row):
            heapq.heappush(minHeap, (heights[i][0], i, 0))
            heapq.heappush(minHeap, (heights[i][col - 1], i, col - 1))
            visited[i][0] = True
            visited[i][col - 1] = True
        # 2. Get the top row and bottom row (excluding corner elements) into minHeap
        for j in range(1, col - 1):
            heapq.heappush(minHeap, (heights[0][j], 0, j))
            heapq.heappush(minHeap, (heights[row - 1][j], row - 1, j))
            visited[0][j] = True
            visited[row - 1][j] = True

        chg = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        while minHeap: # minHeap not empty
            minH, x, y = heapq.heappop(minHeap)
            for chgX, chgY in chg:
                newX = x + chgX
                newY = y + chgY
                # if new x, y in board range and not visited, proceed
                if newX >= 0 and newX < row and newY >= 0 and newY < col and visited[newX][newY]== False:
                    visited[newX][newY] = True
                    if minH > heights[newX][newY]:
                        res += (minH - heights[newX][newY])
                        heapq.heappush(minHeap, (minH, newX, newY))
                    else:
                        heapq.heappush(minHeap, (heights[newX][newY], newX, newY))
        return res

# Test Cases
if __name__ == "__main__":
    s = Solution()
