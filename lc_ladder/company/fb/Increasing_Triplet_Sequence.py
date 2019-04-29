#! /usr/local/bin/python3

# https://www.lintcode.com/problem/increasing-triplet-subsequence/description
# Example
# 给定未排序的数组，返回是否在数组中存在递增的长度为3的子序列。
#
# 完整的功能应为：
# 如果存在i, j, k，使得arr[i] < arr[j] < arr[k]，且0 ≤ i < j < k ≤ n-1，则返回true，否则返回false。
# 您的算法应该以O(n)时间复杂度和O(1)空间复杂度运行。
#
# 样例
# 样例1
#
# 输入： [1, 2, 3, 4, 5]
# 输出： true
# 样例2
#
# 输入： [5, 4, 3, 2, 1]
# 输出： false
"""
Algo:
D.S.:

Solution:
Time: O(n)
Space: O(1)

Corner cases:
"""

class Solution:
    """
    @param nums: a list of integers
    @return: return a boolean
    """
    def increasingTriplet(self, nums):
        # write your code
        if not nums or len(nums) < 3:
            return False

        import sys
        min1, min2 = sys.maxsize, sys.maxsize

        for i in nums:
            if i < min1:
                min2 = min1
                min1 = i
            if min1 < i < min2:
                min2 = i
            if i > min2:
                return True
        return False

# Test Cases
if __name__ == "__main__":
    solution = Solution()
