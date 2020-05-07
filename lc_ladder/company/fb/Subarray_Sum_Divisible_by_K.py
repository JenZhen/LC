#! /usr/local/bin/python3

# https://leetcode.com/problems/subarray-sums-divisible-by-k/submissions/
# Example
# Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.
# Example 1:
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#
# Note:
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
"""
Algo:
D.S.: map

Solution:
original: [4, 5, 0, -2, -3, 1]
presum  0, 4, 9, 9,  7,  4, 5
mod     0, 4, 4, 4,  2,  4, 0
cnt          +1,+2,     +3,+1 = 7

Time: O(n)
Space: O(n)
Corner cases:
"""

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        if not A: return []
        res = 0
        cnt_map = {0: 1}
        presum = 0
        for a in A:
            presum += a
            mod = presum % K
            if mod in cnt_map:
                res += cnt_map[mod]
                cnt_map[mod] += 1
            else:
                cnt_map[mod] = 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
