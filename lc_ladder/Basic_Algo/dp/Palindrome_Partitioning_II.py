#!/usr/bin/python

# https://leetcode.com/problems/palindrome-partitioning-ii/
# Example
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example:
#
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

"""
Algo: DP
D.S.:

Solution:
- State:
- Function:
- Initialization:
- Answer:

Time: O(N^2)
Space: O(N^2)

Solution1：
超时

Solution2：
在判断字符串是否是回文的地方进行优化
注意矩阵DP 填充技巧

Corner cases:
"""

class Solution_Basic:
    def minCut(self, s: str) -> int:
        if not s or self.is_palindrome(s):
            return 0

        #  0 | 1 | 2 | 3
        # "" | a | a | b
        # -1 | 0 | 0 | 1

        dp = [i for i in range(len(s) + 1)]
        dp[0] = -1
        for j in range(1, len(s) + 1):
            for i in range(j):
                if self.is_palindrome(s[i:j]):
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]

    def is_palindrome(self, string):
        l, r = 0, len(string) - 1
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True

class Solution_Optimal:
    def minCut(self, s: str) -> int:
        if not s:
            return 0

        #    | 0 | 1 | 2
        #    | a | a | b
        #  a | T | T | F
        #  a | 0 | T | F
        #  b | 0 | 0 | T
        # 注意 这个是DP 填充技巧，可以利用中间结果 is_palindrome[i + 1][j - 1]
        is_palindrome = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            # 行： 从下往上
            for j in range(i, len(s)):
                # 列：从左往右
                if i == j:
                    is_palindrome[i][j] = True
                elif i + 1 == j and s[i] == s[j]:
                    is_palindrome[i][j] = True
                elif s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = True

        # print(is_palindrome)
        dp = [len(s) for _ in range(len(s))]
        dp[0] = 0
        for j in range(len(s)):
            if is_palindrome[0][j]:
                dp[j] = 0
                continue
            for i in range(j):
                if is_palindrome[i + 1][j]:
                    dp[j] = min(dp[j], dp[i] + 1)
        # print(dp)
        return dp[-1]

# Test Cases
if __name__ == "__main__":
    solution = Solution()
