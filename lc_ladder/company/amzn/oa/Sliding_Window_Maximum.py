#! /usr/local/bin/python3

# https://www.lintcode.com/problem/sliding-window-maximum/description?_from=ladder&&fromId=62
# Example

# 给出一个可能包含重复的整数数组，和一个大小为 k 的滑动窗口, 从左到右在数组中滑动这个窗口，找到数组中每个窗口内的最大值。
#
# 样例
# 给出数组 [1,2,7,7,8], 滑动窗口大小为 k = 3. 返回 [7,7,8].
#
# 解释：
#
# 最开始，窗口的状态如下：
#
# [|1, 2 ,7| ,7 , 8], 最大值为 7;
#
# 然后窗口向右移动一位：
#
# [1, |2, 7, 7|, 8], 最大值为 7;
#
# 最后窗口再向右移动一位：
#
# [1, 2, |7, 7, 8|], 最大值为 8.
#
# 挑战
# O(n)时间，O(k)的额外空间

"""
Algo:
D.S.: deque

Solution:


Corner cases:
"""

from collections import deque
class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        q = deque()
        result = []
        if len(nums) < k or k == 0:
            return []

        n = len(nums)
        for i in range(n):
            # handle remove window leftmost element
            if i >= k and nums[i - k] == q[0]:
                q.popleft()
            # iterate all potential pop before adding new element
            while len(q) and nums[i] > q[-1]:
                q.pop()
            q.append(nums[i])
            # add max to res only when i >= k - 1
            if i >= k - 1:
                result.append(q[0])
        return result;


# Test Cases
if __name__ == "__main__":
    solution = Solution()
