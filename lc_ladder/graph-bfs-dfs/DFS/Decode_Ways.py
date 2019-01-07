#! /usr/local/bin/python3

# https://leetcode.com/problems/decode-ways/
# Example
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

"""
Algo: DFS, DP
D.S.:

Solution:
1. DFS (TIME LIMIT)
2. DP
dp[i] = 前i个元素有几种方法
init: dp[0] 前0个元素default有1中方法，就是不拿
      dp[i] 前1个元素有几种，如果不为‘0’就有1种，否则有0种 *Corner cases*
dp: 检查第i个元素的时候
1. 如果它不为零，可以单独取，dp值和前一个一样 dp[i] = dp[i - 1]
2. 如果可以和前一位合作，要求前一位不是‘0’，而且和前一位在【1，26】以内，dp值和dp[i - 2]一样

Corner cases:
"""

class SolutionDP:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(dp)):
            if s[i - 1] != '0':
                # if ith element in s is not 0, it can be used alone
                # count same as prev digit
                dp[i] += dp[i - 1]
            if s[i - 2] != '0' and 0 < int(s[i - 2 : i]) < 27:
                # if prev position is not '0', then we check if can go with it
                # if yes, same cnt as dp[i - 2]
                dp[i] += dp[i - 2]
        return dp[-1]


class SolutionDFS:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        ans = [0]
        startIdx = 0
        self.dfs(s, ans, startIdx)
        return ans[0]

    def dfs(self, s, ans, startIdx):
        if startIdx == len(s):
            ans[0] += 1
            return
        for i in range(startIdx, startIdx + 2):
            if i == len(s):
                return
            subStr = s[startIdx:(i + 1)]
            # print("substr: " + subStr)
            if not self.inRange(subStr):
                continue
            self.dfs(s, ans, i + 1)

    def inRange(self, str):
        if str[0] == '0': return False
        return 0 < int(str) < 27


# Test Cases
if __name__ == "__main__":
    testCases = [
        "",     # 0
        None,   # 0
        "1",    # 1
        "0",    # 0
        "123",  # 3
        "101",  # 1
        "110",  # 1
        "111",  # 3
    ]
    s1 = SolutionDFS()
    s2 = SolutionDP()
    for t in testCases:
        res1 = s1.numDecodings(t)
        res2 = s2.numDecodings(t)
        print(res1)
        print(res2)
