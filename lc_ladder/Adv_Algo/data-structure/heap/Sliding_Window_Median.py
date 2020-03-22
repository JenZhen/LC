#! /usr/local/bin/python3

# https://www.lintcode.com/en/old/problem/sliding-window-median/
# Given an array of n integer, and a moving window(size k),
# move the window at each iteration from the start of the array, find the median of the element inside the window at each moving.
# (If there are even numbers in the array, return the N/2-th number after sorting the element in the window. )
# Example
# For array [1,2,7,8,5], moving window size k = 3. return [2,7,7]
# At first the window is at the start of the array like this
# [ | 1,2,7 | ,8,5] , return the median 2;
# then the window move one step forward.
# [1, | 2,7,8 | ,5], return the median 7;
# then the window move one step forward again.
# [1,2, | 7,8,5 | ], return the median 7;

"""
Algo:
D.S.: min/maxHeap

Solution:
Solution1: remove from heap takes O(n) -- Exceed time limit

Solution2: https://www.jiuzhang.com/solution/sliding-window-median/#tag-highlight-lang-python
# TODO:
Corner cases:
"""
from heapq import heappush, heappop, heapify
class DataStreamMedian(object):
    def __init__(self):
        self.median = None
        self.maxHeap = []
        self.minHeap = []

    def add(self, ele):
        if self.median == None:
            self.median = ele
        elif ele < self.median:
            heappush(self.maxHeap, -ele)
        else:
            heappush(self.minHeap, ele)

        if len(self.minHeap) > len(self.maxHeap) + 1:
            # rotate to left
            heappush(self.maxHeap, (-1) * self.median)
            self.median = heappop(self.minHeap)
        elif len(self.maxHeap) > len(self.minHeap):
            # rotate to right
            heappush(self.minHeap, self.median)
            self.median = -heappop(self.maxHeap)

    def remove(self, ele):
        if ele == self.median:
            if len(self.maxHeap) == len(self.minHeap):
                # move self.maxHeap top to median
                self.median = -heappop(self.maxHeap)
            elif len(self.maxHeap) + 1 == len(self.minHeap):
                # move minHeap top to median
                self.median = heappop(self.minHeap)
        elif ele < self.median:
            self.maxHeap = self._removeFromMaxHeap(self.maxHeap, ele)
            self._rotateHeaps()
        else:
            self.minHeap = self._removeFromMinHeap(self.minHeap, ele)
            self._rotateHeaps()

    def _removeFromMinHeap(self, heap, ele):
        tempList = []
        i = 0
        for i in range(len(heap)):
            if heap[i] != ele:
                tempList.append(heap[i])
            else:
                break
        tempList.extend(heap[i + 1:])
        heapify(tempList)
        return tempList

    def _removeFromMaxHeap(self, heap, ele):
        tempList = []
        i = 0
        for i in range(len(heap)):
            if heap[i] != -ele:
                tempList.append(heap[i])
            else:
                break
        tempList.extend(heap[i + 1:])
        heapify(tempList)
        return tempList

    def _rotateHeaps(self):
        lenMax = 0
        if self.maxHeap is not None:
            lenMax = len(self.maxHeap)
        lenMin = 0
        if self.minHeap is not None:
            lenMin = len(self.minHeap)
        if lenMax > lenMin:
            # rotate from left to right
            heappush(self.minHeap, self.median)
            self.median = -heappop(self.maxHeap)
        elif lenMin > lenMax + 1:
            # rotate from right to left
            heappush(self.maxHeap, (-1) * self.median)
            self.median = heappop(self.minHeap)

    def getMedium(self):
        return self.median

    def printList(self, list):
        print("[%s]" % (", ".join([str(ele) for ele in list])))

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        res = []
        if not nums or not k:
            return res
        ds = DataStreamMedian()
        # init the first k elements in the array
        for i in range(k):
            if i == len(nums):
                res.append(ds.getMedium())
                return res
            ds.add(nums[i])
        res.append(ds.getMedium())
        # iterate thru list nums do add/remove and getMedium
        for i in range(k, len(nums)):
            ds.add(nums[i])
            ds.remove(nums[i - k])
            res.append(ds.getMedium())
        ds.printList(res)
        return res


# Test Cases
if __name__ == "__main__":
    testCases = [
        {
            "nums": [1,2,7,8,5], #[2,7,7]
            "k": 3
        }
    ]
    s1 = Solution1()
    for t in testCases:
        nums = t["nums"]
        k = t["k"]
        res1 = s1.medianSlidingWindow(nums, k)
