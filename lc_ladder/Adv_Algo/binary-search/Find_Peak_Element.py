#! /usr/local/bin/python3

# https://lintcode.com/problem/find-peak-element/description
# There is an integer array which has the following features:
# The numbers in adjacent positions are different.
# A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
# A[P] > A[P-1] && A[P] > A[P+1]
# Example
# Given [1, 2, 1, 3, 4, 5, 7, 6]
# Return index 1 (which is number 2) or 6 (which is number 7)
# Time complexity O(logN)
# Same as lc_ladder/binary-search/Max_Number_in_Mountian_Sequence.py

"""
Algo: Binary Search
D.S.:

Solution:
- Important prerequisite that A[0] < A[1] && A[A.length - 2] > A[A.length - 1], meaning a peak is for sure to be exisiting.
Using binary search, if find a number greater than the middle one, go to that direction will for sure to find a peak.
Time: O(logn)
Corner cases:
"""

class Solution:
    """
    @param: A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if not A:
            return None

        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2 # note python3 takes the floor
            if A[mid - 1] > A[mid]:
                end = mid
            elif A[mid + 1] > A[mid]:
                start = mid
            else:
                return mid
        return start if A[start] > A[end] else end

# Test Cases
if __name__ == "__main__":
    solution = Solution()
