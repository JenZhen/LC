#!/usr/bin/python

# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. 
# And you need to output the maximum average value. 
# Example
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

# Note:    
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].

"""
Algo: 
D.S.: 

Solution:
Solution1:
Straight forward, brutal force, 2 nested loops
Time Complexity: O(n * k)
Space Compelexity: O(1)

Solution2:
orig: [1, 12, -5, -6, 50, 3], k = 3
sum:[0,1, 13,  8,  2, 52, 55], sum[i] = sum(orgi[-1:i]), prefix sum[-1] = 0
k-sum[- - - ,  8,  1, 39, 47]
Time Complexity: O(n)
Space Complexity: O(2n)
Enhancement:
Mantain sum and ksum of size k and keep track of max sum.

Solution3: Binary way? 
Confused; 
https://www.jiuzhang.com/solution/maximum-average-subarray/

Follow-ups:
1. Given an array of integers, find a contiguous subarray which has the largest sum.
https://yisuang1186.gitbooks.io/-shuatibiji/maximum_subarray.html

2. 给出一个整数数组，有正有负。找到这样一个子数组，他的长度大于等于 k，且平均值最大。
https://www.jiuzhang.com/solution/maximum-average-subarray/

2. Given an array of integers, find two non-overlapping subarrays which have the largest sum. 
The number in each subarray should be contiguous.+
Return the largest sum.
https://yisuang1186.gitbooks.io/-shuatibiji/maximum_subarray_ii.html

Corner cases:
k < n
'-inf', 'inf'
"""
class Solution1(object):
	def findMaxAverage(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: float
		"""
		if nums is None or k is None or \
			len(nums) == 0 or len(nums) < k:
			return None
		avg = float('-inf')
		arrLen = len(nums)
		largestSum = float('-inf')
		for idx in range(k - 1, arrLen):
			total = 0
			for i in range(k):
				total += nums[idx - i]
				print 'total: ', total
			if total > largestSum:
				largestSum = total
		return largestSum / float(k)


class Solution2(object):
	def findMaxAverage(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: float
		"""
		if nums is None or k is None or \
			len(nums) == 0 or len(nums) < k:
			return None
		preSum = [None] * len(nums)
		kSum = [None] * len(nums)
		preSum[0] = nums[0]
		for i in range(1, len(nums)):
			preSum[i] = preSum[i - 1] + nums[i]
		print "preSum: ", preSum
		kSum[k - 1] = preSum[k - 1]
		for i in range(k, len(nums)):
			kSum[i] = preSum[i] - preSum[i - k]
		print "kSum: ", kSum

		return max(kSum) / float(k) 


# Test Cases
if __name__ == "__main__":
	solution1 = Solution1()
	solution2 = Solution2()
	inputs = [
		{'nums': [1,12,-5,-6,50,3], #12.75
		 'k': 4,
		},
		{'nums': [1,12,-5,-6,50,3], #15.76
		 'k': 3
		},
		{'nums': [-1],
		 'k': 1,
		}
	]
	for testcase in inputs:
		nums = testcase['nums']
		k = testcase['k']
		print solution1.findMaxAverage(nums, k)

	for testcase in inputs:
		nums = testcase['nums']
		k = testcase['k']
		print solution2.findMaxAverage(nums, k)
