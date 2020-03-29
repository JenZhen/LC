#!/usr/bin/python

# https://leetcode.com/problems/longest-consecutive-sequence/description/
# Example
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.
"""
Algo:
D.S.:
重复的数不算
Solution:
Easy solution:
    1. Sort array, then iterate thru array
    Time Complexity: O(nlgn) for soring

Faster solution:
    1. build a map for all elements in nums
    2. given an element find left side and right side util not in previously built map
    3. to avoid revisit
        1) build another map to track visited, next loop don't do it again
        2) or when element is visited as consecutive when searching left/right, remove from map
        next time when checking it in nums, it won't have consecutive neighbours in map

Corner cases:
"""
class Solution_Slow:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        num.sort()
        maxLen = 1
        tmpLen = 1
        pre = num[0]
        for n in num:
            if n == pre:
                continue
            elif n - pre == 1:
                tmpLen += 1
            elif n - pre > 1:
                maxLen = max(maxLen, tmpLen)
                tmpLen = 1
            pre = n
        maxLen = max(maxLen, tmpLen)
        return maxLen

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        maxLen = 1
        dic = {}
        visited = {} # optional

        # prepare dic
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1

        for n in nums:
            # if n in visited:
            #     continue
            tmpLen = 1
            left = n - 1
            right = n + 1
            while left in dic:
                tmpLen += 1
                # visited[left] = 1
                del dic[left]
                left -= 1
            while right in dic:
                tmpLen += 1
                # visited[right] = 1
                del dic[right]
                right += 1
            maxLen = max(tmpLen, maxLen)
        return maxLen


# Test Cases
if __name__ == "__main__":
	solution = Solution()
