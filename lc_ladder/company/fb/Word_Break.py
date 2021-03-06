#! /usr/local/bin/python3

# Requirement
# https://www.lintcode.com/problem/word-break/description
# 给定字符串 s 和单词字典 dict，确定 s 是否可以分成一个或多个以空格分隔的子串，并且这些子串都在字典中存在。
#
# 样例
# 样例 1:
# 	输入:  "lintcode", ["lint", "code"]
# 	输出:  true
#
# 样例 2:
# 	输入: "a", ["a"]
# 	输出:  true
"""
Algo: DP, DFS
D.S.:

Solution:
DFS exceed time limit
DP best solution

Time: O(n * length of word)
f[i]: if first i char can be breakable in dict
f[0] = True
if f[i - j] is in dict, check if str[i - j: i] in dict,
if true, mark f[i] = True, to next i loop

Corner cases:
"""

class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if not s or not dict:
            return len(s) == 0

        n = len(s)
        f = [False for _ in range(n + 1)]
        f[0] = True
        maxlen = max([len(word) for word in dict])
        for i in range(1, n + 1):
            # i denotes if first i char can be breakable in dict
            for j in range(1, min(i, maxlen) + 1):
                # j denotes if the word length when search from i back to front
                if f[i - j] == False:
                    continue
                if s[i - j:i] in dict:
                    f[i] = True
                    break
        print(f)
        return f[n]


class Solution_DFS: #(Suggested)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wordDict 和memo 都可以当做参数 或是 self. 使用
        self.memo = {}
        dict = set(wordDict)
        return self.dfs(s, dict)

    def dfs(self, s, dict):
        if s in self.memo: return self.memo[s]
        # 整串在此考虑
        if s in dict:
            self.memo[s] = True
            return True
        # 在串中间分隔
        for j in range(1, len(s)):
            left = s[:j]
            right = s[j:]
            if right in dict and self.dfs(left, dict):
                self.memo[s] = True
                return True
        self.memo[s] = False
        return False

# Test Cases
if __name__ == "__main__":
    solution = Solution()
