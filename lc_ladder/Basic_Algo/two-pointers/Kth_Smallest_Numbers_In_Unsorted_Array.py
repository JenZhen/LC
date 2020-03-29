#!/usr/bin/python

# http://www.jiuzhang.com/solution/kth-smallest-numbers-in-unsorted-array/
# Example

"""
Algo: heapq, min heap, max heap, two pointers(quick select)
D.S.: heap

Solution:
The best way is to use heap
Time Complexity O(n)
Space: Solution1 O(len(nums)), Solution2 O(k)
Corner cases:
"""
class Solution1:
    """
    @param: k: An integer
    @param: nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        from heapq import heappush, heappop
        if not nums:
            return None
        heap = []
        for i in nums:
            heappush(heap, i)
        res = None
        for i in range(k):
            res = heappop(heap)

        return res

class Solution2:
    """
    @param: k: An integer
    @param: nums: An integer array
    @return: kth smallest element
    make a max heap of size k,
    """
    def kthSmallest(self, k, nums):
        from heapq import heappush, heappop
        max_heap = []
        for num in nums:
            heappush(max_heap, -num)
            if len(max_heap) > k:
                heappop(max_heap)

        return - max_heap[0]

# Test Cases
if __name__ == "__main__":
    solution1 = Solution1()
    testCases = [
        {"nums": [5,2,4,3,1],
         "k": 4}, #4
        {"nums": [1,2,3],
         "k": 4}
    ]
    for t in testCases:
        nums = t["nums"]
        k = t["k"]
        res1 = solution1.kthSmallest(k, nums)
        print("res1: %s" %res1)
