#! /usr/local/bin/python3

# https://www.lintcode.com/problem/continuous-subarray-sum-ii/
#
# Given an circular integer array (the next element of the last element is the first element), find a continuous subarray in it,
# where the sum of numbers is the biggest. Your code should return the index of the first number and the index of the last number.
#
# If duplicate answers exist, return any of them.
#
# Example
# Give [3, 1, -100, -3, 4], return [4,1].
#
# Challenge
# Do it in O(n) time

"""
Algo:
D.S.: Array

Solution:
有2种情况
1，结果在array中间，直接求即可
2. 结果在array两头，求最小连续和，找到区间，反过来就行。注意要单独考虑最小结果是全部array

Solution2:
将A求负，可以利用 findmax 函数

Corner cases:
考的重点
1. 最大在两头且有负数
[1, 2, -3, 2, -1] -> 2, -1, 1, 2
2. 有0 (这个题目答案要求含有0)
[0, 1, 2] -> return [0, 2] 而不是[1, 2]
3. all negative
[-2, -1, -3] -> [1, 1]
findMin -> [0, 2] 这是应该返回findMax的区间

"""


class Solution1:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        # write your code here
        res = []
        if not A:
            return res
        maxSum, maxRange = self.findMax(A)
        minSum, minRange = self.findMin(A)
        if maxSum >= sum(A) - minSum or sum(A) - minSum == 0:
            return maxRange
        else:
            st = (minRange[1] + 1) % len(A)
            end = 0 if minRange[0] - 1 == -1 else minRange[0] - 1
            return [st, end]

    def findMax(self, A):
        maxRes = A[0]
        ttl = A[0]
        st, end = 0, 0
        res = [st, end]
        for i in range(1, len(A)):
            if ttl >= 0:
                ttl += A[i]
                end = i
            else:
                ttl = A[i]
                st, end = i, i
            if ttl > maxRes:
                maxRes = ttl
                res = [st, end]
        return maxRes, res

    def findMin(self, A):
        minRes = A[0]
        ttl = A[0]
        st, end = 0, 0
        res = [st, end]
        for i in range(1, len(A)):
            if ttl < 0:
                ttl += A[i]
                end = i
            else:
                ttl = A[i]
                st, end = i, i
            if ttl < minRes:
                minRes = ttl
                res = [st, end]
        return minRes, res


class Solution2:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        # write your code here
        res = []
        if not A:
            return res
        maxSum, maxRange = self.findMax(A)
        minSum, minRange = self.findMax([-a for a in A])
        minSum = -minSum
        if maxSum >= sum(A) - minSum or sum(A) - minSum == 0:
            return maxRange
        else:
            st = (minRange[1] + 1) % len(A)
            end = 0 if minRange[0] - 1 == -1 else minRange[0] - 1
            return [st, end]

    def findMax(self, A):
        maxRes = A[0]
        ttl = A[0]
        st, end = 0, 0
        res = [st, end]
        for i in range(1, len(A)):
            if ttl >= 0:
                ttl += A[i]
                end = i
            else:
                ttl = A[i]
                st, end = i, i
            if ttl > maxRes:
                maxRes = ttl
                res = [st, end]
        return maxRes, res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
