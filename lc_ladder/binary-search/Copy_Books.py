#!/usr/bin/python

# http://www.lintcode.com/en/problem/copy-books/
# Given array A = [3,2,4], k = 2.
# Return 5( First person spends 5 minutes to copy book 1 and book 2 and 
# second person spends 4 minutes to copy book 3. )

"""
Algo: Binary Search / DP
D.S.: Array

Solution:
Solution1: Binary Search
Original data is not sorted, but searching goal could be treated as searchable
Example [3, 2, 4] k = 2
- given pages array, (regardless value of k), it's easy to know the min/max
  min = max(pages) (multiple copier do at the same time)
  max = sum(pages) (only 1 copier time cumulates)
- time array [4, 5, 6, 7, 8, 9] (we only know 4 and 9)
	mid 6, call subfunction to get how many copier needed if copy time <= 6 (limit)
	Note: in subfunction, numCopier starts at 1 counting start 2nd element
- if when copy time <= mid, we have <= k copier, hi = mid, try smaller time limit
  else lo = mid
- Remember at the end lo and hi needs to examed, lo has priority

Time Complexity:
m = len(pages)
n = diff(sum(pages) - max(pages)) [1,2,90] or [1,90,91]
O(m*log(n))

Solution2: DP
Corner cases:
"""

# Similar to "Wood Cut"
# http://www.lintcode.com/en/problem/wood-cut/

# Solution1: Binary Search
class Solution1:
	"""
	@param: pages: an array of integers
	@param: k: An integer
	@return: an integer
	"""

	def copyBooks(self, pages, k):
		# write your code here
		if pages is None or k is None or len(pages) == 0:
			return 0
		
		def numCopier(pages, limit):
			sum = pages[0]
			copier = 1
			for i in range(1, len(pages)):
				if sum + pages[i] > limit:
					copier += 1
					sum = 0
				sum += pages[i]
			print "--------need: ", copier
			return copier
		
		lo = max(pages)
		hi = sum(pages)
		
		while lo + 1 < hi:
			mid = (lo + hi) / 2
			if numCopier(pages, mid) <= k:
				hi = mid
			else:
				lo = mid
		if numCopier(pages, lo) <= k:
			print "here"
			return lo
		else:
			return hi


# Test Cases
if __name__ == "__main__":
	solution1 = Solution1()

	inputs = [
		{
			'pages': [3,2,4],
			'k': 2
		},
		{
			'pages': [1,2],
			'k': 5
		}
	]

	for testcase in inputs:
		pages = testcase['pages']
		k = testcase['k']
		print solution1.copyBooks(pages, k)
