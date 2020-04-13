#! /usr/local/bin/python3

# https://leetcode.com/problems/word-break/
# Example
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
"""
Algo:
D.S.:

Solution:
0. DFS no memo 会超时
1. DFS with memo (memo 记录子串) -- HuaHua Solution https://www.youtube.com/watch?v=ptlwluzeC1I
1.1 DFS with memo
2. BFS
3. DP (suggested)

Corner cases:
"""
class Solution0_DFS_NO_MEMO:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.dfs(s, set(wordDict), 0)

    def dfs(self, s, wordDict, start_idx):
        if start_idx == len(s):
            return True

        for end in range(start_idx + 1, len(s) + 1):
            left_string = s[start_idx:end]
            if left_string in wordDict and self.dfs(s, wordDict, end):
                return True
        return False

class Solution1_DFS: #(Suggested)
    # memo 也可带入DFS 函数做参数
    def __init__(self):
        # memo {} key: substring , val: if substring can do wordBreak
        self.memo = {}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict = set(wordDict)
        return self.dfs(s, dict)

    def dfs(self, s, dict):
        if s in self.memo: return self.memo[s]
        if s in dict:
            self.memo[s] = True
            return True
        for j in range(1, len(s)):
            left = s[:j]
            right = s[j:]
            if right in dict and self.dfs(left, dict):
                self.memo[s] = True
                return True
        self.memo[s] = False
        return False


class Solution1_1_DFS:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # memo[i] 截止到 s[i]以前能否满足字典分割
        memo = [None] * len(s)
        return self.dfs(s, set(wordDict), 0, memo)

    def dfs(self, s, wordDict, start_idx, memo):
        if start_idx == len(s):
            return True
        if memo[start_idx] != None:
            return memo[start_idx]

        for i in range(start_idx, len(s)):
            left_string = s[start_idx:(i + 1)]
            if left_string in wordDict and self.dfs(s, wordDict, i + 1, memo):
                memo[start_idx] = True
                return True
        memo[start_idx] = False
        return False


class Solution2_BFS:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        q = collections.deque([0]) # 以0开始能拼成一个词 找下一层能开始词的位置
        visited = set()
        while q:
            start = q.popleft()
            if start not in visited:
                for end in range(start + 1, len(s) + 1):
                    left_string = s[start:end]
                    if left_string in wordDict:
                        q.append(end)
                        if end == len(s):
                            return True
                visited.add(start)
        return False

class Solution3_DP:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True # 前n个字符能不能构成 或是 截止到i 前面一个位置能否构成
        # 固定SUBSTRING end
        for end in range(1, len(s) + 1):
            # 遍历START 的位置
            for start in range(end):
                if dp[start] and s[start:end] in wordDict:
                    dp[end] = True
        return dp[-1]
# Test Cases
if __name__ == "__main__":
    solution = Solution()
