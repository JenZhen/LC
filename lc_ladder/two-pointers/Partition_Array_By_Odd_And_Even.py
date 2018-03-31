#!/usr/bin/python

# http://lintcode.com/en/problem/partition-array-by-odd-and-even/
# Example
# Partition an integers array into odd number first and even number second.
# Given [1, 2, 3, 4], return [1, 3, 2, 4]

"""
Algo: two pointers
D.S.:

Solution:
Solution2 and 3 mapps to Parition Array solution 2 and 3
Solution1 takes extra O(n) space
Corner cases:
"""

class Solution1:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        # In the example, original order is maintained
        odd = []
        even = []
        for n in nums:
            if n % 2 == 1:
                odd.append(n)
            else:
                even.append(n)
        return odd + even


class Solution2:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] % 2 == 1:
                l += 1
            while l < r and nums[r] % 2 == 0:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

class Solution3:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        i, evenIdx = 0, len(nums) - 1
        while i < evenIdx:
            if nums[i] % 2 == 0:
                nums[i], nums[evenIdx] = nums[evenIdx], nums[i]
                evenIdx -= 1
            else:
                i += 1
        return nums

# Test Cases
if __name__ == "__main__":
    solution1 = Solution1()
    solution2 = Solution2()
    solution3 = Solution3()
    testCases = [
        {"nums": [2147483644,2147483645,2147483646,2147483647]},
    ]
    for t in testCases:
        nums = t["nums"]
        res1 = solution1.partitionArray(nums)
        print("res1: %s" %res1)
        res2 = solution2.partitionArray(nums)
        print("res2: %s" %res2)
        res3 = solution3.partitionArray(nums)
        print("res3: %s" %res3)
