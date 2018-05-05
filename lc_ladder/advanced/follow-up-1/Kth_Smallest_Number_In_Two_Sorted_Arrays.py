#! /usr/local/bin/python3

# https://www.lintcode.com/en/old/problem/kth-smallest-sum-in-two-sorted-arrays/
# Given two integer arrays sorted in ascending order and an integer k. Define sum = a + b, where a is an element from the first array and b is an element from the second one. Find the kth smallest sum out of all possible sums.
# Example
# Given [1, 7, 11] and [2, 4, 6].
# For k = 3, return 7.
# For k = 4, return 9.
# For k = 8, return 15.

"""
Algo: template to find kth smallest
D.S.: minHeap

Solution:
Time: O(klogk) k operations (loops), and each heap operation takes logk
Space: O(m*n) m = len(A), n = len(B)

Solution:

Corner cases:
"""

class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        # write your code here
        import heapq

        # invalid input
        if not A or not B or not k:
            return 0

        # out of boundry check
        m = len(A)
        n = len(B)
        if k > m * n:
            return A[m - 1] + B[n - 1]

        # A is x, B is y
        """
        Converted to https://www.lintcode.com/en/old/problem/kth-smallest-number-in-sorted-matrix/
             2  4  6
        1 |  3  5  7
        7 |  9 11  13
        11| 13 15  17

        m * n (m is len(A) n is len(B))
        """
        minHeap = []
        heapq.heapify(minHeap)
        visited = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(False)
            visited.append(row)
        heapq.heappush(minHeap, (A[0] + B[0], (0, 0)))
        for i in range(k - 1):
            cur = heapq.heappop(minHeap)
            x, y = cur[1][0], cur[1][1]
            if x + 1 < m and visited[x + 1][y] == False:
                heapq.heappush(minHeap, (A[x + 1] + B[y], (x + 1, y)))
                visited[x + 1][y] = True
            if y + 1 < n and visited[x][y + 1] == False:
                heapq.heappush(minHeap, (A[x] + B[y + 1], (x, y + 1)))
                visited[x][y + 1] = True
        cur = heapq.heappop(minHeap)
        return cur[0]
        
# Test Cases
if __name__ == "__main__":
    solution = Solution()
