#! /usr/local/bin/python3

# https://www.lintcode.com/problem/sliding-window-maximum/description
# Example
# For array [1, 2, 7, 7, 8], moving window size k = 3. return [7, 7, 8]

"""
Algo:
D.S.: deque implemented monotonous stack

Solution:
slidingWindow -- maintain an interval, remove left then add right
    [1, 2, 7, 7, 8]
q:   1,
q:      2, (add 2 which is greater than 1, meaning 1 will never be used as window max, remove)
q:         7, (same for 2)
q:         7, 7, (the second 7 could be the max if the first 7 is popped)
q:               8 (7 will never be a window max if there's 8)
overall, q is an descending or flat deque
iterate for 0 -> len(nums) - 1
- Removal leftmost element starting when i is k
- Add to res list when i >= k - 1

Time: O(n)

# Jiuzhang Solution -- very hard to understand (index based)
https://www.jiuzhang.com/solution/sliding-window-maximum/#tag-highlight-lang-python

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
