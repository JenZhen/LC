# Given a collection of integers that might contain duplicates, nums, return all possible subsets
# Note: The solution set must not contain duplicate subsets.
# Example: nums = [1,2,2]
# Return [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]

"""
Algo: DFS (Similar to subsets_17)
D.S.: List/Array

Solution 1:
- The only difference from subsets_17 
Condition to tell duplicate or not:
Need not to find if dup: 
	the first iteration of a for loop -- meaning a new level (i == idx)
Need to find if dup:
	when pop off last ele and try next ele in nums
	-- meaning prev iteration used will try a new i, so num[i] != nums[i - 1]

Time Complexity: O(2 ^ n)
Space Complexity: O(2 ^ (n - 1))

Solution 2:
Similar to subsets_17

Corner cases:
- Invalidity check, return []
	1. nums is None
	2. nums contains no element (need to discuss it's [] or [[]])
"""

class Solution(object):
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self.ret = []
		if nums is None or len(nums) == 0:
			return self.ret
		nums.sort() # need to sort first to make sure subset are sorted as well
		self.helper(nums, [], 0) #no need for ret since it's self.ret and accessible by member function
		return self.ret
	
	def helper(self, nums, subset, idx):
		newSet = [ele for ele in subset] # important to deep copy subset 
		# print ("append set: %s at idx: %s" %(subset, idx))
		self.ret.append(newSet)
		for i in range(idx, len(nums)):
			if i != idx and nums[i] == nums[i - 1]:
				# print ("Skip i = %s" %i)
				continue
			subset.append(nums[i])
			# print ("in loop i = %s. create set: %s" %(i, subset))
			self.helper(nums, subset, i + 1)
			del subset[-1]
			# print "next loop"
		# print "trace back"
		return


# Test Cases
if __name__ == "__main__":
	solution = Solution()
	# 1. nums = [1,2,2]
	# -> [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]
	nums = [1,2,2]
	solution.subsets(nums)
	print solution.ret
	
	# tbd
	# 2. 
	# 3.