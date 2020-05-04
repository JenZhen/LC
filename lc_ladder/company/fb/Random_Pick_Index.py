#! /usr/local/bin/python3

# https://leetcode.com/problems/random-pick-index/submissions/
# Example
# Given an array of integers with possible duplicates, randomly output the index of a given target number.
# You can assume that the given target number must exist in the array.
# Note:
# The array size can be very large. Solution that uses too much extra space will not pass the judge.
#
# Example:
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
#
# // pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
# solution.pick(3);
#
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);
"""
Algo:
D.S.:

Solution1:
Time: O(1)
Space: O(n)

Solution2:
Time: O(n)
Space: O(1)
Corner cases:
"""
class Solution1:
    def __init__(self, nums: List[int]):
        self.dict = {} # key: nums, val: [idx]
        for i, num in enumerate(nums):
            if num not in self.dict:
                self.dict[num] = []
            self.dict[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.dict[target])

class Solution2:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        idx = random.randrange(len(self.nums))
        while self.nums[idx] != target:
            idx = random.randrange(len(self.nums))
        return idx

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
