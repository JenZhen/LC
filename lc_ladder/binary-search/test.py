#!/urs/bin/python

class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""      
		ret = [-1, -1]
		if nums is None or len(nums) == 0:
			return ret
		print ret[0], ret[1]
		ret[0] = self.firstPos(nums, target)
		ret[1] = self.lastPos(nums, target)
		return ret
	
	def firstPos(self, nums, target):
		lo, hi = 0, len(nums) - 1
		mid = (lo + hi) / 2
		while lo + 1 < hi:
			mid = (lo + hi) / 2
			print "where is mid: ", mid
			if target > nums[mid]:
				lo = mid
			else:
				hi = mid
		if nums[lo] == target:
			return lo
		elif nums[hi] == target:
			return hi
		else:
			return -1
	def lastPos(self, nums, target):
		lo, hi = 0, len(nums) - 1
		while lo + 1 < hi:
			mid = (lo + hi) / 2
			if target >= nums[mid]:
				lo = mid
			else:
				hi = mid 
		if nums[hi] == target:
			return hi
		elif nums[lo] == target:
			return lo
		else:
			return -1

if __name__ == "__main__":
	solution = Solution()
	nums = [5,7,7,8,8,10]
	target = 8
	print solution.searchRange(nums, target)
