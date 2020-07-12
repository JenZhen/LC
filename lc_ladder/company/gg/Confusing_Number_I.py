#! /usr/local/bin/python3

# https://leetcode.com/problems/confusing-number/
# Example
# Given a number N, return true if and only if it is a confusing number, which satisfies the following condition:
# We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees,
# they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.
# A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.
#
# Example 1:
# Input: 6
# Output: true
# Explanation:
# We get 9 after rotating 6, 9 is a valid number and 9!=6.
#
# Example 2:
# Input: 89
# Output: true
# Explanation:
# We get 68 after rotating 89, 86 is a valid number and 86!=89.
#
# Example 3:
# Input: 11
# Output: false
# Explanation:
# We get 11 after rotating 11, 11 is a valid number but the value remains the same, thus 11 is not a confusing number.
#
# Example 4:
# Input: 25
# Output: false
# Explanation:
# We get an invalid number after rotating 25.
#
# Note:
#
# 0 <= N <= 10^9
# After the rotation we can ignore leading zeros,
# for example if after rotation we have 0008 then this number is considered as just 8.
"""
Algo:
D.S.: Map

Solution:
Time:O(N)
Space: O(1)

Corner cases:
"""

class Solution:
    def confusingNumber(self, N: int) -> bool:
        if N is None:
            return False
        mp = {'0': '0',
              '1': '1',
              '8': '8',
              '6': '9',
              '9': '6'}
        nums = [char for char in str(N)]
        flag = False
        l, r = 0, len(nums) - 1
        while l <= r:
            if not self.isCN(nums[l]) or not self.isCN(nums[r]):
                return False
            if mp[nums[l]] != nums[r] or mp[nums[r]] != nums[l]:
                flag = True
            l += 1
            r -= 1
        return flag

    def isCN(self, char):
        if int(char) in set([0, 1, 6, 8, 9]):
            return True
        else:
            return False


# Test Cases
if __name__ == "__main__":
    solution = Solution()
