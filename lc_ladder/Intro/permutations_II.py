# Given a collection of distinct numbers, return all possible permutations.
# [1,1,2] -> [[1,1,2], [1,2,1], [2,1,1]]

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
					if i != start_idx and nums[start_idx] == nums[i]:
						continue
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
		nums.sort() # Note here should NOT _helper(res, nums.sort(), 0) 
		_helper(res, nums, 0) #ret = nums.sort() ret is None type
		return res

# Test Cases
if __name__ == "__main__":
	solution = Solution()
	# 1. [1,1,3]
	nums = [1,1,3]
	print solution.permute(nums)
	# tbd
	# 2. [2,2,1,1]
	nums = [2,2,1,1]
	res = solution.permute(nums)
	print ("res: %s \n size: %s" %(res, len(res)))
	# 3.