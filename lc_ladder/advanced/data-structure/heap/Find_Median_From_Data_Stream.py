#! /usr/local/bin/python3

# Requirement
# Numbers keep coming, return the median of numbers at every time a new number added.
# Clarification
# What's the definition of Median?
# - Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is A[(n - 1) / 2].
# For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.
# Example
# For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3].
# For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3].
# For numbers coming list: [2, 20, 100], return [2, 2, 20].
# Example

"""
Algo:
D.S.: Heap

Solution:
There are ways to build min/max heaps for finding median
1. minHeap, maxHeap and a median number
    result is always maintained as the median number

Example:
array: [1, 2, 3, 4, 5]
result:[1, 2, 2, 3, 3]
        median
        1(1)
maxHeap     minHeap

add(1): 1 locates as median
add(2): 2 > median(1), add to minHeap, len(minHeap) > len(maxHeap)
        move 1 to maxHeap, pop 2 from minHeap, add 2 as median

2. minHeap, and maxHeap
    insert to maintain size of heaps equal of differ by 1
        - if equal, median is the minHeap.top()
        - if not equal, median is the larger heap top()
Example:
array: [1, 2, 3, 4, 5]
result:[1, 2, 2, 3, 3]

Corner cases:
"""
from heapq import heappush, heappop
class Solution1:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """

    def medianII(self, nums):
        # write your code here
        res = []
        if not nums:
            return res
        self.minHeap, self.maxHeap = [], []
        self.median =  None
        for ele in nums:
            self.add(ele)
            res.append(self.getMedium())
        self.printRes(res)
        return res

    def add(self, ele):
        if self.median == None:
            self.median = ele
        elif ele < self.median:
            heappush(self.maxHeap, -ele)
        else:
            heappush(self.minHeap, ele)

        if len(self.minHeap) > len(self.maxHeap) + 1:
            # rotate to left
            heappush(self.maxHeap, -self.median)
            self.median = heappop(self.minHeap)
        elif len(self.maxHeap) > len(self.minHeap):
            # rotate to right
            heappush(self.minHeap, self.median)
            self.median = -heappop(self.maxHeap)

    def getMedium(self):
        return self.median

    def printRes(self, res):
        print("[%s]" % (", ".join([str(ele) for ele in res])))


class Solution2:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        res = []
        if not nums:
            return res
        self.minHeap, self.maxHeap = [], []
        for ele in nums:
            self.add(ele)
            res.append(self.getMedium())
        self.printRes(res)
        return res

    def add(self, ele):
        if not self.maxHeap:
            # if both empty, starting from maxHeap (lelf side)
            heappush(self.maxHeap, -ele)
        else:
            # if maxHeap (left) not empty, right may empty
            if ele < -self.maxHeap[0]:
                heappush(self.maxHeap, -ele)
            else:
                heappush(self.minHeap, ele)

            if len(self.minHeap) > len(self.maxHeap) + 1:
                heappush(self.maxHeap, (-1) * heappop(self.minHeap))
            if len(self.maxHeap) > len(self.minHeap) + 1:
                heappush(self.minHeap, (-1) * heappop(self.maxHeap))

    def getMedium(self):
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0] # means top()
        else:
            return -self.maxHeap[0]

    def printRes(self, res):
        print("[%s]" % (", ".join([str(ele) for ele in res])))

# Test Cases
if __name__ == "__main__":
    testCases = [
        [1, 2, 3, 4, 5], #return [1, 1, 2, 2, 3].
        [4, 5, 1, 3, 2, 6, 0], #return [4, 4, 4, 3, 3, 3, 3].
        [2, 20, 100], #return [2, 2, 20].
        [5,-10,4], #return [5,-10,4]
    ]
    s1 = Solution1()
    s2 = Solution2()
    for nums in testCases:
        res1 = s1.medianII(nums)
        res2 = s2.medianII(nums)
