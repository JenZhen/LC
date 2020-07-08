#! /usr/local/bin/python3

# https://leetcode.com/problems/largest-multiple-of-three/submissions/
# Example
# Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.
# Since the answer may not fit in an integer data type, return the answer as a string.
# If there is no answer return an empty string.
#
# Example 1:
# Input: digits = [8,1,9]
# Output: "981"
#
# Example 2:
# Input: digits = [8,6,7,1,0]
# Output: "8760"
#
# Example 3:
# Input: digits = [1]
# Output: ""
#
# Example 4:
# Input: digits = [0,0,0,0,0,0]
# Output: "0"
#
# Constraints:
# 1 <= digits.length <= 10^4
# 0 <= digits[i] <= 9
# The returning answer must not contain unnecessary leading zeros.
"""
Algo:
D.S.:

Solution:
原则
1，去除尽可能少的数
2，去除的数字尽可能小

Corner cases:
[0,0,0,0,0] --> 返回’0‘
[1,1,1,1,1] --> 去除2个1
[2,2,2,2,2] --> 去除2个2
[5,8] --> 都去除 没有了，返回‘’
"""
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        if not digits:
            return ''
        total = sum(digits)
        remain = total % 3
        if remain == 0:
            digits = sorted(digits, reverse = True)
            if digits[0] == 0: # [0,0,0,0]
                return '0'
            return ''.join([str(d) for d in digits])

        mp = {} # key: remain, val: sorted(list of digit)
        for i in range(3):
            mp[i] = []

        digits.sort()
        for d in digits:
            mp[d % 3].append(d)
        to_remove = []
        if mp[remain]:
            to_remove.append(mp[remain][0])
        else:
            if remain == 1:
                if len(mp[2]) < 2:
                    return False
                else:
                    to_remove.append(mp[2][0])
                    to_remove.append(mp[2][1])
            elif remain == 2:
                if len(mp[1]) < 2:
                    return False
                else:
                    to_remove.append(mp[1][0])
                    to_remove.append(mp[1][1])

        # remove elements in to_remove from digits
        new_digits = []
        to_remove.sort()
        i, j = len(digits) - 1, len(to_remove) - 1
        while i >= 0 and j >= 0:
            if digits[i] == to_remove[j]:
                i -= 1
                j -= 1
            else:
                new_digits.append(digits[i])
                i -= 1
        while i >= 0:
            new_digits.append(digits[i])
            i -= 1

        # new_digits are digits sorted from high to low
        if not new_digits:
            return ''
        elif new_digits[0] == 0:
            return '0'
        return ''.join([str(d) for d in new_digits])

# Test Cases
if __name__ == "__main__":
    solution = Solution()
