#! /usr/local/bin/python3

# https://leetcode.com/problems/maximum-swap/solution/
# Example
# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.
#
# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
# Note:
# The given number is in the range [0, 108]

"""
Algo:
D.S.:

Solution:
1993
9931
和最大情况相比，第一位应该是个9
从后面找那个9个当前比9小的数来swap
后面有2个9， 要找后面的一个9因为前面的9 肯定比前面要换下去的1大，所以换最后面的9，
可以从后往前找到最后的一个9

Time: O(nlogn) -- n is length of num
Space: O(n)
Corner cases:
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        if not num:
            return num
        origin_s = [c for c in str(num)]
        sorted_s = sorted(origin_s)[::-1]
        print(origin_s)
        print(sorted_s)
        if origin_s == sorted_s:
            return num

        i = 0
        while i < len(origin_s):
            if origin_s[i] != sorted_s[i]:
                break
            i += 1

        j = len(origin_s) - 1
        while j > i:
            if origin_s[j] == sorted_s[i]:
                break
            j -= 1
        origin_s[i], origin_s[j] = origin_s[j], origin_s[i]
        return int(''.join(origin_s))

# Test Cases
if __name__ == "__main__":
    solution = Solution()
