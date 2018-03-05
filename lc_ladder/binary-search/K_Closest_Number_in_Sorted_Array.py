# #!/usr/bin/python

# Given a target number, a non-negative integer k and an integer array A sorted in ascending order, find the k closest numbers to target in A, sorted in ascending order by the difference between the number and target. Otherwise, sorted in ascending order by number if the difference is same.
# Example
# Given A = [1, 2, 3], target = 2 and k = 3, return [2, 1, 3].
# Given A = [1, 4, 6, 8], target = 3 and k = 3, return [4, 1, 6].

"""
Algo: Binary Search
D.S.: Array

Solution:
1. Binary search to find the target
	- if exists, find the leftmost of target
	- if not, find the estimate (lo, hi right next to each other)
	Search will end with lo, hi next to each other
2. comparing and moving lo hi to two sides until all K is found

Follow up: Leetcode "Find K Closest Element"
https://leetcode.com/problems/find-k-closest-elements/description/
where result is required to be sorted in ascending order
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Using stack and queue(deque) to handle everything < target and >= target
Note: if findFirstOccurence then target goes to queue else goes to stack
Then pop all from stack to result, popleft all from deque to result
Need to be familar with "collections, deque" module

Time Complexity: O(LogN) + O(k) (Worst case k >= n)
Space Complexity: 
basic O(1)
Followup O(k) (space of queue and stack added up to k)

Corner cases:
- Invalid inputs
- k == 0 or len(A) == 0
- k > len(A) --> for now populate all in A
"""

class Solution:
	# @param {int[]} A an integer array
	# @param {int} target an integer
	# @param {int} k a non-negative integer
	# @return {int[]} an integer array
	def kClosestNumbers(self, A, target, k):
		res = []
		if A is None or target is None or k is None or \
			len(A) == 0 or k == 0:
			return res
		lo, hi = self.findTargetPosition(A, target)
		for i in range(k):
			if lo < 0 and hi == len(A):
				break
			elif lo < 0:
				res.append(A[hi])
				hi += 1
			elif hi == len(A):
				res.append(A[lo])
				lo -= 1
			else:
				# both lo and hi in range
				if abs(A[lo] - target) <= abs(A[hi] - target):
					res.append(A[lo])
					lo -= 1
				else:
					res.append(A[hi])
					hi += 1
		return res

	def kClosestNumbersFollowUp(self, A, target, k):
		from collections import deque
		res = []
		stack = []
		queue = deque([])
		if A is None or target is None or k is None or \
			len(A) == 0 or k == 0:
			return res
		lo, hi = self.findTargetPosition(A, target)
		for i in range(k):
			if lo < 0 and hi == len(A):
				break
			elif lo < 0:
				queue.append(A[hi])
				hi += 1
			elif hi == len(A):
				stack.append(A[lo])
				lo -= 1
			else:
				# both lo and hi in range
				if abs(A[lo] - target) <= abs(A[hi] - target):
					stack.append(A[lo])
					lo -= 1
				else:
					queue.append(A[hi])
					hi += 1
		while len(stack) > 0:
			res.append(stack.pop())
		while len(queue) > 0:
			res.append(queue.popleft())
		return res

	def findTargetPosition(self, A, target):
		# find the first occurence if exisiting
		lo, hi = 0, len(A) - 1
		while lo + 1 < hi:
			mid = (lo + hi) / 2
			if target <= A[mid]:
				hi = mid
			else:
				lo = mid
		print "lo = ", lo, " hi = ", hi
		return lo, hi

# Test Cases
if __name__ == "__main__":
	solution = Solution()

	inputs = [
		{'A'     : [1, 2, 3], 
		 'target': 2, 
		 'k'     : 3,
		},        #[2, 1, 3]
		{'A'     : [1, 4, 6, 8],
		 'target': 3, 
		 'k'     : 3,
		},		  #[4, 1, 6]
		{'A'     : [1, 2],
		 'target': 3, 
		 'k'     : 2,
		},		  #[2, 1]
		{'A'     : [2, 3],
		 'target': 1, 
		 'k'     : 2,
		},		  #[2, 3]
		{'A'     : [1, 1, 1, 1, 1],
		 'target': 1, 
		 'k'     : 3,
		},		  #[1, 1, 1]
		{'A'     : [1, 1, 1],
		 'target': 1, 
		 'k'     : 5,
		},		  #[1, 1, 1]
		{'A'     : [1, 3, 5, 7, 9],
		 'target': 5, 
		 'k'     : 2,
		},		  #[5, 3]
		{'A'     : [1, 1, 2, 6, 9],
		 'target': 3, 
		 'k'     : 2,
		},		  #[2, 1]
	]

	print "Test K Cloeset Number -----------"
	for testcase in inputs:
		A = testcase['A']
		target = testcase['target']
		k = testcase['k']
		print solution.kClosestNumbers(A, target, k)

	print "Test Follow-up -----------"
	for testcase in inputs:
		A = testcase['A']
		target = testcase['target']
		k = testcase['k']
		print solution.kClosestNumbersFollowUp(A, target, k)
