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

Solution1:
Time: O(m * n)
Space: O(1)
Simulation of the process.

Solution2:
读每一条， 根据方向reverse 需要额外空间
Time: O(m * n)
Space: O(max(m, n))

注意方向的设定
Corner cases:
"""
class Solution1:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        res = []
        i, j = 0, 0
        FLAG = 1
        dirs = {
            1: (-1, 1),
            0: (1, -1)
        }
        while 0 <= i < m and 0 <= j < n:
            res.append(matrix[i][j])
            ni, nj = dirs[FLAG][0] + i, dirs[FLAG][1] + j
            if 0 <= ni < m and 0 <= nj < n:
                i = ni
                j = nj
            else:
                # 重要 方向装换
                if FLAG:
                    i += (j == n - 1)
                    j += (j < n - 1)
                else:
                    j += (i == m - 1)
                    i += (i < m - 1)
                FLAG = 1 - FLAG
        return res


class Solution2:
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
