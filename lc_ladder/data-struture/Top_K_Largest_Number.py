#!/usr/bin/python
# http://www.lintcode.com/en/problem/top-k-largest-numbers/
# Example
# Given [3,10,1000,-99,4,100] and k = 3.
# Return [1000, 100, 10].

"""
Algo:
D.S.: python heapq
from python built-in min heap -> max heap

Similar to Kth Largest Element

Solution:

Corner cases:
"""
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        if nums is None or len(nums) == 0:
            return None
        if k is None or k == 0:
            return None

        from heapq import heappush, heappop
        heap = []
        res = []
        # private method to maintain python max heap
        def _maxHeappush(heap, value):
            heappush(heap, value * (-1))
        def _maxHeappop(heap):
            return heappop(heap) * (-1)

        for i in nums:
            _maxHeappush(heap, i)
        for j in range(k):
            res.append(_maxHeappop(heap))
        return res

class Solution2:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        if nums is None or len(nums) == 0:
            return None
        if k is None or k == 0:
            return None

        from heapq import heappush, heappop, heapreplace
        heap = []

        # maintain a fixed-size min heap
        # -- Important: cannot implement fixed-size max heap using negationg method
        # size of k or less
        # min heap, new elemen compare with heap[0]
        # return revesed heap

        for i in nums:
            if len(heap) < k:
                heappush(heap, i)
            else:
                if heap[0] < i:
                    heapreplace(heap, i)

        return sorted(heap, reverse=True)

# Test Cases
if __name__ == "__main__":
	solution = Solution()
