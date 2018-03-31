#!/usr/bin/python

# http://lintcode.com/en/problem/merge-k-sorted-arrays/
# Example
# [
#   [1, 3, 5, 7],
#   [2, 4, 6],
#   [0, 8, 9, 10, 11]
# ]
# return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
"""
Algo:
D.S.: heapq

Solution:
This is a bit more complex than merge K sorted list.
After one element is popped from heap, how to retrieve what's next in its original list is unknow directly
Also, if list is out of range is unknown
Therefore, in the heap structure, key comparator is the val of element array, comes with it's arrays's idx and it's element idx in the array

Corner cases:
"""

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        if arrays is None or len(arrays) == 0:
            return None

        import heapq
        res = []
        # create a heap of
        # order at array value, with arrIdx for nth array, eleIdx
        heap = [(arrays[i][0], i, 0) for i in range(len(arrays)) if len(arrays[i]) > 0]
        heapq.heapify(heap)

        while len(heap):
            val, arrIdx, eleIdx = heapq.heappop(heap)
            res.append(val)
            if eleIdx < len(arrays[arrIdx]) - 1:
                eleIdx += 1
                heapq.heappush(heap, (arrays[arrIdx][eleIdx], arrIdx, eleIdx))
        return res
# Test Cases
if __name__ == "__main__":
	solution = Solution()
