#!/usr/local/bin/python3

# https://leetcode.com/problems/two-sum-less-than-k/
# Example
# Given an array A of integers and integer K, return the maximum S such that
#  there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.
#
# Example 1:
#
# Input: A = [34,23,1,24,75,33,54,8], K = 60
# Output: 58
# Explanation:
# We can use 34 and 24 to sum 58 which is less than 60.
# Example 2:
#
# Input: A = [10,20,30], K = 15
# Output: -1
# Explanation:
# In this case it's not possible to get a pair sum less that 15.
#
#
# Note:
#
# 1 <= A.length <= 100
# 1 <= A[i] <= 1000
# 1 <= K <= 2000

"""
Algo:
D.S.: Two pointers

Solution:
Time: O(n)
Space: O(1)

i, j 从两边加

Corner cases:
"""
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if not A or K is None:
            return -1

        A.sort()
        i, j = 0, len(A) - 1
        res = -1
        while i < j:
            sum = A[i] + A[j]
            if sum < K:
                i += 1
                res = max(res, sum)
            elif sum >= K:
                j -= 1
        return res
# Test Cases
if __name__ == "__main__":
	solution = Solution()
