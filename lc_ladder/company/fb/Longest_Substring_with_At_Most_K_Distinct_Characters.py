#! /usr/local/bin/python3

# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# Example
# Given a string, find the length of the longest substring T that contains at most k distinct characters.
#
# Example 1:
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# Example 2:
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.
"""
Algo: sliding window with dictionary
D.S.:

Solution:

Time: O(N)
Space: O(N) char_cnt map
Corner cases:
"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0
        i, j, res = 0, 0, 0
        char_cnt = {} # key: char, val: cnt
        while i < len(s):
            while j < len(s):
                if s[j] in char_cnt:
                    # if in char_cnt, add length, won't change len(char_cnt)
                    char_cnt[s[j]] += 1
                else:
                    # check size first, if == k break inner while
                    if len(char_cnt) == k:
                        break
                    # if less than k, add to char_cnt
                    char_cnt[s[j]] = 1
                j += 1

            # once inner while break, either j reach to len(s) or reach to k
            res = max(res, j - i)
            # reduce s[i] from char_cnt (remove if cnt == 0)
            if char_cnt[s[i]] == 1:
                del char_cnt[s[i]]
            else:
                char_cnt[s[i]] -= 1
            i += 1
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
