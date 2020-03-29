#!/usr/bin/python

# http://www.lintcode.com/en/problem/kth-largest-element/
# Example
# In array [9,3,2,4,8], the 3rd largest element is 4.
# In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.

"""
Algo:
D.S.:

Solution:
Find largest number -> max heap
- In python, heapq is min heap. To convert to maxHeap, negate value when push, negate when pop
- In c++, priority queue is max heap.
std::priority_queue<int, std::vector<int>, mycomparison> myPQ
Takes type, container, comparator. use comparator to define min/max/customized heap

Find the Kth element
- option 1: iterate k times
- use fixed size heap
Corner cases:
"""
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if A is None or k is None or k == 0:
            return None

        from heapq import heappush, heappop
        heap = []
        res = None
        def _maxHeapPush(heap, value):
            negVal = value * (-1)
            heappush(heap, negVal)

        def _maxHeapPop(heap):
            return heappop(heap) * (-1)

        for i in A:
            _maxHeapPush(heap, i)

        for i in range(k):
            val = _maxHeapPop(heap)
            if i == k - 1:
                res = val
        return res

# Test Cases
if __name__ == "__main__":

