#! /usr/local/bin/python3

# https://leetcode.com/problems/word-pattern-ii/
# Example
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.
#
# Example 1:
#
# Input: pattern = "abab", str = "redblueredblue"
# Output: true
# Example 2:
#
# Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
# Output: true
# Example 3:
#
# Input: pattern = "aabb", str = "xyzabcxzyabc"
# Output: false
# Notes:
# You may assume both pattern and str contains only lowercase letters.

"""
Algo: 暴力DFS
D.S.:

Solution:


Corner cases:
"""
class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        p_to_s = {} # pattern to word map
        used_str = set() # set of word if has a pattern mapped, can be a map, but we don't need to lookup
        return self.dfs(pattern, str, p_to_s, used_str)

    def dfs(self, pattern, string, p_to_s, used_str):
        # exit:
        # 如果pattern 为空说明都遍历完了 如果 string也是空的就可以返回TRUE
        if not pattern:
            return not string

        char = pattern[0] # --> current pattern char

        # if char in p_to_s map
        if char in p_to_s:
            word = p_to_s[char]
            # string must start with this word
            if not string.startswith(word):
                return False
            return self.dfs(pattern[1:], string[len(word):], p_to_s, used_str)

        # if char not in p_to_s, ie. it's a new pattern，向下寻找可能对应的新词
        for i in range(len(string)):
            word = string[:(i + 1)]
            # 如果这次之前用过，说明对应了已知的PATTERN 但是上面逻辑排除了，所以跳过
            if word in used_str:
                continue

            p_to_s[char] = word
            used_str.add(word)
            # 如果下一层能满足，这层就能返回true
            if self.dfs(pattern[1:], string[len(word):], p_to_s, used_str):
                return True
            del p_to_s[char]
            used_str.remove(word)
        return False
# Test Cases
if __name__ == "__main__":
    solution = Solution()
