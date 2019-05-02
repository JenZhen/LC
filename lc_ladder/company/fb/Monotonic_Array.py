#! /usr/local/bin/python3

# https://leetcode.com/problems/monotonic-array/
# Example
# An array is monotonic if it is either monotone increasing or monotone decreasing.
#
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
#
# Return true if and only if the given array A is monotonic.
#
#
#
# Example 1:
#
# Input: [1,2,2,3]
# Output: true
# Example 2:
#
# Input: [6,5,4,4]
# Output: true
# Example 3:
#
# Input: [1,3,2]
# Output: false
# Example 4:
#
# Input: [1,2,4,5]
# Output: true
# Example 5:
#
# Input: [1,1,1]
# Output: true
#
#
# Note:
#
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000

"""
Algo:
D.S.: Array

Solution:
Time: O(n) -- 需要做到one-pass

Corner cases:
"""

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if not A or len(A) == 1:
            return True
        cur = 1
        trend = None
        for i in range(1, len(A)):
            if A[i] > A[i -1]:
                if trend == None:
                    trend = 1
                elif trend == -1:
                    return False
            if A[i] < A[i - 1]:
                if trend == None:
                    trend = -1
                elif trend == 1:
                    return False
        return True


# Test Cases
if __name__ == "__main__":
    solution = Solution()
