#! /usr/local/bin/python3

# https://www.lintcode.com/problem/maximum-gap/
# Example
# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#
# Return 0 if the array contains less than 2 elements.
#
# Example
# Given [1, 9, 2, 5], the sorted form of it is [1, 2, 5, 9], the maximum gap is between 5 and 9 = 4.
#
# Challenge
# Sort is easy but will cost O(nlogn) time. Try to solve it in linear time and space.
#
# Notice
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.



"""
Algo:
D.S.: Greedy

Solution:
Sort o(nlogn)不是理想算法。
如果o(n) 应该是greedy. 见法二

这个题如果用min max of value 开辟而外存储空间不能通过oj 空间太大了
Corner cases:
"""

class Solution1:
    """
    @param nums: an array of integers
    @return: the maximun difference
    """
    def maximumGap(self, nums):
        # write your code here
        if not nums or len(nums) == 1:
            return 0
        nums = sorted(nums)
        import sys
        res = -sys.maxsize
        for i in range(1, len(nums)):
            res = max(res, nums[i] - nums[i - 1])
        return res


class Solution2:
     # @param nums: a list of integers
     # @return: the maximum difference
    def maximumGap(self, nums):
        # write your code here
        if (len(nums)<2): return 0
        minNum = -1
        maxNum = -1
        n = len(nums)
        for i in xrange(n):
            minNum = self.min(nums[i], minNum)
            maxNum = self.max(nums[i], maxNum)
        if maxNum==minNum: return 0
        average = (maxNum-minNum) * 1.0 / (n-1)
        if average==0: average += 1
        localMin = []
        localMax = []
        for i in xrange(n):
            localMin.append(-1)
            localMax.append(-1)
        for i in xrange(n):
            t = int((nums[i]-minNum) / average)
            localMin[t] = self.min(localMin[t], nums[i])
            localMax[t] = self.max(localMax[t], nums[i])
        ans = average
        left = 0
        right = 1
        while left<n-1:
            while right<n and localMin[right]==-1: right += 1
            if right>=n: break
            ans = self.max(ans, localMin[right]-localMax[left])
            left = right
            right += 1
        return ans
    def min(self, a, b):
        if (a==-1): return b
        elif (b==-1): return a
        elif (a<b): return a
        else: return b
    def max(self, a, b):
        if (a==-1): return b
        elif (b==-1): return a
        elif (a>b): return a
        else: return b
# Test Cases
if __name__ == "__main__":
    solution = Solution()
