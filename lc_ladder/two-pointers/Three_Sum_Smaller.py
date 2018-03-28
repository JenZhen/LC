#!/usr/bin/python

# http://lintcode.com/en/problem/3sum-smaller/
# Example

"""
Algo: 3Sum, 2Sum, two pointers sorted array, dup check
D.S.:

Solution:
Similar to Two Sum Less Than or Equal To Target
Note that the key difference of this problem is that
looking for different idx not element value, hence,
[-1, 0, 1] vs [-1, 0, 1] in array [-1, -1, 0, 1, 1] are different tuples
Remove all duplicate check, ie. the while loop compare with the pre/next value check are removed

Corner cases:
"""

class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        # Write your code here
        length = len(nums)
        if length < 3 or target is None:
            return 0
        nums.sort()
        res = 0
        for i in range(length - 2):
            l, r = i + 1, length - 1
            while l < r:
                ttl = nums[i] + nums[l] + nums[r]
                if ttl < target:
                    # once this right boundry is less than target
                    # any r less than it will be less than target
                    res += r - l
                    l += 1
                else:
                    r -= 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
