#! /usr/local/bin/python3

# https://leetcode.com/problems/strobogrammatic-number/submissions/
# Example
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
# Example 1:
# Input:  "69"
# Output: true
# Example 2:
# Input:  "88"
# Output: true
# Example 3:
# Input:  "962"
# Output: false
"""
Algo: map
D.S.:

Solution:

Time: O(n)
Space: O(1)
Corner cases:
"""

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if not num: return True

        MAP = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        l, r = 0, len(num) - 1
        while l <= r:
            # 注意要急着考虑 不满足的条件，否则MAP[]有KEY error
            if num[l] not in MAP or num[r] not in MAP:
                return False
            if MAP[num[r]] != num[l]:
                return False
            l += 1
            r -= 1
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
