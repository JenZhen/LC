#! /usr/local/bin/python3

# https://lintcode.com/problem/subarray-sum-ii/description
# Given an integer array, find a subarray where the sum of numbers is in a given interval. Your code should return the number of possible answers. (The element in the array should be positive)

# Example
# Given [1,2,3,4] and interval = [1,3], return 4. The possible answers are:

# [0, 0]
# [0, 1]
# [1, 1]
# [2, 2]

"""
Algo: presum
D.S.:

Solution:
Solution1: presum + brutal force, O(N^2)

Solution2: presum + binary search, O(Nlogn)??

idx   -1,  0, 1,  2,  3,
nums       1, 2,  3,  4,
presum 0,  1, 3,  6,  10,

sum[i:j] = pre[j] - pre[i - 1]
low <= sum[i:j] <= high  <==>
low <= pre[j] - pre[i - 1] <= high
TODO: 看不懂了

Corner cases:
"""

class Solution1:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        # write your code here
        if not A:
            return 0
        pre = [0]
        for i in A:
            pre.append(pre[-1] + i)
        cnt = 0
        for i in range(len(pre)):
            for j in range(i + 1, len(pre)):
                if start <= pre[j] - pre[i] <= end:
                    cnt += 1
        return cnt

class Solution2:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        # write your code here
        if not A:
            return 0
        pre = [0]
        for i in A:
            pre.append(pre[-1] + i)
        cnt = 0
        for i in range(1, len(pre)):
            low = self.find(pre, i, pre[i] - end)
            high = self.find(pre, i, pre[i] - start + 1)
            cnt += (high - low)
        return cnt
    def find(self, pre, i, target):
        if pre[i - 1] < target:
            return i
        l, r = 0, i - 1
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            if pre[mid] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
# Test Cases
if __name__ == "__main__":
    solution = Solution()
