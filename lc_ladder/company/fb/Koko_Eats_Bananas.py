#! /usr/local/bin/python3

# https://leetcode.com/problems/koko-eating-bananas/submissions/
# Example
# Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.
# The guards have gone and will come back in H hours.
# Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.
# If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.
# Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
# Return the minimum integer K such that she can eat all the bananas within H hours.
#
# Example 1:
# Input: piles = [3,6,7,11], H = 8
# Output: 4
# Example 2:
# Input: piles = [30,11,23,4,20], H = 5
# Output: 30
# Example 3:
# Input: piles = [30,11,23,4,20], H = 6
# Output: 23
#
# Note:
# 1 <= piles.length <= 10^4
# piles.length <= H <= 10^9
# 1 <= piles[i] <= 10^9
"""
Algo: Binary Search
D.S.:

Solution:
类似：
copy books
woodcut
Time: O(log(max(piles)) * len(piles))
Space: O(1)
Corner cases:
"""


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if len(piles) > H: return None
        l, r = 1, max(piles)
        while l + 1 < r:
            k = l + (r - l) // 2
            if self.need_time(piles, k) <= H:
                r = k
            else:
                l = k
        if self.need_time(piles, l) < H:
            return l
        return r

    def need_time(self, piles, k):
        res = 0
        for p in piles:
            res += p // k
            remain = p % k
            if remain:
                res += 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
