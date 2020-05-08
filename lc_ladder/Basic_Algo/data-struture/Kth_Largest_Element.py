#!/usr/bin/python

# http://www.lintcode.com/en/problem/kth-largest-element/
# Example
# In array [9,3,2,4,8], the 3rd largest element is 4.
# In array [1,2,3,4,5], the 1st largest element is 5, 2nd largest element is 4, 3rd largest element is 3 and etc.

"""
Algo: QuickSelect
D.S.: Heap, Array

Solution1:
Heap
Find largest number -> max heap
- In python, heapq is min heap. To convert to maxHeap, negate value when push, negate when pop
- In c++, priority queue is max heap.
std::priority_queue<int, std::vector<int>, mycomparison> myPQ
Takes type, container, comparator. use comparator to define min/max/customized heap

Find the Kth element
- option 1: iterate k times
- use fixed size heap

Solution2:
QuickSelect 经典模板， 适用于有相同数字的情况
Time： O(N) - average, O(N ^ 2) - worst case
Space: O(1)

[4, 1, 3, 2] - N = 4; K = 2
第K(2)大 --> 第3小 --> idx = 2 (N - K)
第K(2)小 --> 第3大 --> idx = 1 (K - 1)

Corner cases:
"""
class Solution1:
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



class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k)

    def quick_select(self, nums, l, r, target_idx):
        if l == r:
            return nums[l]

        # find the rightmost element to pivot, could be a random one within l, r
        pivot_idx = self.partition(nums, l, r)

        if target_idx == pivot_idx:
            return nums[target_idx]

        elif target_idx < pivot_idx:
            # 注意挪动的时候要pivot_idx + 1
            return self.quick_select(nums, l, pivot_idx - 1, target_idx)

        else:
            return self.quick_select(nums, pivot_idx + 1, r, target_idx)

    def partition(self, nums, l, r):
        i = l - 1 # i + 1 表示下一个比Pivot值小的数应该去的地方
        pivot_value = nums[r]

        for j in range(l, r):
            if nums[j] <= pivot_value:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        # 最后不要忘记挪动Pivot数，并返回
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    # parition can be
    def partition2(self, nums, l, r):
        i = l - 1 # i + 1 will be next number less than pivot value
        pivot_value = nums[r]

        for j in range(l, r + 1):
            if nums[j] <= pivot_value:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        return i

# Test Cases
if __name__ == "__main__":
