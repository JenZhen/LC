#! /usr/local/bin/python3

# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Example

"""
Algo: Binary Seary
D.S.:

Solution:
注意2种情况 按以下方式罗列清楚情况

Time: O(logn)
Space: O(1)

Corner cases:
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0 or target is None:
            return -1
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid
                else:
                    r = mid
        if nums[l] == target: return l
        if nums[r] == target: return r
        return -1

# Test Cases
if __name__ == "__main__":
    solution = Solution()
