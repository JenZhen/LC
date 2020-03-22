#!/usr/bin/python

# http://www.jiuzhang.com/solution/partition-array-ii/
# Example
# Partition an unsorted integer array into three parts:
# The front part < low
# The middle part >= low & <= high
# The tail part > high
# Return any of the possible solutions.

"""
Algo:
D.S.:

Solution:
Using Partition Array Solution1 idea
Time: O(N)
Space: O(1

Corner cases:
- while loop condition is to i <= r, r meaning everything after r are examined
    hence need to check the case when i == r,
    to tell if nums[i] in < low or >= low <= high (if only 2 regions, like Partition Array, no need)
- whether to move i at when nums[i] < low and nums[i] < high
- if using swap method, original order will be disrupted.
"""

class Solution:
    # @param {int[]} nums an integer array
    # @param {int} low an integer
    # @param {int} high an integer
    # @return {int[]} any of the possible solutions
    def partition2(self, nums, low, high):
        # Write your code here
        if nums is None or \
            low is None or \
            high is None or \
            len(nums) == 0 or \
            low > high:
            return nums

        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] < low:
                nums[i], nums[l] = nums[l], nums[i]
                # IMPORTANT i >= l, which means nums[i] >= nums[l]
                # It's safe to move i to next position
                i += 1
                l += 1
            elif nums[i] > high:
                nums[i], nums[r] = nums[r], nums[i]
                # IMPORTANT:
                # when swap with nums[r], which is not examined
                # do not i += 1 unknown where nums[i] to go
                #i += 1
                r -= 1
            else:
                i += 1
        return nums

# Test Cases
if __name__ == "__main__":
    solution = Solution()
    testCases = [
        {
            "nums": [0,0,0,0],
            "low": 0,
            "high": 0
        },
        {
            "nums": [5,4,3,2,1],
            "low": 1,
            "high": 5
        },
        {
            "nums": [5,4,3,2,1],
            "low": 0,
            "high": 6
        },
        {
            "nums": [5,4,3,2,1],
            "low": 2,
            "high": 4
        },
    ]
    for t in testCases:
        nums = t["nums"]
        low = t["low"]
        high = t["high"]
        res = solution.partition2(nums, low, high)
        print("res: %s" %res)
