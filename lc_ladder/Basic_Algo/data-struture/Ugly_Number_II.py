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
ugly number comes from ugly numbers
x,   x,   x,   x,   x,   x    --- * 1
x*2, x*2, x*2, x*2, x*2, x*2, --- * 2
x*3, x*3, x*3, x*3, x*3, x*3, --- * 3
x*5, x*5, x*5, x*5, x*5, x*5, --- * 5

essentially it's 4 sorted array merge find the top k

Solution2:
DP
Time: O(n)
Space: O(n)
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

class Solution2:
    def nthUglyNumber(self, n: int) -> int:
        if not n:
            return 0

        arr = [0 for _ in range(n)]
        arr[0] = 1 # the 1st number is 1
        idx2, idx3, idx5 = 0, 0, 0 # 2, 3, 5 init at arr[0] position

        # the n-th ugly number at idx n - 1
        for i in range(1, n):
            val2 = 2 * arr[idx2]
            val3 = 3 * arr[idx3]
            val5 = 5 * arr[idx5]

            val = min([val2, val3, val5])
            print(val)
            arr[i] = val
            if val == val2:
                idx2 += 1
            if val == val3:
                idx3 += 1
            if val == val5:
                idx5 += 1
        return arr[n - 1]
# Test Cases
if __name__ == "__main__":
	solution = Solution()
