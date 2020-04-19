#! /usr/local/bin/python3

# https://leetcode.com/problems/sliding-window-maximum/submissions/
# Example
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers in the window.
# Each time the sliding window moves right by one position. Return the max sliding window.
#
# Follow up:
# Could you solve it in linear time?
#
# Example:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
# Constraints:
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length

"""
Algo:
D.S.: 单调栈

Solution:
Use deque as non ascending stack
Same as /lc_ladder/advanced/data-structure/heap/sliding_Window_Maximum.py

Corner cases:
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # consider k == 0 or k > len(nums)
        res = []
        q = collections.deque([]) # list of tuple (nums[i], i)
        n = len(nums)

        for i in range(n):
            # 先考虑要不要把最左边的pop
            if i >= k:
                if q[0][1] == i - k:
                    q.popleft()
            # 考虑把前面比nums[i]小的都挪出去
            while q and nums[i] > q[-1][0]:
                q.pop()
            # 最后把这个新数放进来
            q.append((nums[i], i))

            # 只有在够K个数的时候才去选q最左边的最大数
            if i >= k - 1:
                res.append(q[0][0])
        return res

# Test Cases
if __name__ == "__main__":
    s = Solution()
