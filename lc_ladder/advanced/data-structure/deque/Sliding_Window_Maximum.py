#! /usr/local/bin/python3

# Requirement
# Example

"""
Algo:
D.S.:

Solution:
Use deque as non ascending stack
Same as /lc_ladder/advanced/data-structure/heap/sliding_Window_Maximum.py

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
    s = Solution()
