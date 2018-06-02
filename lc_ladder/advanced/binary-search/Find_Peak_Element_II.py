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

Acceptable interview solutions are solution3 and solution4
Corner cases:
"""

class Solution3:
    # Time O(nlogn) -- n times of binary search
    # Binary on row, linear find max through each column
    # Failed lintcode.com time limit.
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        # write your code here
        if not A or not A[0]:
            return None
        m = len(A)
        n = len(A[0])
        topRow = 1 # excluding first/last row
        bottomRow = m - 2
        ans  = []
        while topRow <= bottomRow:
            midRow = (topRow + bottomRow) // 2
            rowMaxCol = self.findRowMaxCol(A[midRow]) # O(n)
            if A[midRow][rowMaxCol] < A[midRow - 1][rowMaxCol]:
                bottomRow = midRow - 1
            elif A[midRow][rowMaxCol] < A[midRow + 1][rowMaxCol]:
                topRow = midRow + 1
            else:
                # find a peak point
                ans.append(midRow)
                ans.append(rowMaxCol)
                break
        return ans

    def findRowMaxCol(self, row):
        maxCol = 0
        for i in range(len(row)):
            maxCol = i if row[i] > row[maxCol] else maxCol
        return maxCol


"""
--------
|   |   |
|   |   |
------j--
|   |   |
|   i   |
--------
1. make a m*n grid to 4 even pieces (size from m * n to m/2 * n/2)
2. Comparing with the middle cross point(as init comparison),
    iterate O(n) to find col max on axis of midRow,
    iterate O(m) to find row max on axis of midCol,
    --> find a pair of i, j that could make a posible candidate on 1/4 panels.
3. Search around (up/down/left/right) that candidate (in the climb mountain style).
    --> if fails one direction, move candidate to that direction
    --> if candidate is validated, return it's cooridation,
        else continue to next recursion level to break down the panel. (Based on current candidate to determine which panel to be broken down)
4. Break down (size from m/2 * n/2 to m/4 * n/4)

"""
class Solution4:
    # Time O(m + n) -- binary search on row and column
    """
    @param: A: An integer matrix
    @return: The index of the peak
    """
    def findPeakII(self, A):
        # write your code here
        if not A or not A[0]:
            return None
        m, n = len(A), len(A[0])
        startRow, endRow = 1, m - 2
        startCol, endCol = 1, n - 2
        return self.helper(startRow, endRow, startCol, endCol, A)

    def helper(self, startRow, endRow, startCol, endCol, A):
        midRow = (startRow + endRow) // 2
        midCol = (startCol + endCol) // 2
        print("find mid [%s, %s]" %(midRow, midCol))
        # init x and y at midRow, midCol
        x, y = midRow, midCol
        max = A[midRow][midCol]
        # Go through columns first
        for j in range(startCol, endCol + 1):
            if A[midRow][j] > max:
                max = A[midRow][j]
                x = midRow # no change
                y = j
        # Go through row
        for i in range(startRow, endRow + 1):
            if A[i][midCol] > max:
                max = A[i][midCol]
                x = i
                y = midCol # no change

        # Search around x,y
        print("candidate: %s" %A[x][y])
        isPeak = True
        # up
        if A[x - 1][y] > A[x][y]:
            isPeak = False
            x -= 1
        # down
        elif A[x + 1][y] > A[x][y]:
            isPeak = False
            x += 1
        # left
        elif A[x][y - 1] > A[x][y]:
            isPeak = False
            y -= 1
        # right
        elif A[x][y + 1] > A[x][y]:
            isPeak = False
            y += 1
        # if find peak
        if isPeak:
            return [x, y]

        # if not find peak, continue to narrow down
        # top-left
        if startRow <= x < midRow and startCol <= y < midCol:
            return self.helper(startRow, midRow - 1, startCol, midCol - 1, A)
        # top-right
        if startRow <= x < midRow and midCol < y <= endCol:
            return self.helper(startRow, midRow - 1, midCol + 1, endCol, A)
        # bottom-left
        if midRow < x <= endRow and startCol <= y < midCol:
            return self.helper(midRow + 1, endRow, startCol, midCol - 1, A)
        # bottome-right
        if midRow < x <= endRow and midCol < y <= endCol:
            return self.helper(midRow + 1, endRow, midCol + 1, endCol, A)
        return [-1, -1]

# Test Cases
if __name__ == "__main__":
    testCases = [
        [
         [1, 2, 3, 4, 5],
         [16,41,23,22,6],
         [15,17,24,21,7],
         [14,18,19,20,8],
         [13,12,11,10,9]
        ],
        [
         [1, 2, 4, 3],
         [5, 6, 8, 7],
         [9, 10,12,11],
         [13,14,16,15],
         [21,22,24,23],
         [17,18,20,19]
        ]
    ]
    s3 = Solution3()
    s4 = Solution4()
    for A in testCases:
        res3 = s3.findPeakII(A)
        print("res3: %s" %repr(res3))
        res4 = s4.findPeakII(A)
        print("res4: %s" %repr(res4))
