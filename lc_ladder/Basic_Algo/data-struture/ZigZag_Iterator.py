#!/usr/bin/python

# https://leetcode.com/problems/zigzag-iterator/
# Given two 1d vectors, implement an iterator to return their elements alternately.
# Example:
# Input:
# v1 = [1,2]
# v2 = [3,4,5,6]
# Output: [1,3,2,4,5,6]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
#
# Follow up:
# What if you are given k 1d vectors? How well can your code be extended to such cases?
#
# Clarification for the follow up question:
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
# If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:
#
# Input:
# [1,2,3]
# [4,5,6,7]
# [8,9]
#
# Output: [1,4,8,2,5,9,3,6,7].

"""
Algo:
D.S.: queue

Solution:
- use queue properties for iterately check each vector
- v.pop(0) get the first element available in the vector

Corner cases:
"""

class ZigzagIterator:

    # @param {int[]} v1 v2 two 1d vectors
    def __init__(self, v1, v2):
        # initialize your data structure here
        # 非常重要 的条件 if v 如果是[] 不要放进queue
        self.queue = [v for v in (v1, v2) if v]

    def next(self):
        # Write your code here
        # use list as queue and pop
        v = self.queue.pop(0)
        value = v.pop(0)
        # if a list gets empty do not push it back
        if v:
            self.queue.append(v)
        return value


    def hasNext(self):
        # Write your code here
        return len(self.queue) > 0


# Test Cases
if __name__ == "__main__":
    solution = Solution()
