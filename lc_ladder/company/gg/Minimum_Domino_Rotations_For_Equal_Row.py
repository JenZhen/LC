#! /usr/local/bin/python3

# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/submissions/
# Example
# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.
# (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
#
# We may rotate the i-th domino, so that A[i] and B[i] swap values.
# Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.
# If it cannot be done, return -1.
#
# Example 1:
# Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# Output: 2
# Explanation:
# The first figure represents the dominoes as given by A and B: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
# Example 2:
# Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
# Output: -1
# Explanation:
# In this case, it is not possible to rotate the dominoes to make one row of values equal.
#
# Note:
# 1 <= A[i], B[i] <= 6
# 2 <= A.length == B.length <= 20000
"""
Algo:
D.S.:

Solution:
Time: O(n)
Space: O(1)

Corner cases:
"""
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        rotation2A = self.rotate(A[0], A, B)
        rotation2B = self.rotate(B[0], A, B)

        if rotation2A == -1:
            return rotation2B
        elif rotation2B == -1:
            return rotation2A
        else:
            return min(rotation2A, rotation2B)

    def rotate(self, x, A, B):
        # 把A或B 翻成x值 最少几次
        cnta = 0
        cntb = 0
        for i in range(len(A)):
            if A[i] != x and B[i] != x:
                return -1
            if A[i] != x:
                cnta += 1
            if B[i] != x:
                cntb += 1
        return min(cnta, cntb)
# Test Cases
if __name__ == "__main__":
    solution = Solution()
