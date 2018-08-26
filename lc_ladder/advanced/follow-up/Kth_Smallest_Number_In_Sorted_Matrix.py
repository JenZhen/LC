#! /usr/local/bin/python3

# https://www.lintcode.com/en/old/problem/kth-smallest-number-in-sorted-matrix/
# Find the kth smallest number in at row and column sorted matrix.
# Example
# Given k = 4 and a matrix
# [
#   [1 ,5 ,7],
#   [3 ,7 ,8],
#   [4 ,8 ,9],
# ]
# Return 5

"""
Algo: template to find kth smallest
D.S.: minHeap

Solution:
Time: O(klogk) k operation (loops), and each heap operation takes logk
Space: O(m*n)

Corner cases:
"""

class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        # write your code here
        import heapq

        # invalid input
        if not matrix or not matrix[0] or not k:
            return 0

        # out of boundry check
        m = len(matrix)
        n = len(matrix[0])
        if k > m * n:
            return matrix[m - 1][n - 1]

        # normal flow
        # cannot init this way, it's copy of reference not entity
        # visited = [[False] * n] * m
        visited = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(False)
            visited.append(row)

        minHeap = []
        heapq.heapify(minHeap)

        # init
        heapq.heappush(minHeap, (matrix[0][0], (0, 0)))
        visited[0][0] = True
        # go thru k - 1 times of iteration,
        # stop at the kth time, pop is the kth min
        for i in range(k - 1):
            # self.printHeap(minHeap)
            cur = heapq.heappop(minHeap)
            # do something
            x, y = cur[1][0], cur[1][1]
            print("curn x: %s, y: %s" %(x, y))
            if y + 1 < n and visited[x][y + 1] == False:
                heapq.heappush(minHeap, (matrix[x][y + 1], (x, y + 1)))
                visited[x][y + 1] = True
            if x + 1 < m and visited[x + 1][y] == False:
                heapq.heappush(minHeap, (matrix[x + 1][y], (x + 1, y)))
                visited[x + 1][y] = True
            self.printHeap(minHeap)
        cur = heapq.heappop(minHeap)
        return cur[0]

    @staticmethod
    def printHeap(heap):
        print("Diag heap:")
        print("[")
        for item in heap:
            print("[Value: %s. [x: %s, y: %s]]" %(item[0], item[1][0], item[1][1]))
        print("]")

# Test Cases
if __name__ == "__main__":
    testCases = [
        {
            "matrix":
                [
                  [1 ,5 ,7],
                  [3 ,7 ,8],
                  [4 ,8 ,9],
                ],
            "k": 5
        },
    ]
    solution = Solution()
    for t in testCases:
        matrix = t["matrix"]
        k = t["k"]
        res = solution.kthSmallest(matrix, k)
        print("res: %s" %res)
