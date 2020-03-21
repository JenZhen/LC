#!/usr/bin/python

# Given n pieces of wood with length L[i] (integer array).
# Cut them into small pieces to guarantee you could have equal or
# more than k pieces with the same length. What is the longest length you can get
# from the n pieces of wood? Given L & k, return the maximum length of the small pieces.
# You couldn't cut wood into float length. If you couldn't get >= k pieces, return 0.

# Example:
# L=[232, 124, 456], k=7, return 114
"""
Algo: Binary Search
D.S.:

Solution:
- Given L (regardless value of k), can know min and max of the after-cut length
	min: 1
	max: max(L)
- Think this way, if equal lenght is N, how many pieces we could have
	sum = L[0] / N  + L[1] / N +... = sum(L / N)
	if sum >= k: N is too small, increase N could have less cut
	if sum < k: N is too large

Similar to "Copy Books"
Corner cases:
- total length of L less than k (even cut all to 1 still not enough)
"""

class Solution1:
	"""
	@param: L: Given n pieces of wood with length L[i]
	@param: k: An integer
	@return: The maximum length of the small pieces
	"""
	def woodCut(self, L, k):
		# write your code here
		if L is None or k is None or len(L) == 0 or sum(L) < k:
			return 0

		lo, hi = 1, max(L);
		while lo + 1 < hi:
			mid = (lo + hi) / 2
			# 核心：相当于抄书的 numberOfCopier 函数
			numPieces = sum([l / mid for l in L])
			if numPieces >= k:
				lo = mid
			else:
				hi = mid
		if sum([l / hi for l in L]) >= k:
			return hi
		else:
			return lo

# Test Cases
if __name__ == "__main__":
	solution = Solution()
