# Given a set of distinct integers, nums, return all possible subsets.
# Note: The solution set must not contain duplicate subsets.
# 		Elements in a subset must be in non-descending order. 
# Exmple: Given [1,3] return [[],[1],[3],[1,3]]

"""
Algo: DFS
D.S.: Back-Trace

Solution 1:
DFS
** Backtracking Condition: idx is at the last of nums (all has tried to append)

[] --> init
[1] -> [1,2] -> [1,2,3]
    <-       <-
[2] -> [2,3]
    <-
[3]

Time Complexity: O(2^n) (traverse each possible mapping)
Space Complexity: O(n) max list [1, 2, ... n] a list contains all element

Solution 2:
Expansion method: size from 1 -> 2 -> 4 -> 8
[]
[1]
[2] [1,2]
[3] [1,3] [2,3] [1,2,3]

Time Complexity: O(2^n) same as above
Space Complexity: O(2^(n-1)) all previous subsets need to be saved

Solution 3:
bit manipulation
http://www.jiuzhang.com/solution/subsets-ii/

Corner cases:
- Invalidity check, return []
	1. nums is None
	2. nums contains no element (need to discuss it's [] or [[]])
"""

# Solution 1
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
		self.ret.append(newSet)
		for i in range(idx, len(nums)): # range(start, end, step) step default as 1
			subset.append(nums[i]) 
			self.helper(nums, subset, i + 1)
			del subset[-1]
		return

'''
# Solution 2
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        if nums is None or len(nums) == 0:
            return ret
        nums.sort()
        ret = [[]]
        for i in nums:
            prevSize = len(ret)
            for j in range(prevSize):
                newSubset = [ele for ele in ret[j]]
                newSubset.append(i)
                ret.append(newSubset)
        return ret
'''

# Test Cases
if __name__ == "__main__":
	solution = Solution()

	# 1. nums = [1,2,3]
	# -> [[], [1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
	nums = [1,2,3]
	solution.subsets(nums)
	print solution.ret
