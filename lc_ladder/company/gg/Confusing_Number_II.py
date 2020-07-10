#! /usr/local/bin/python3

# https://leetcode.com/problems/confusing-number-ii/
# Example
# We can rotate digits by 180 degrees to form new digits.
# When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively.
# When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.
#
# A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.
# (Note that the rotated number can be greater than the original number.)
#
# Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.
#
# Example 1:
#
# Input: 20
# Output: 6
# Explanation:
# The confusing numbers are [6,9,10,16,18,19].
# 6 converts to 9.
# 9 converts to 6.
# 10 converts to 01 which is just 1.
# 16 converts to 91.
# 18 converts to 81.
# 19 converts to 61.
# Example 2:
#
# Input: 100
# Output: 19
# Explanation:
# The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90,91,98,99,100].
#
# Note:
#
# 1 <= N <= 10^9

"""
Algo: Backtracking, DFS Search
D.S.:

Solution:
Time: O(5 ^ len(N))

Corner cases:
"""
class Solution1:
    def confusingNumberII(self, N: int) -> int:
        self.N = N
        self.confuse_mp = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        self.res = 0
        for d in self.confuse_mp:
            if d != 0:
                # 从 每个confusing 数开始 search, 把当前数的rotate 也算好，传进去
                self.dfs(d, self.confuse_mp[d], 10)
        return self.res

    def dfs(self, n, rotate, digit):
        if n > self.N:
            return
        if n != rotate:
            self.res += 1
        for d in self.confuse_mp:
            num = n * 10 + d
            self.dfs(num, self.confuse_mp[d] * digit + rotate, digit * 10)

class Solution2:
    def confusingNumberII(self, N: int) -> int:
        self.res = 0
        self.dfs(0, N)
        return self.res

    def dfs(self, num, N):
        if num > N:
            return
        if num != 0 and num != self.rotate(num):
            self.res += 1
        if num != 0:
            # append 0 at the end of num
            self.dfs(num * 10, N)
        # append 0 at the end of num
        self.dfs(num * 10 + 1, N)
        # append 0 at the end of num
        self.dfs(num * 10 + 6, N)
        # append 0 at the end of num
        self.dfs(num * 10 + 8, N)
        # append 0 at the end of num
        self.dfs(num * 10 + 9, N)

    def rotate(self, num):
        mp = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }
        res = 0
        while num:
            digit = num % 10
            num = num // 10
            res = res * 10 + mp[digit]
        # print(res)
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
