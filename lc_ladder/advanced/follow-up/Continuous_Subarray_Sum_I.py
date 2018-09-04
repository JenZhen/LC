#! /usr/local/bin/python3

# https://www.lintcode.com/problem/continuous-subarray-sum/
# Given an integer array, find a continuous subarray where the sum of numbers is the biggest. Your code should return the index of the first number and the index of the last number. (If their are duplicate answer, return the firstone you find)

# Example
# Give [-3, 1, 3, -3, 4], return [1,4].
"""
Algo:
D.S.:

Solution:
Time: O(n)

Corner cases:
"""

class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        if not A:
            return []

        sum = A[0]
        ans = A[0]
        st, end = 0, 0
        res = [st, end]
        for i in range(1, len(A)):
            if sum < 0:
                sum = A[i]
                st = i
                end = i
            else:
                sum += A[i]
                end += 1
            if sum > ans:
                ans = sum
                res = [st, end]
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
