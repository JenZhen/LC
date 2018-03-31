#!/usr/bin/python

# https://leetcode.com/problems/ugly-number-ii/description/
# Example
# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

"""
Algo: heap
D.S.:
1. 2(0), 3(0), 5(0)
2. 2(1), 3(0), 5(0)
3. 2(0), 3(1), 5(0)
4. 2(2), 3(0), 5(0)
5. 2(0), 3(0), 5(1)
6. 2(1), 3(1), 5(0)
8. 2(3), 3(0), 5(0)

Solution:

Corner cases:
"""

import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is None or n == 0:
            return None

        fac = [2, 3, 5]
        heap = [(fac[i], i) for i in range(len(fac))]
        heapq.heapify(heap)

        val = 1
        while n - 1 > 0:
            val, level = heapq.heappop(heap)
            while level < 3:
                newVal = val * fac[level]
                heapq.heappush(heap, (newVal, level))
                level += 1
            n -= 1
        return val


# Test Cases
if __name__ == "__main__":
	solution = Solution()
