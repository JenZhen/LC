#! /usr/local/bin/python3

# https://leetcode.com/problems/range-sum-query-2d-immutable/submissions/
# Example

"""
Algo: Presum
D.S.:

Solution:
build presum matrix with first row and col as padding -- all 0s
记着考虑特殊非法输入 [[]] 返回None
Time: O(mn)
Space: O(mn)
Corner cases:
"""

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # 记着考虑 invalid input [[[]]] return None
        if not matrix or not len(matrix):
            self.sum_matrix = None
            return
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.sum_matrix = [[0 for _ in range(self.col + 1)] for _ in range(self.row + 1)]
        # fill self.sum_matrix
        for i in range(1, self.row + 1):
            for j in range(1, self.col + 1):
                self.sum_matrix[i][j] = matrix[i - 1][j - 1] + self.sum_matrix[i - 1][j] + self.sum_matrix[i][j - 1] - self.sum_matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.sum_matrix: return None
        return self.sum_matrix[row2 + 1][col2 + 1] - self.sum_matrix[row1][col2 + 1] - self.sum_matrix[row2 + 1][col1] + self.sum_matrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
