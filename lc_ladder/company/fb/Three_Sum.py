#! /usr/local/bin/python3

# https://leetcode.com/problems/3sum/solution/
# Example

"""
Algo:
D.S.:

Solution:
Time: O(n^2) + O(nlogn)
Time: O(1)

Corner cases:
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []

        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while r > -1 and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    r -= 1
                    while r > -1 and nums[r] == nums[r + 1]:
                        r -= 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
