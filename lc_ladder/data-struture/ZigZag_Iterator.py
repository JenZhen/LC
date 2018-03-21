#!/usr/bin/python

# ZigZag Iterator II
# Given two 1d vectors, implement an iterator to return their elements alternately.

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
