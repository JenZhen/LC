#!/usr/local/bin/python3
import linkedlist
# https://leetcode.com/problems/happy-number/
# Example
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer,
# replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
#
# Example:
#
# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
"""
Algo:
D.S.: Linked List/Array

核心思路，找环的存在
Solution1:
用set来记录访问过的点
Time： O(logn).

Solution2：
快慢指针
Time： O(logn).

Corner cases:
"""

class Solution1:
    def isHappy(self, n: int) -> bool:

        seen = set([n])
        while True:
            n = self.nextNum(n)
            if n == 1:
                return True
            if n not in seen:
                seen.add(n)
            else:
                return False

    def nextNum(self, num):
        digits = [int(ele) for ele in str(num)]
        return sum([ele ** 2 for ele in digits])


class Solution2:
    def isHappy(self, n: int) -> bool:
        p1 = n
        p2 = self.nextNum(n)

        while p2 != 1 and p1 != p2:
            # if p2 not reach 1 and p1 != p2 (not circle yet)
            p1 = self.nextNum(p1) # p1 one step
            p2 = self.nextNum(self.nextNum(p2)) # p2 two steps

        return p2 == 1

    def nextNum(self, num):
        digits = [int(ele) for ele in str(num)]
        return sum([ele ** 2 for ele in digits])

# Test Cases
if __name__ == "__main__":
	solution = Solution()
