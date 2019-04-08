#! /usr/local/bin/python3

# https://www.lintcode.com/problem/palindrome-partitioning-ii/description
# Example
# 给定一个字符串s，将s分割成一些子串，使每个子串都是回文。
#
# 返回s符合要求的的最少分割次数。
#
# 样例
# 比如，给出字符串s = "aab"，
#
# 返回 1， 因为进行一次分割可以将字符串s分割成["aa","b"]这样两个回文子串
"""
Algo: DP, DFS(exceed memory)
D.S.:

Solution:
DP: n ^ 2
DFS: n * n !

Corner cases:
"""

class Solution_TOLONG:
    """
    @param s: A string
    @return: An integer
    """
    def minCut(self, s):
        ans = []
        subStrings = []
        self.dfs(s, subStrings, 0, ans)
        return min([len(li) for li in ans]) - 1


    def dfs(self, s, subStrings, startIdx, ans):
        if startIdx == len(s):
            ans.append(subStrings[:])
        for i in range(startIdx, len(s)):
            leftString = s[startIdx:(i + 1)]
            if not self.isPalindrome(leftString):
                continue
            subStrings.append(leftString)
            self.dfs(s, subStrings, i + 1, ans)
            subStrings.pop()

    def isPalindrome(self, string):
        size = len(string)
        if size <= 1:
            return True
        l, r = 0, size - 1
        while l < r:
            if string[l] != string[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

# Test Cases
if __name__ == "__main__":
    solution = Solution()
