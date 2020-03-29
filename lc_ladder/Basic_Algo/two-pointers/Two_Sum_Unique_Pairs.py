#!/usr/bin/python

# http://www.jiuzhang.com/solution/two-sum-unique-pairs/
# Example
# Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

"""
Algo:
D.S.: map, two pointers

Solution:
Solution1: sort array, two pointers check from two ends,
            if duplicate, keep moving
    Time: O(nlogn) (sort + traverse)
    Space: O(1)

Solution2: no sort, no removal of dup from array,
            use map visited to check if element/pair has been checked
    Time: O(n)
    Space: O(n)

Corner cases:
- [1,1,1,1,1,1] target: 2
    - For Solution1: tricky when move l, r to next element not same with prev and within range
    - For Solution2:
"""

class Solution1:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if len(nums) < 2 or not target:
            return 0

        def moveToNextLeft(l):
            l += 1
            while l < len(nums) and \
                  nums[l] == nums[l - 1]:
                l += 1
            return l - 1 if l == len(nums) else l
        def moveToNextRight(r):
            r -= 1
            while r >= 0 and \
                  nums[r] == nums[r + 1]:
                r -= 1
            return 0 if r == 0 else r

        nums.sort()
        l, r = 0, len(nums) - 1
        cnt = 0
        while l < r:
            total = nums[l] + nums[r]
            if total > target:
                r = moveToNextRight(r)
            elif total < target:
                l = moveToNextLeft(l)
            else:
                cnt += 1
                l = moveToNextLeft(l)
                r = moveToNextRight(r)
        return cnt


class Solution2:
    """
    @param: nums: an array of integer
    @param: target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if len(nums) < 2 or not target:
            return 0

        # key: element
        # val: boolean, False, traversed, not paired;
        #               True, paired with some other element
        visited = {}
        cnt = 0
        for i in nums:
            other = target - i
            if other in visited:
                if visited[other] == False:
                    visited[other] = True
                    visited[i] = True
                    cnt += 1
            else:
                visited[i] = False
        return cnt

# Test Cases
if __name__ == "__main__":
    testCases = [
        {"nums": [1,1,1,1], "target": 2}, #1
        {"nums": [2,2,1,1,4,3], "target": 5}, #2
    ]
    solution1 = Solution1()
    solution2 = Solution2()
    for test in testCases:
        nums = test["nums"]
        target = test["target"]
        print("solution1: %s" %solution1.twoSum6(nums, target))
        print("solution2: %s" %solution2.twoSum6(nums, target))

