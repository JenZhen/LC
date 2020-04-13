#!/usr/bin/python

# https://leetcode.com/problems/super-ugly-number/description/
# Example

"""
Algo: heap
D.S.:

Solution:
Same as ugly number II, prime list was given
Corner cases:
"""

import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n == 0 or primes is None or len(primes) == 0:
            return None

        # setup the init heap
        heap = [(primes[i], i) for i in range(len(primes))]
        heapq.heapify(heap)

        val = 1
        while n - 1 > 0:
            val, level = heapq.heappop(heap)
            while level < len(primes):
                newVal = val * primes[level]
                heapq.heappush(heap, (newVal, level))
                level += 1
            n -= 1
        return val

# Test Cases
if __name__ == "__main__":
	solution = Solution()
