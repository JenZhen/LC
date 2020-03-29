#!/usr/bin/python

# http://www.lintcode.com/en/problem/top-k-largest-numbers-ii/
# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Example
#
# Implement a data structure, provide two interfaces:
# add(number). Add a new number in the data structure.
# topk(). Return the top k largest numbers in this data structure. k is given when we create the data structure.

# s = new Solution(3);
# >> create a new data structure.
# s.add(3)
# s.add(10)
# s.topk()
# >> return [10, 3]
# s.add(1000)
# s.add(-99)
# s.topk()
# >> return [1000, 10, 3]
# s.add(4)
# s.topk()
# >> return [1000, 10, 4]
# s.add(100)
# s.topk()
# >> return [1000, 100, 10]

"""
Algo:
D.S.:python heapq
from python built-in min heap -> max heap

Solution:

Corner cases:
"""
from heapq import heappush, heappop, heapreplace
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.k = k
        self.heap = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if len(self.heap) < self.k:
            heappush(self.heap, num)
        elif self.heap[0] < num:
            heapreplace(self.heap, num)
    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        return sorted(self.heap, reverse=True)

# Test Cases
if __name__ == "__main__":
	solution = Solution()
