#!/usr/bin/python

# http://lintcode.com/en/problem/heapify/
# Example

"""
Algo: heap sort
D.S.:

Solution:
Must remember this classic heapsort

Corner cases:
"""

class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def helper(self, A, i):
        l = i * 2 + 1
        r = i * 2 + 2
        min = i
        if l < len(A) and A[l] < A[min]:
            min = l
        if r < len(A) and A[r] < A[min]:
            min = r
        if min != i:
            A[min], A[i] = A[i], A[min]
            self.helper(A, min)

    def heapify(self, A):
        # write your code here
        for i in range(len(A) / 2, -1, -1):
            self.helper(A, i)

    def printResult(self, A):
        print("Min-heap: ")
        print("->".join([str(ele) for ele in A]))
# Test Cases
if __name__ == "__main__":
    solution = Solution()
    A = [3,2,1,5,4]
    solution.heapify(A)
    solution.printResult(A)
