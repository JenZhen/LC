#!/usr/bin/python

# Suppose you have n versions [1, 2, ..., n]
# You want to find out the first bad one, which causes all the 
# following ones to be bad. 
# user bool isBadVersion(version) to tell if bad or not
# https://leetcode.com/problems/first-bad-version/description/
"""
Algo: Binary Search
D.S.: 

Solution:
Binary Search with comparison, using Solution3 template
Exactly same with "First Position of Target"

Corner cases:
"""
class Solution(object):
	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n is None or n == 0:
			return -1
		lo, hi = 1, n
		while lo + 1 < hi:
			mid = (lo + hi) / 2
			if isBadVersion(mid):
				hi = mid
			else:
				lo = mid
		if isBadVersion(lo):
			return lo
		elif isBadVersion(hi):
			return hi
		else:
			return -1

# Test Cases
if __name__ == "__main__":
	solution = Solution()
	# 1. 
	# 2. 
	# 3.