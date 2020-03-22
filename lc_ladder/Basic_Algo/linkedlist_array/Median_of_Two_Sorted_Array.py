#!/usr/bin/python
import linkedlist
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Example
# [1,3] [2] return 2

"""
Algo: Recursion
D.S.: Array

Solution:
Key part
1. total length m + n, find the (m+n)/2 th element ie problem of find kth element
2. when finding the kth element,
    array1 k/2 th (p1) compare with array2 k/2 th (p2)
        if either is not long enough, return max
        if p1 <= p2, remove all first k/2 th of that array, k reduced to k - k / 2
            to next recursion

Be careful of exit conditions
starting pointer p1 p2 are changing

Time Compelxity: O(log(m + n))
Corner cases:
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # think as find the kth smallest of nums1 and nums2
        import sys
        m = len(nums1)
        n = len(nums2)
        total = m + n

        def findKth(nums1, nums2, p1, p2, k):
            # p1 start pointer for nums1, same for p2
            if p1 >= m:
                return nums2[p2 + k - 1]
            if p2 >= n:
                return nums1[p1 + k - 1]
            if k == 1:
                return min(nums1[p1], nums2[p2])

            val1 = nums1[p1 + k / 2 - 1] if p1 + k / 2 - 1 < m \
                else sys.maxint
            val2 = nums2[p2 + k / 2 - 1] if p2 + k / 2 - 1 < n \
                else sys.maxint

            if val1 <= val2:
                return findKth(nums1, nums2, p1 + k / 2, p2, k - k / 2)
            else:
                return findKth(nums1, nums2, p1, p2 + k / 2, k - k / 2)

        if total % 2 == 1:
            return findKth(nums1, nums2, 0, 0, total / 2 + 1)
        else:
            midLeft = findKth(nums1, nums2, 0, 0, total / 2)
            midRight = findKth(nums1, nums2, 0, 0, total / 2 + 1)
            return (midLeft + midRight) / 2.0

# Test Cases
if __name__ == "__main__":
	solution = Solution()
