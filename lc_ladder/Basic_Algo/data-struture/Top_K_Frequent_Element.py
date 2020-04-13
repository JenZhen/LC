#!/usr/local/bin/python3

# https://leetcode.com/problems/top-k-frequent-elements/
# Example
# Given a non-empty array of integers, return the k most frequent elements.
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""
Algo: collcetions.Counter, heapq
D.S.: min heap

Solution:
Time: O(nlogk)
Space: O(k)

Corner cases:
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or len(nums) == 0:
            return None
        if not k:
            return None
        from heapq import heappush, heappop
        counter = collections.Counter(nums)
        h = []
        for n, freq in counter.items():
            heappush(h, (freq, n))
            if len(h) > k:
                heappop(h)
        return [ele[1] for ele in h][::-1 ]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
