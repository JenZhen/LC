#!/usr/bin/python

# http://www.jiuzhang.com/solution/two-sum-closest-to-target/
# Example

"""
Algo:
D.S.:

Solution:

Corner cases:
"""
class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumClosest(self, nums, target):
        # Write your code here
        # careful that when "target is None" and "target = 0"
        # not target is True
        if len(nums) < 2 or target is None:
            return None
        import sys
        minDiff = sys.maxsize
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                return 0
            elif total > target:
                minDiff = min(minDiff, total - target)
                r -= 1
            else:
                minDiff = min(minDiff, target - total)
                l += 1
        return minDiff


# Test Cases
if __name__ == "__main__":
    solution = Solution()
    testCases = [
        {"nums": [2,1,3,1],
        "target": 6}, #1
        {"nums": [1,1,5],
        "target": 0}, #2
        {"nums": [1,3,2],
        "target": 3}, #0
    ]
    for t in testCases:
        nums = t["nums"]
        target = t["target"]
        print("closest: %s" %(solution.twoSumClosest(nums, target)))
