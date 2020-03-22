#! /usr/local/bin/python3

# https://www.lintcode.com/problem/maximum-average-subarray-ii/description
# Given an array with positive and negative numbers, find the maximum average subarray which length should be greater or equal to given length k.
# It's guaranteed that the size of the array is greater or equal to k.
# Example
# Given nums = [1, 12, -5, -6, 50, 3], k = 3
# Return 15.667 // (-6 + 50 + 3) / 3 = 15.667

"""
Algo: Binary Search
D.S.:

Solution:
Same with Maximum_Average_Subarray.py

1. 找到可行解的范围: min(nums), max(nums)
2. 猜答案 （二分）: 对可行解范围进行二分，因为可以取float，所以需要使用epsilon, 方法和sqrt_II相同 l + epsilon < r:
3. 检验条件，来判断答案应该在哪一侧
## TODO: 对子问题更加熟练
子问题：平均值为mid时，能不能找到一个子数组 使得子数组长度 >=k
如果有，说明可以尝试更大的平均值，l = mid, 反之，r = mid
剩余l,r位置，先尝试更大的r，如果不满足>=k，取l
4. 调整搜索范围
特征：**biggest** average that has length >= k

Time: O(len(nums) * log(max - min))
Corner cases:
"""

class Solution:
    """
    @param: nums: an array with positive and negative numbers
    @param: k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        if not nums or not k:
            return 0
        l, r = min(nums), max(nums)
        epsilon = 10 ** -6
        while l + epsilon < r:
            mid = (l + r) / 2
            if self.check(nums, k, mid):
                l = mid
            else:
                r = mid
        if self.check(nums, k, r):
            return r
        else:
            return l

    def check(self, nums, k, avg):
        ttl = [0] * (len(nums) + 1)
        minPre = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            ttl[i] = ttl[i - 1] + (nums[i - 1] - avg)
            minPre[i] = min(minPre[i - 1], ttl[i])

            if i >= k and ttl[i] - minPre[i - k] >= 0:
                return True
        return False

# Test Cases
if __name__ == "__main__":
    s = Solution()
