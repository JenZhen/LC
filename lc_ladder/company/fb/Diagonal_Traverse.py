#! /usr/local/bin/python3

# https://leetcode.com/problems/diagonal-traverse/
# Example
# Given a matrix of M x N elements (M rows, N columns),
# return all elements of the matrix in diagonal order as shown in the below image.
# Example:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
#
# Output:  [1,2,4,7,5,3,6,8,9]
"""
Algo:
D.S.:

Solution:
Time: O(m * n)
Space: O(m)

注意方向的设定
Corner cases:
"""

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        flag = True
        res = []
        for j in range(n):
            x, y = 0, j
            li = []
            while 0 <= x < m and 0 <= y < n:
                li.append(matrix[x][y])
                x += 1
                y -= 1
            if flag:
                res.extend(li[::-1])
            else:
                res.extend(li)
            flag = not flag

        for i in range(1, m):
            x, y = i, n - 1
            li = []
            while 0 <= x < m and 0 <= y < n:
                li.append(matrix[x][y])
                x += 1
                y -= 1
            if flag:
                res.extend(li[::-1])
            else:
                res.extend(li)
            flag = not flag
        return res
        
# Test Cases
if __name__ == "__main__":
    solution = Solution()
