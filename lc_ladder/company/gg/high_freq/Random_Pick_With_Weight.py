#! /usr/local/bin/python3

# https://leetcode.com/problems/random-pick-with-weight/
# Example
# Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex
# which randomly picks an index in proportion to its weight.
#
# Note:
#
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# Example 1:
#
# Input:
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
# Example 2:
#
# Input:
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""
Algo: random， binary search，presum
D.S.:

Solution:
加权抽样
bisect, bisect_left

Corner cases:
"""

from random import randint
class Solution:

    def __init__(self, w: List[int]):
        self.presum = w
        for i in range(1, len(w)):
            self.presum[i] += self.presum[i - 1]
        self.sum = self.presum[-1]

    def pickIndex(self) -> int:
        rand = randint(1, self.sum)
        # return bisect.bisect_left(self.presum, rand)
        # 下面是bisect_left的二分法实现
        l, r = 0, len(self.presum) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if rand < self.presum[mid]:
                r = mid
            elif rand > self.presum[mid]:
                l = mid
            else: # equal
                return mid
        if rand <= self.presum[l]:
            return l
        else:
            return r


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Test Cases
if __name__ == "__main__":
    solution = Solution()
