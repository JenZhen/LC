#! /usr/local/bin/python3

# https://leetcode.com/problems/word-break-ii/submissions/
# Example
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# Example 2:
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []

"""
Algo: DFS with memo
D.S.:

Solution:
https://www.youtube.com/watch?v=JqOIRBC0_9c

左右两半分开后，DFS 哪一边都可以
一定要用memo 否则会超时
超时例子
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

Corner cases:
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {} # key: substring, value: List[str] wordBreak list
        return self.dfs(s, set(wordDict), memo)

    def dfs(self, s, dict, memo):
        if s in memo:
            return memo[s]

        ans = []
        if s in dict:
            ans.append(s)
        for j in range(1, len(s)):
            left = s[:j]
            right = s[j:]

            if right not in dict:
                continue

            left_ans = self.dfs(left, dict, memo)
            for sub_ans in left_ans:
                ans.append(sub_ans + " " + right)


        memo[s] = ans
        return ans

# Test Cases
if __name__ == "__main__":
    solution = Solution()
