#! /usr/local/bin/python3

# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/submissions/
# Example
# Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
# If there is no non-empty subarray with sum at least K, return -1.
#
# Example 1:
#
# Input: A = [1], K = 1
# Output: 1
# Example 2:
#
# Input: A = [1,2], K = 4
# Output: -1
# Example 3:
#
# Input: A = [2,-1,2], K = 3
# Output: 3
#
# Note:
#
# 1 <= A.length <= 50000
# -10 ^ 5 <= A[i] <= 10 ^ 5
# 1 <= K <= 10 ^ 9
"""
Algo: Monotonous Queue, presum, sliding window
D.S.:

Solution:
[0, -1, 2] k = 2 return 1
sliding window 2 pointers works well with all positive numbers
上例子中， 由于有负数，加起来的数变小，需要后面窗口前进

因为是sliding window 要缩进左端窗口，所以要用单调队列
单调栈、队列可以解决以上问题， 维护一个严格单调递增的队列，如果presume 变小， 就POP

Time: O(n)
Space: O(n)

Corner cases:
"""

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        presum = [0]
        for num in A:
            presum.append(presum[-1] + num)

        res = n + 1
        q = collections.deque()
        for i, num in enumerate(presum):
            while q and num <= presum[q[-1]]:
                # maintain a strictly increasing queue
                # q has index of presum
                q.pop()
            while q and num - presum[q[0]] >= K:
                res = min(res, i - q[0])
                q.popleft()
            q.append(i)
        return res if res < n + 1 else -1


# Test Cases
if __name__ == "__main__":
    s = Solution()
