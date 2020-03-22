#!/usr/bin/python

# http://www.jiuzhang.com/solution/two-sum-difference-equals-to-target/
# Example
# Given an array of integers, find two numbers that their difference equals to a target value.
# where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

"""
Algo:
D.S.:

Solution:

Corner cases:
"""
class Solution1:
    """
    @param nums {int[]} n array of Integer
    @param target {int} an integer
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """
    """
    Sort method
    """
    def twoSum7(self, nums, target):
        # Write your code here
        nums = [(num, i) for i, num in enumerate(nums)]
        target = abs(target)
        n, indexs = len(nums), []

        nums = sorted(nums, key=lambda x: x[0])

        j = 0
        for i in xrange(n):
            if i == j:
                j += 1
            while j < n and nums[j][0] - nums[i][0] < target:
                j += 1
            if j < n and nums[j][0] - nums[i][0] == target:
                indexs = [nums[i][1] + 1, nums[j][1] + 1]

        if indexs[0] > indexs[1]:
            indexs[0], indexs[1] = indexs[1], indexs[0]

        return indexs

class Solution2:
    """
    @param nums {int[]} n array of Integer
    @param target {int} an integer
    @return {int[]} [index1 + 1, index2 + 1] (index1 < index2)
    """
    """
    map method
    """
    def twoSum7(self, nums, target):
        # Write your code here
        if len(nums) < 2 or target is None:
            return [0, 0]
        # key: num value
        # val: num index in nums
        map = {}
        for i in range(len(nums)):
            if nums[i] - target in map:
                return [map[nums[i] - target] + 1, i + 1]
            if nums[i] + target in map:
                return [map[nums[i] + target] + 1, i + 1]
            map[nums[i]] = i


# Test Cases
if __name__ == "__main__":
    solution1 = Solution1()
    solution2 = Solution2()
    testCases = [
        {"nums": [7,2,5,9,3], "target": 6}, #[4,5]
        {"nums": [7,2,5,9,3], "target": 3}, #[2,3]
        {"nums": [4,2,4,1], "target": 0}, #[1,3]
    ]
    for t in testCases:
        nums = t["nums"]
        target = t["target"]
        print("Solution1: %s" %solution1.twoSum7(nums, target))
        print("Solution2: %s" %solution2.twoSum7(nums, target))
