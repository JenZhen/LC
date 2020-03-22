#!/usr/local/bin/python3

# https://leetcode.com/problems/largest-number/
# Example
# Given a list of non negative integers, arrange them such that they form the largest number.
#
# Example 1:
#
# Input: [10,2]
# Output: "210"
# Example 2:
#
# Input: [3,30,34,5,9]
# Output: "9534330"
# Note: The result may be very large, so you need to return a string instead of an integer.

"""
Algo: Sort
D.S.:

Solution:
Key: write Python Comparator
[3,30,34,5,9]
-> ['3','30','34','5','9']
in comparator, '3' vs '9', since '39' < '93', return order '3', '9'

Time: O(nlogn)
Space: O(1)
Corner cases:

[0,0] -> '0' not '00'
"""

class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted([str(ele) for ele in nums], key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

# Test Cases
if __name__ == "__main__":
    solution = Solution()
