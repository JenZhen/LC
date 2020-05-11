#! /usr/local/bin/python3

# https://leetcode.com/problems/intersection-of-three-sorted-arrays/
# Example
# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order,
# return a sorted array of only the integers that appeared in all three arrays.
# Example 1:
# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.
#
# Constraints:
# 1 <= arr1.length, arr2.length, arr3.length <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""
Algo:
D.S.:

Solution:
simplified merge k sorted array
use 3 pointers not a heap

Time: O(min(arr1, arr2, arr3))
Space: O(1)
Corner cases:
"""

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        if not arr1 or not arr2 or not arr3:
            return []
        i, j, k = 0, 0, 0
        res = []
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                maxval = max(arr1[i], arr2[j], arr3[k])
                if maxval != arr1[i]:
                    i += 1
                if maxval != arr2[j]:
                    j += 1
                if maxval != arr3[k]:
                    k += 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
