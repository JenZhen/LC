# Given a collection of distinct numbers, return all possible permutations.
# [1,2] -> [[1,2], [2,1]]

"""
Algo: DFS, Recursion
D.S.: 

Solution:

Corner cases:
Invalidity check:
	1. nums is None: []
	2. nums contains no element: [[]]
"""

class Solution(object):
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		def _swap(nums, i, j):
			nums[i], nums[j] = nums[j], nums[i]
		def _helper(res, nums, start_idx):
			if start_idx == len(nums) - 1:
				newNums = [ele for ele in nums]
				# print ("Add %s" %newNums)
				res.append(newNums) # why not use deep copy
				# return #no need to have return
			else:
				for i in range(start_idx, len(nums)):
					_swap(nums, i, start_idx)
					# print ("Entering next: ")
					# print ("Nums: %s, startIdx: %s, i: %s" %(nums, start_idx, i))
					_helper(res, nums, start_idx + 1)
					_swap(nums, i, start_idx)
				# return #no need to have return
		
		if nums is None:
			return []
		if len(nums) == 0:
			return [[]]
		res = []
		_helper(res, nums, 0)
		return res

# Test Cases
if __name__ == "__main__":
	solution = Solution()
	# 1. [1,2,3]
	nums = [1,2,3]
	print solution.permute(nums)
	# tbd
	# 2. 
	# 3.