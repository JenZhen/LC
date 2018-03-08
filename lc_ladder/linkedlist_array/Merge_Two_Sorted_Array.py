#!/usr/bin/python

# https://leetcode.com/problems/merge-sorted-array/description/
# Given two arrays, nums1, nums2. Merge nums2 into nums1, do it in-place

"""
Algo:
D.S.: Array

Solution:
Do from back to front
Time Complexity: O(m+n)

FollowUp1:
If merge to a new array
Pitfall: init new array [], when assigning new element use append not using index
arr[0] is out of range error.

FollowUp2:
Merge K Sorted arrays (Also in category Data Structure)
http://www.jiuzhang.com/solution/merge-k-sorted-arrays/
Given k sorted integer arrays, merge them into one sorted array.



Corner cases:
"""

class Solution(object):
	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: void Do not return anything, modify nums1 in-place instead.
		"""
		# It's hard to insert and adjust from start
		# Allocate from back to start
		#
		# m and n are unnecessary m = len(nums1) n = len(nums2)
		cur = m + n - 1
		p1 = m - 1
		p2 = n - 1
		# Important: condition is ">= 0" not "p1 and p2"
		while p1 >= 0 and p2 >= 0:
			if nums1[p1] >= nums2[p2]:
				nums1[cur] = nums1[p1]
				p1 -= 1
				cur -= 1
			else:
				nums1[cur] = nums2[p2]
				p2 -= 1
				cur -= 1

		if p1 < 0:
			nums1[0:cur + 1] = nums2[0:p2 + 1]
		"""
		If merging nums2 into nums1, no need to handle remaining nums1, already there
		if p2 < 0:
			nums1[0:cur + 1] = nums1[0:p1 + 1]
		"""


class Solution_FollowUp1:
	"""
	@param: A: sorted integer array A
	@param: B: sorted integer array B
	@return: A new sorted integer array
	"""
	def mergeSortedArray(self, A, B):
		# write your code here
		arr = []
		m = len(A)
		n = len(B)
		p1, p2 = 0, 0
		while p1 < m and p2 < n:
			if A[p1] <= B[p2]:
				arr.append(A[p1])
				p1 += 1
			else:
				arr.append(B[p2])
				p2 += 1

		if p1 < m:
			while p1 < m:
				arr.append(A[p1])
				p1 += 1
		if p2 < n:
			while p2 < m:
				print 'p2: ', p2
				arr.append(B[p2])
				p2 += 1
		return arr

# Test Cases
if __name__ == "__main__":
	solution2 = Solution2()
	A = [7]
	B = [5, 7]
	print solution2.mergeSortedArray(A, B)



