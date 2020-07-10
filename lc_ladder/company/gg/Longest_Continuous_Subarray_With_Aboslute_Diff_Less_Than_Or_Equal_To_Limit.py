#! /usr/local/bin/python3

# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
# Example
# Given an array of integers nums and an integer limit,
# return the size of the longest non-empty subarray such that the absolute difference
# between any two elements of this subarray is less than or equal to limit.
#
# Example 1:
#
# Input: nums = [8,2,4,7], limit = 4
# Output: 2
# Explanation: All subarrays are:
# [8] with maximum absolute diff |8-8| = 0 <= 4.
# [8,2] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4] with maximum absolute diff |8-2| = 6 > 4.
# [8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
# [2] with maximum absolute diff |2-2| = 0 <= 4.
# [2,4] with maximum absolute diff |2-4| = 2 <= 4.
# [2,4,7] with maximum absolute diff |2-7| = 5 > 4.
# [4] with maximum absolute diff |4-4| = 0 <= 4.
# [4,7] with maximum absolute diff |4-7| = 3 <= 4.
# [7] with maximum absolute diff |7-7| = 0 <= 4.
# Therefore, the size of the longest subarray is 2.
# Example 2:
#
# Input: nums = [10,1,2,4,7,2], limit = 5
# Output: 4
# Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
# Example 3:
#
# Input: nums = [4,2,2,2,4,4,2,2], limit = 0
# Output: 3
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9e

"""
Algo: Monotonous queue
D.S.:

Solution:
Time: O(n)
Space: O(n)

Corner cases:
"""


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        min_q = deque([])
        max_q = deque([])
        res = 0
        l = 0
        for r in range(len(nums)):
            while min_q and nums[r] < min_q[-1]:
                min_q.pop()
            min_q.append(nums[r])
            while max_q and nums[r] > max_q[-1]:
                max_q.pop()
            max_q.append(nums[r])

            while max_q and min_q and max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[l]:
                    max_q.popleft()
                if min_q[0] == nums[l]:
                    min_q.popleft()
                l += 1
            res = max(res, r - l + 1)
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
