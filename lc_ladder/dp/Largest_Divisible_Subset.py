#!/usr/bin/python

# http://lintcode.com/en/problem/largest-divisible-subset/
# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
# Notice
# If there are multiple solutions, return any subset is fine.
# Example
# Given nums = [1,2,3], return [1,2] or [1,3]
# Given nums = [1,2,4,8], return [1,2,4,8]

"""
Algo: Sequence DP
D.S.:

Solution:
- State: seq[] sequence of element in such sequence, pre[] previous element idx in the sequence
- Function:
- Initialization: seq[] init with all 0, ie, the 0th element of the sequence
                  pre[] init with all -1, ie, its previous element in the seq of idx -1 (no previous element)
- Answer: find the max value and its idx of seq, meaning the longest sequence, use pre[i] to trace back till pre[i] == -1

#Example:
idx: 0, 1, 2, 3, 4, 5, 6, 7
arr: 1, 2, 3, 4, 5, 6, 7, 8
seq: 0, 0, 0, 0, 0, 0, 0, 0
     1, 2, 2, 3, 2, 3, 2, 4
pre: -1,-1,-1,-1,-1,-1,-1,-1
     -1,0, 0, 1, 0, 2, 0, 3

res: 4 is max in seq, idx = 7; prevIdx = pre[idx] = 3; --> put 8 in
     prev: idx != -1; val = nums[idx] = 4; preIdx = pre[idx] = 2; --> put 4 in
     prev: idx != -1; val = nums[idx] = 2; preIdx = pre[idx] = 0; --> put 2 in
     prev: idx != -1; val = nums[idx] = 1; preIdx = pre[idx] = -1; --> put 1 in
     prev: idx == -1: end of iteration

Time: O(n ^ 2)
Space: O(3n)

Corner cases:
"""

class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset
    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        if not nums:
            return None
        if len(nums) <= 1:
            return nums
        # init
        length = len(nums)
        nums.sort()
        seq = [1] * length
        pre = [-1] * length
        # iterate through to calculate
        for i in range(1, length):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    seq[i] = seq[j] + 1
                    pre[i] = j
        # get answer array
        res = []
        maxSeq = 0
        maxIdx = 0
        maxPre = -1
        for i in range(length):
            if seq[i] > maxSeq:
                maxSeq = seq[i]
                maxPre = pre[i]
                maxIdx = i

        res.append(nums[maxIdx])
        while maxPre != -1:
            res.append(nums[maxPre])
            maxPre = pre[maxPre]
        repr(seq)
        repr(pre)
        res.reverse()
        return res

def repr(arr):
    if not arr:
        print("[]")
    else:
        print "[" + ", ".join([str(ele) for ele in arr]) + "]"

# Test Cases
if __name__ == "__main__":
    testCass = [
        [1, 2, 4], # 1, 2, 4
        [1, 3], # 1, 3
        [1, 2, 3, 4, 5, 6, 7, 8], # 1, 2, 4, 8
        [], # []
        [2], # [2]
    ]
    solution = Solution()
    for nums in testCass:
        res = solution.largestDivisibleSubset(nums)
        repr(res)
