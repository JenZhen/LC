#! /usr/local/bin/python3

# https://leetcode.com/problems/jump-game-ii/submissions/
# Example
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Note:
#
# You can assume that you can always reach the last index.
"""
Algo: Greedy
D.S.:

Solution1:

Time: O(N)
Space: O(1)

Solution2:
超时

Corner cases:
"""
class Solution_Greedy:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0
        jump = 0
        curFurthest = 0 # from current position i to how far
        lastFurthest = 0 # before current position i to how far

        for i in range(len(nums)):
            if lastFurthest < i:
                jump += 1
                lastFurthest = curFurthest
            curFurthest = max(curFurthest, nums[i] + i)
        return jump

class Solution2:
    def jump(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0

        f = [len(nums)] * len(nums)
        f[0] = 0
        for i in range(len(nums) - 1):
            for step in range(1, nums[i] + 1):
                if i + step < len(f):
                    f[i + step] = min(f[i + step], f[i] + 1)
        return f[-1]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
