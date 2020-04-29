#! /usr/local/bin/python3

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Example
# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
Algo: two pointers; sliding window
D.S.:

Solution:
Time: O(N)
Space: O(N)

Similar to:
Minimum Window Substring
一个window 有左右两个指针
外层遍历左边指针
内层遍历右边指针 - 条件1）不越界2）满足题意条件 调节 sliding window

Corner cases:
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        right, res = 0, 0
        idx_map = {}
        for left in range(len(s)):
            while right < len(s) and s[right] not in idx_map:
                idx_map[s[right]] = 1
                res = max(res, right - left + 1)
                right += 1
            if right < len(s):
                del idx_map[s[left]]
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
