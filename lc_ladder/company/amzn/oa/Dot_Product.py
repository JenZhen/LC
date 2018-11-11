#! /usr/local/bin/python3

# Requirement
# 给出两个数组，求它们的点积。(Wikipedia)
#
# 样例
# Input:A = [1,1,1]
# B = [2,2,2]
# Output:6
# 注意事项
# 如果没有点积则返回-1

"""
Algo:
D.S.:

Solution:

class Solution:
    """
    @param A: an array
    @param B: an array
    @return: dot product of two array
    """
    def dotProduct(self, A, B):
        # Write your code here
        if not A or not B or len(A) != len(B):
            return -1
        res = 0
        for i in range(len(A)):
            res += A[i] * B[i]
        return res

Corner cases:
"""

# Test Cases
if __name__ == "__main__":
    solution = Solution()
