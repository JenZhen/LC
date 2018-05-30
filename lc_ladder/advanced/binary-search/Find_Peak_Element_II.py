#! /usr/local/bin/python3

# https://lintcode.com/problem/find-peak-element-ii/description
# There is an integer matrix which has the following features:

# The numbers in adjacent positions are different.
# The matrix has n rows and m columns.
# For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
# For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].

# We define a position P is a peek if:
# A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]
# Example
# [
#   [1 ,2 ,3 ,6 ,5],
#   [16,41,23,22,6],
#   [15,17,24,21,7],
#   [14,18,19,20,10],
#   [13,14,11,10,9]
# ]
# return index of 41 (which is [1,1]) or index of 24 (which is [2,2])
# Requirement O(m + n) where m is row count n is column count

"""
Algo: Bianry Search
D.S.: matris

Solution:
Solution1: iteration
for i in range(1, m - 1):
    for j in range(1, n - 1):
        if height[i][j] > (i j) up/down/left/right:
            return peak
Time: O(m * n)

Solution2: Search -- climb a mountian: to find the peak, follow the trail to go up hill
Worse case Time O(m * n) (zigzag shape)

Solution3: Semi binary search
Row and column are equivalent.
Binary search row: 1) find middle row; 2) find max in middle row; 3) compare max of middle row with its up/down neighbors
4) go to the bigger neighbor direction; will never across the middle row anymore; 5) iterate the process
Time: O(logm) + O(n) + O(log(m/2)) + O(n) + ...
      O(logm * n)

Solution4: binary search on rows and columns
binary row -> binary column -> binary row -> bianry column -> ... -> find the peak
Assume m = n:
T(n) = O(n) + O(n/2) + T(n/2) --> changed from n*n to (n/2) * (n/2)
T(n) = 3/2O(n) + T(n/2) ... expand
T(n) = 3O(n)
So far the best solution, this is a hire standard

Corner cases:
"""

# Test Cases
if __name__ == "__main__":
    solution = Solution()
